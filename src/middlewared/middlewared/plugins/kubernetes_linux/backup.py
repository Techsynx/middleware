import os

from datetime import datetime

from middlewared.schema import Str
from middlewared.service import accepts, CallError, job, Service

from .utils import BACKUP_NAME_PREFIX


class KubernetesService(Service):

    @accepts(
        Str('backup_name', null=True, default=None)
    )
    @job(lock='chart_releases_backup')
    def backup_chart_releases(self, job, backup_name):
        self.middleware.call_sync('kubernetes.validate_k8s_setup')
        # TODO: Add validation for backup name to ensure it's not already taken
        name = BACKUP_NAME_PREFIX + (backup_name or datetime.utcnow().strftime('%F_%T'))
        if self.middleware.call_sync('zfs.snapshot.query', [['name', '=', name]]):
            raise CallError(f'{name!r} snapshot already exists')

        k8s_config = self.middleware.call_sync('kubernetes.config')
        backup_base_dir = os.path.join('/mnt', k8s_config['dataset'], 'backup')
        os.makedirs(backup_base_dir, exist_ok=True)
        backup_dir = os.path.join(backup_base_dir, name)
        os.makedirs(backup_dir)

        job.set_progress(10, 'Basic validation complete')
        chart_releases = self.middleware.call_sync('chart.release.query')
        len_chart_releases = len(chart_releases)
        for index, chart_release in enumerate(chart_releases):
            job.set_progress(
                10 + ((index + 1) / len_chart_releases) * len_chart_releases, f'Backing up {chart_release["name"]}'
            )
            chart_release_backup_path = os.path.join(backup_dir, chart_release['name'])
            os.makedirs(chart_release_backup_path)
            with open(os.path.join(chart_release_backup_path, 'namespace.yaml'), 'w') as f:
                f.write(self.middleware.call_sync('k8s.namespace.export_to_yaml', chart_release['namespace']))

            secrets_dir = os.path.join(chart_release_backup_path, 'secrets')
            os.makedirs(secrets_dir)

            secrets = self.middleware.call_sync(
                'k8s.secret.query', [
                    ['type', '=', 'helm.sh/release.v1'], ['metadata.namespace', '=', chart_release['namespace']]
                ]
            )
            for secret in sorted(secrets, key=lambda d: d['metadata']['name']):
                with open(os.path.join(secrets_dir, secret['metadata']['name']), 'w') as f:
                    f.write(self.middleware.call_sync('k8s.secret.export_to_yaml_internal', secret))

        job.set_progress(95, 'Taking snapshot of ix-applications')

        self.middleware.call_sync(
            'zfs.snapshot.create', {'dataset': k8s_config['dataset'], 'name': name, 'recursive': True}
        )

        job.set_progress(100, f'Backup {name!r} complete')
