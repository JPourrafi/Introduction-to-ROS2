#!/usr/bin/python3

import sys
import rclpy

from rclpy.node import Node
# from example_interfaces.srv import AddTwoInts
from my_interfaces.srv import AddTwoInts

class simpleServiceClient(Node):
    def __init__(self):
        super().__init__('simple_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_int')
        while not self.cli.wait_for_service(timeout_sec=0.1):
            self.get_logger().info('service not available! still waiting ...')
        self.req = AddTwoInts.Request()
    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)

def main():
    rclpy.init()

    simple_client = simpleServiceClient()
    future = simple_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    rclpy.spin_until_future_complete(simple_client, future)

    response = future.result()
    simple_client.get_logger().info(
        f'results of add_two_int: for {int(sys.argv[1])} + {int(sys.argv[2])} = {response.sum}'
    )

    simple_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()