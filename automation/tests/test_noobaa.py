"""Offline regression tests for GPTEINFRA-18445.

Requires Helm, PyYAML, Jinja2 and ansible-core. Run from any working directory:
    python -m unittest discover -s automation/tests -p 'test_noobaa.py' -v
"""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from ansible.plugins.filter.core import FilterModule
from jinja2 import ChainableUndefined
from jinja2.nativetypes import NativeEnvironment
import yaml


ROOT = Path(__file__).resolve().parents[2]
ROLE = ROOT / 'automation/ansible/roles/ocp4_workload_dev_days_rdshw_cluster_bootstrap'
CHART = ROOT / 'automation/gitops/cluster/noobaa'
PARENT = ROOT / 'automation/gitops/cluster/app-of-apps'
PREFIX = 'ocp4_workload_dev_days_rdshw_'
ENV = NativeEnvironment(undefined=ChainableUndefined)
ENV.filters.update(FilterModule().filters())
TASKS = yaml.safe_load((ROLE / 'tasks/noobaa.yml').read_text())


def evaluate_facts(context):
    context = copy.deepcopy(context)
    for task in TASKS:
        for key, expression in task.get('ansible.builtin.set_fact', {}).items():
            context[key] = ENV.from_string(expression).render(context)
    return context


def scenario(platform='AWS', existing=False, managed=False, mode='auto', storage=''):
    context = {
        PREFIX + 'noobaa_install': mode,
        PREFIX + 'noobaa_storage_class': storage,
        PREFIX + 'gitops_repo': 'https://github.com/rhpds/dev-day-roadshow.git',
        'r_dev_days_noobaa_system': {'resources': [{}] if existing else []},
        'r_dev_days_noobaa_app': {'resources': []},
        'r_api_url': {'resources': [{'status': {'platformStatus': {'type': platform}}}]},
    }
    if managed:
        context['r_dev_days_noobaa_app']['resources'] = [{'spec': {'source': {
            'repoURL': context[PREFIX + 'gitops_repo'],
            'path': 'automation/gitops/cluster/noobaa',
        }}}]
    return context


def helm(chart, values):
    with tempfile.TemporaryDirectory() as directory:
        fixture = Path(directory) / 'values.yaml'
        fixture.write_text(yaml.safe_dump(values))
        result = subprocess.run(
            ['helm', 'template', 'test', str(chart), '--namespace', 'openshift-storage',
             '--values', str(fixture)], capture_output=True, text=True, check=True)
        return [doc for doc in yaml.safe_load_all(result.stdout) if doc]


class BootstrapTests(unittest.TestCase):
    def test_fresh_aws_installs_on_gp3(self):
        result = evaluate_facts(scenario())
        self.assertIs(result['r_dev_days_noobaa_install'], True)
        self.assertEqual(result['r_dev_days_noobaa_storage_class'], 'gp3-csi')

    def test_fresh_cnv_preserves_ceph(self):
        result = evaluate_facts(scenario('None'))
        self.assertIs(result['r_dev_days_noobaa_install'], True)
        self.assertEqual(result['r_dev_days_noobaa_storage_class'],
                         'ocs-external-storagecluster-ceph-rbd')

    def test_existing_cnv_noobaa_is_not_adopted(self):
        result = evaluate_facts(scenario('None', existing=True))
        self.assertIs(result['r_dev_days_noobaa_install'], False)

    def test_skipped_noobaa_lookup_without_crd(self):
        context = scenario()
        context['r_dev_days_noobaa_system'] = {'skipped': True}
        self.assertIs(evaluate_facts(context)['r_dev_days_noobaa_install'], True)

    def test_rerun_keeps_own_noobaa_application_enabled(self):
        result = evaluate_facts(scenario(existing=True, managed=True))
        self.assertIs(result['r_dev_days_noobaa_install'], True)

    def test_explicit_install_and_storage_override(self):
        result = evaluate_facts(scenario('None', existing=True, mode=True, storage='custom-rwo'))
        self.assertIs(result['r_dev_days_noobaa_install'], True)
        self.assertEqual(result['r_dev_days_noobaa_storage_class'], 'custom-rwo')

    def test_explicit_disable(self):
        self.assertIs(evaluate_facts(scenario(mode=False))['r_dev_days_noobaa_install'], False)

    def test_invalid_mode_is_rejected(self):
        expression = TASKS[0]['ansible.builtin.assert']['that'][0]
        for mode in ['auto', True, False, 'true', 'false']:
            self.assertIs(ENV.from_string('{{ ' + expression + ' }}').render(scenario(mode=mode)), True)
        self.assertIs(ENV.from_string('{{ ' + expression + ' }}').render(scenario(mode='invalid')), False)

    def test_missing_storage_class_is_rejected(self):
        guard = next(t for t in TASKS if t['name'] == 'Require usable backing storage before deploying NooBaa')
        expression = guard['ansible.builtin.assert']['that'][0]
        context = {'r_dev_days_noobaa_storage': {'resources': []}}
        self.assertIs(ENV.from_string('{{ ' + expression + ' }}').render(context), False)

    def test_unrelated_application_is_not_taken_over(self):
        context = scenario(existing=True, managed=True)
        context['r_dev_days_noobaa_app']['resources'][0]['spec']['source']['repoURL'] = 'external'
        self.assertIs(evaluate_facts(context)['r_dev_days_noobaa_install'], False)
        context[PREFIX + 'noobaa_install'] = True
        result = evaluate_facts(context)
        guard = next(t for t in TASKS if t['name'] == 'Refuse to take over another NooBaa application')
        expression = guard['ansible.builtin.assert']['that'][0]
        self.assertIs(ENV.from_string('{{ ' + expression + ' }}').render(result), False)

    def test_bootstrap_forwards_resolved_values(self):
        defaults = yaml.safe_load((ROLE / 'defaults/main.yml').read_text())
        context = defaults | scenario()
        context.update({
            'common_password': 'REPLACE_ME', 'openshift_gitops_admin_password': 'REPLACE_ME',
            'r_openshift_subdomain': 'apps.example.test',
            'r_openshift_api_server': 'https://api.example.test:6443',
            'ocp4_workload_authentication_keycloak_backstage_client_secret': 'REPLACE_ME',
            'ocp4_workload_authentication_keycloak_backstage_plugin_client_secret': 'REPLACE_ME',
            PREFIX + 'litellm_api_url': '', PREFIX + 'litellm_api_key': '',
            PREFIX + 'gitops_repo_tag': 'dev',
        })
        for _ in range(3):
            for key, value in list(context.items()):
                if isinstance(value, str) and '{{' in value:
                    context[key] = ENV.from_string(value).render(context)
        context = evaluate_facts(context)
        template = ROLE / 'templates/app-of-apps/app-of-apps-application.yaml.j2'
        rendered = yaml.safe_load(ENV.from_string(template.read_text()).render(context))
        values = rendered['spec']['source']['helm']['valuesObject']
        self.assertIs(values['noobaa']['enabled'], True)
        self.assertEqual(values['noobaa']['backingStore']['storageClass'], 'gp3-csi')
        self.assertEqual(values['gitops']['targetRevision'], 'dev')


