#!/usr/bin/python3

import rclpy

from rclpy.node import Node
# from example_interfaces.srv import AddTwoInts
from my_interfaces.srv import AddTwoInts

class simpleService(Node):
    def __init__(self):
        super().__init__('simple_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_int', self.add_two_int_callback)

    def add_two_int_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'I have got two inputs: {request.a} + {request.b}')

        return response

def main():
    rclpy.init()

    simple_service = simpleService()

    rclpy.spin(simple_service)
    rclpy.shutdown()


if __name__ == '__main__':
    main()