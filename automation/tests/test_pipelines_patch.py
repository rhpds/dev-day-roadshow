"""Offline RBAC regression tests for the Pipelines PostSync hook.

Run: python3 -m unittest discover -s automation/tests -p 'test_pipelines_patch.py' -v
"""
from pathlib import Path
import subprocess
import unittest

import yaml


TEMPLATE = (Path(__file__).resolve().parents[1] /
            'gitops/cluster/openshift-pipelines/templates/tektonconfig-patch-job.yaml')


class PipelinesPatchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This template's only Helm expression is the release namespace.
        rendered = TEMPLATE.read_text().replace('{{ .Release.Namespace }}', 'openshift-pipelines')
        cls.docs = [doc for doc in yaml.safe_load_all(rendered) if doc]

    def resource(self, kind, name):
        return next(doc for doc in self.docs
                    if doc['kind'] == kind and doc['metadata']['name'] == name)

    def test_results_permissions_are_namespaced_and_minimal(self):
        role = self.resource('Role', 'tektonconfig-patch-results')
        self.assertEqual(role['rules'], [
            {'apiGroups': [''], 'resources': ['configmaps'],
             'resourceNames': ['tekton-results-api-config'], 'verbs': ['get', 'update']},
            {'apiGroups': [''], 'resources': ['configmaps'],
             'resourceNames': ['chains-config'], 'verbs': ['get']},
            {'apiGroups': ['apps'], 'resources': ['deployments'],
             'resourceNames': ['tekton-chains-controller'], 'verbs': ['get']},
            {'apiGroups': [''], 'resources': ['pods'], 'verbs': ['list', 'delete']},
        ])
        cluster_role = self.resource('ClusterRole', 'tektonconfig-patch')
        self.assertFalse(any('configmaps' in rule['resources'] or 'pods' in rule['resources']
                             for rule in cluster_role['rules']))

    def test_results_role_is_bound_to_the_hook_service_account(self):
        binding = self.resource('RoleBinding', 'tektonconfig-patch-results')
        job = self.resource('Job', 'tektonconfig-patch')
        self.assertEqual(binding['roleRef'], {
            'apiGroup': 'rbac.authorization.k8s.io', 'kind': 'Role',
            'name': 'tektonconfig-patch-results'})
        self.assertEqual(binding['subjects'], [{
            'kind': 'ServiceAccount',
            'name': job['spec']['template']['spec']['serviceAccountName'],
            'namespace': 'openshift-pipelines'}])
        for kind in ['Role', 'RoleBinding']:
            annotations = self.resource(kind, 'tektonconfig-patch-results')['metadata']['annotations']
            self.assertEqual(annotations['argocd.argoproj.io/hook'], 'PostSync')
            self.assertLessEqual(int(annotations['argocd.argoproj.io/sync-wave']),
                                 int(job['metadata']['annotations']['argocd.argoproj.io/sync-wave']))

    def test_chains_audience_is_owned_by_tektonconfig_not_installerset(self):
        job = self.resource('Job', 'tektonconfig-patch')
        shell = job['spec']['template']['spec']['containers'][0]['command'][-1]
        self.assertIn('"options": {', shell)
        self.assertIn('"deployments": {', shell)
        self.assertIn('"tekton-chains-controller": {', shell)
        self.assertIn('"audience": "trusted-artifact-signer"', shell)
        self.assertIn('[ "${AUDIENCE}" = "trusted-artifact-signer" ]', shell)
        self.assertIn('[ "${ENABLED}" = "true" ]', shell)
        self.assertNotIn('oc get tektoninstallerset', shell)
        cluster_role = self.resource('ClusterRole', 'tektonconfig-patch')
        self.assertFalse(any('tektoninstallersets' in rule['resources']
                             for rule in cluster_role['rules']))

    def test_hook_shell_syntax(self):
        job = self.resource('Job', 'tektonconfig-patch')
        shell = job['spec']['template']['spec']['containers'][0]['command'][-1]
        subprocess.run(['bash', '-n'], input=shell, text=True, check=True)


if __name__ == '__main__':
    unittest.main()