@unittest.skipUnless(shutil.which('helm'), 'Helm is required')
class ChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(['helm', 'dependency', 'build', str(CHART), '--skip-refresh'],
                       capture_output=True, text=True, check=True)

    def parent_values(self, enabled=True, storage='gp3-csi'):
        return {
            'gitops': {'targetRevision': 'dev'},
            'cluster': {'subdomain': 'apps.example.test', 'apiServer': 'https://api.example.test:6443'},
            'vault': {'secrets': {'keycloak': {'clientId': 'backstage'}}},
            'noobaa': {'enabled': enabled, 'backingStore': {'storageClass': storage}},
        }

    def test_parent_enabled_and_disabled(self):
        docs = helm(PARENT, self.parent_values())
        app = next(d for d in docs if d['metadata']['name'] == 'noobaa')
        self.assertEqual(app['metadata']['annotations']['argocd.argoproj.io/sync-wave'], '0')
        source = app['spec']['source']
        self.assertEqual(source['path'], 'automation/gitops/cluster/noobaa')
        self.assertEqual(source['targetRevision'], 'dev')
        values = source['helm']['valuesObject']
        self.assertEqual(values['noobaa-operator']['noobaa']['subscription']['source'],
                         'redhat-operators-snapshot')
        self.assertEqual(values['noobaa-operator']['noobaa']['subscription']['channel'], 'stable-4.22')
        self.assertEqual(values['noobaa']['backingStore']['storageClass'], 'gp3-csi')
        quay = next(d for d in docs if d['metadata']['name'] == 'quay')
        self.assertEqual(quay['metadata']['annotations']['argocd.argoproj.io/sync-wave'], '1')
        self.assertFalse(any(d['metadata']['name'] == 'noobaa'
                             for d in helm(PARENT, self.parent_values(enabled=False))))

    def test_live_catalog_override(self):
        values = self.parent_values()
        values['catalogSource'] = {'enabled': False}
        app = next(d for d in helm(PARENT, values) if d['metadata']['name'] == 'noobaa')
        subscription = app['spec']['source']['helm']['valuesObject']['noobaa-operator']['noobaa']['subscription']
        self.assertEqual(subscription['source'], 'redhat-operators')

    def test_aws_and_cnv_storage_and_operator_ordering(self):
        for storage in ['gp3-csi', 'ocs-external-storagecluster-ceph-rbd', 'custom-rwo']:
            with self.subTest(storage=storage):
                docs = helm(CHART, {'noobaa': {'backingStore': {'storageClass': storage}}})
                by_kind = {d['kind']: d for d in docs}
                operator_group = by_kind['OperatorGroup']
                self.assertEqual(operator_group['spec']['targetNamespaces'], ['openshift-storage'])
                self.assertEqual(operator_group['metadata']['annotations']['argocd.argoproj.io/sync-wave'], '-3')
                self.assertEqual(by_kind['Subscription']['metadata']['annotations']['argocd.argoproj.io/sync-wave'], '-2')
                self.assertEqual(by_kind['Subscription']['spec']['channel'], 'stable-4.22')
                self.assertEqual(by_kind['NooBaa']['spec']['dbStorageClass'], storage)
                self.assertEqual(by_kind['BackingStore']['spec']['pvPool']['storageClass'], storage)
                job = by_kind['Job']
                self.assertEqual(job['metadata']['annotations']['argocd.argoproj.io/hook'], 'PostSync')
                self.assertEqual(job['spec']['activeDeadlineSeconds'], 1800)
                self.assertIn('Ready:OPTIMAL', json.dumps(job))
                for rule in by_kind['Role']['rules']:
                    self.assertEqual(rule['verbs'], ['get'])
                    self.assertTrue(rule['resourceNames'])

    def test_readiness_can_be_disabled(self):
        docs = helm(CHART, {'noobaa': {'readiness': {'enabled': False}}})
        self.assertFalse(any(d['kind'] == 'Job' for d in docs))


if __name__ == '__main__':
    unittest.main()
