from setuptools import find_packages, setup

package_name = 'demo_pkg'

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
    maintainer_email='amirtha-varshiniy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "test_node = demo_pkg.demo_node:main",
            "number_publisher = demo_pkg.no_publisher:main",
            "number_counter = demo_pkg.number_counter:main",
            "reset_counter_client = demo_pkg.reset_counter_client:main",
            "count_until_server = demo_pkg.count_until_server_minimal:main",
            "count_until_client = demo_pkg.count_until_client_minimal:main"
        ],
    },
)
