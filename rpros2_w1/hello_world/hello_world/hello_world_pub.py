#!/usr/bin/python3

import rclpy

from rclpy.node import Node
from std_msgs.msg import String

class simplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.my_publisher = self.create_publisher(String, 'hello_world_msgs', 10)
        self.freq = 10
        self.timer = self.create_timer(1/self.freq, self.timer_callback)
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World ROS2! This is my first ROS Publisher'
        self.my_publisher.publish(msg)

def main(args=None):
    rclpy.init()

    simple_publisher = simplePublisher()

    rclpy.spin(simple_publisher)

    simple_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()