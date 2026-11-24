# NooBaa object storage — GPTEINFRA-18445

Ports the Platform Engineering workshop's OCP 5 NooBaa fix
([PR #6](https://github.com/rhpds/platform-engineering-workshop/pull/6),
source commit `f6846954cf347107c0a089c55bf2b0c01d763bac`) into this repository.
Quay managed object storage, TPA and Module 3 need the NooBaa/OBC APIs.
AWS EBS storage classes alone do not provide an object-storage service.

## Bootstrap configuration

The `ocp4_workload_dev_days_rdshw_cluster_bootstrap` role resolves these settings
before creating the root Argo CD application:

| Variable suffix (`ocp4_workload_dev_days_rdshw_`) | Default | Behavior |
| --- | --- | --- |
| `noobaa_install` | `auto` | Reuse an existing NooBaa system; install if absent. A system already managed by this role stays enabled on reruns. Explicit `true`/`false` is supported. |
| `noobaa_namespace` | `openshift-storage` | Namespace for the standard workshop NooBaa service. |
| `noobaa_name` | `noobaa` | NooBaa system and child application name. |
| `noobaa_storage_class` | empty | Resolve to `gp3-csi` on AWS, otherwise `ocs-external-storagecluster-ceph-rbd`. Set an explicit override for a different RWO storage class. |
| `noobaa_channel` | `stable-4.22` | MCG channel matching the configured OCP 5/4.22 operator snapshot. |

The role validates the selected storage class before installation. Both the
NooBaa database volume and backing-store volumes use that class. Existing CNV
NooBaa systems are not adopted into this chart or deleted on role reruns.
An explicit install refuses to overwrite an application owned by another source.
An existing standalone recovery application must be migrated explicitly rather
than silently overwritten.

Workshop consumers currently expect the standard `openshift-storage` namespace
and its `openshift-storage.noobaa.io` object-bucket storage class. Changing the
namespace requires corresponding changes to those consumers.

For fresh AWS orders using this fix, select **dev for both** the Ansible
collection version and `ocp4_workload_dev_days_rdshw_gitops_repo_tag`. The
collection revision and Argo source revision are independent; selecting one does
not automatically select the other. This change does not alter the existing
`main` defaults or catalog items in AgnosticV.

## GitOps behavior

The new child application is conditional on `noobaa.enabled`. Chart-only
app-of-apps users must explicitly enable it when their cluster has no NooBaa:

```yaml
noobaa:
  enabled: true
  backingStore:
    storageClass: gp3-csi
```

Keep it disabled when the CNV pool already supplies NooBaa. The Ansible bootstrap
performs this detection automatically.

The child uses the same GitOps repository/revision and operator catalog selection
as the parent. Installation order is OperatorGroup (`-3`), Subscription (`-2`),
then NooBaa and BackingStore (`-1`). A read-only, namespace-scoped PostSync job
waits up to 30 minutes for NooBaa `Ready` and backing storage `Ready/OPTIMAL`.
The NooBaa application is in root wave `0`, ahead of Quay and TPA in wave `1`.
Dependent controllers also retry while storage is becoming available.

Student signing, approval, promotion and intentionally broken troubleshooting
exercises are unchanged. Secured tenant apps do not need to be green before
students complete those exercises.

## Validation

```bash
# Prerequisites: Helm, Python with PyYAML, Jinja2 and ansible-core.
python -m unittest discover -s automation/tests -p 'test_noobaa.py' -v
helm dependency build automation/gitops/cluster/noobaa --skip-refresh
helm lint automation/gitops/cluster/noobaa
```

The tests cover AWS/CNV rendering, existing-system reuse, role reruns, explicit
installation/storage overrides, ownership protection, catalog selection, sync
ordering, readiness RBAC and Ansible-to-Helm value forwarding. Generated Helm
dependency archives are not committed.

These checks are not a substitute for fresh-order validation. Test a new AWS
order and a CNV order before promoting the fix beyond `dev`.
