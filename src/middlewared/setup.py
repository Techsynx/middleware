import os
from setuptools import find_packages, setup

# Define constants for package data directories
ASSETS_DIRS = ['alembic', 'assets', 'etc_files', 'migration']
PACKAGE_DATA_DIRS = {
    'middlewared.apidocs': ['templates/websocket/*', 'templates/*.*'],
    'middlewared': [
        'alembic.ini',
        *get_assets('alembic'),
        *get_assets('assets'),
        *get_assets('etc_files'),
        *get_assets('migration'),
    ],
}

def get_assets(name):
    """
    Recursively get directories and files from middlewared/{name}
    """
    base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'middlewared')
    result = []
    for root, dirs, files in os.walk(os.path.join(base_path, name)):
        result.extend([
            f'{os.path.relpath(root, base_path)}/*',
            *[os.path.join(os.path.relpath(root, base_path), file) for file in files if file == '.gitkeep']
        ])
    return result

def main():
    setup(
        name='middlewared',
        description='TrueNAS Middleware Daemon',
        packages=find_packages(),
        package_data=PACKAGE_DATA_DIRS,
        include_package_data=True,
        license='BSD',
        platforms='any',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
        ],
        entry_points={
            'console_scripts': [
                'configure_fips = middlewared.scripts.configure_fips:main',
                'setup_cgroups = middlewared.scripts.setup_cgroups:main',
                'middlewared = middlewared.main:main',
                'midgdb = middlewared.scripts.gdb:main',
                'sedhelper = middlewared.scripts.sedhelper:main',
                'wait_to_hang_and_dump_core = middlewared.scripts.wait_to_hang_and_dump_core:main',
                'wait_on_disks = middlewared.scripts.wait_on_disks:main',
                'start_vendor_service = middlewared.scripts.vendor_service:main',
            ],
        },
    )

if __name__ == '__main__':
    main()
