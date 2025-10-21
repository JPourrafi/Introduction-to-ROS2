from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rpros2_week1',
            executable='simple_publisher',
            name='simple_publisher'
        ),
        Node(
            package='rpros2_week1',
            executable='simple_subscriber',
            name='simple_subscriber'
        )
    ])
