#!/usr/bin/python3

import rclpy

from rclpy.node import Node
from std_msgs.msg import String

class simplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.pub = self.create_publisher(String, '/hello_world', 10)
        publish_frequency = 1
        self.timer = self.create_timer(1/publish_frequency, self.timer_callback)


    def timer_callback(self):
        msg = String()
        msg.data = "hello world!"
        self.pub.publish(msg)
        self.get_logger().info(f'This is my first ROS2 Publisher and I am publishing: "{msg.data}"')

def main():
    rclpy.init()

    simple_publisher = simplePublisher()
    rclpy.spin(simple_publisher)


if __name__ == "__main__":
    main()
