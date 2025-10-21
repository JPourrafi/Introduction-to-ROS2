#!/usr/bin/python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class simpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/hello_world',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('This is my first ROS2 Subscriber and I heared: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    simple_subscriber = simpleSubscriber()
    rclpy.spin(simple_subscriber)


if __name__ == '__main__':
    main()
