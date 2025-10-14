#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class simpleSubscriber(Node):
    def __init__(self):
        super().__init__('simple_subscriber')
        self.subscriber = self.create_subscription(String, 'hello_world_msgs', self.listener_callback, 10)

    def listener_callback(self, msgs):
        self.get_logger().info(f'I am the first Subscriber and I have heard: {msgs.data}')

def main(args=None):
    rclpy.init()

    simple_subscriber = simpleSubscriber()

    rclpy.spin(simple_subscriber)
    
    simple_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()