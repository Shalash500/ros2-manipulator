from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'py_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "Launch"), glob(os.path.join("launch", "*launch.[pxy][yma]*")))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shalash',
    maintainer_email='shalash@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "simple_publisher = py_examples.simple_publisher:main",
            "simple_subscriber = py_examples.simple_subscriber:main",
            "simple_parameter = py_examples.simple_parameters:main",
            "simple_service_server = py_examples.simple_service_server:main",
            "simple_service_client = py_examples.simple_service_client:main",
            "simple_action_server = py_examples.simple_action_server:main",
            "simple_action_client = py_examples.simple_action_client:main",
            "simple_moveit_interface = py_examples.simple_moveit_interface:main",
            "simple_lifecycle_node = py_examples.simple_lifecycle_node:main",
        ],
    },
)
