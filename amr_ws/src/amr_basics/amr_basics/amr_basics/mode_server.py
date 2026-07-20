#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetMode

class ModeServer(Node):
    def __init__(self):
        super().__init__("mode_server")
        self.current_mode = "IDLE"

        self.service= self.create_service(SetMode,"set_mode",self.set_mode_callback)
        self.get_logger().info("Mode Server Ready")

    def set_mode_callback(self, request, response):
        self.current_mode = request.mode
        response.success= True
        response.message= f"Robot mode changed to {self.current_mode}"
        self.get_logger().info(f"Mode changed to {self.current_mode}")
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ModeServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()