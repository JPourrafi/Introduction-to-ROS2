import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'rpros2_week1'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='erfan',
    maintainer_email='erf.riazati@gmail.com',
    description='Robot Programming with ROS2 Course | Week 1 | ROS Publishers/Subscribers, Packages, and Launch Files',
    license='MIT',
    entry_points={
        'console_scripts': [
            'simple_publisher = rpros2_week1.simple_publisher:main',
            'simple_subscriber = rpros2_week1.simple_subscriber:main'
        ],
    },
)
