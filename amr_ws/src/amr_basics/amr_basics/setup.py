from setuptools import find_packages, setup

package_name = 'amr_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amirtha-varshiniy',
    maintainer_email='amirthavarshiniyma@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'distance_publisher = amr_basics.distance_publisher:main',
            'distance_watcher = amr_basics.distance_watcher:main',
            'battery_publisher = amr_basics.battery_publisher:main',
            'battery_watcher = amr_basics.battery_watcher:main',
            'robot_sim = amr_basics.robot_sim:main',
            'controller = amr_basics.controller:main',
            'mode_server = amr_basics.mode_server:main',
            'mode_client = amr_basics.mode_client:main',
            'dock_server = amr_basics.dock_server:main',
            'dock_client = amr_basics.dock_client:main',
            'nav_server = amr_basics.nav_server:main',
            'nav_client = amr_basics.nav_client:main',
        ],
    },
)
