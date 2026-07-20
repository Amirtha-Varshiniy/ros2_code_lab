#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import FindDock


class DockClient(Node):

    def __init__(self):
        super().__init__("dock_client")

        self.client = self.create_client(
            FindDock,
            "find_dock"
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service...")

    def send_request(self, x, y):

        request = FindDock.Request()

        request.x = x
        request.y = y

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(self, future)

        return future.result()


def main(args=None):

    rclpy.init(args=args)

    node = DockClient()

    test_points = [
        (1.0, 1.0),
        (-10.0, 3.0),
        (50.0, 50.0)
    ]

    for x, y in test_points:

        response = node.send_request(x, y)

        print("----------------------------")
        print(f"Robot Position : ({x}, {y})")
        print(f"Reachable      : {response.reachable}")
        print(f"Nearest Dock   : ({response.dock_x}, {response.dock_y})")
        print(f"Distance       : {response.distance:.2f}")

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()