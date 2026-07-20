#!/usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetMode

class ModeClient(Node):
    def __init__(self):
        super().__init__("mode_client")
        self.client= self.create_client(SetMode,"set_mode")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self, mode):
        request= SetMode.Request()
        request.mode= mode
        future= self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main(args=None):
    rclpy.init(args=args)
    node= ModeClient()
    mode= "AUTO"
    if len(sys.argv) > 1:
        mode = sys.argv[1]

    response= node.send_request(mode)
    print("Success :", response.success)
    print("Message :", response.message)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()