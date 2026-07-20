#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class ControllerNode(Node):

    def __init__(self):
        super().__init__("controller")
        self.target_vel = 1.5

        self.publisher= self.create_publisher( Float32,"/cmd_vel",10)

        self.subscription = self.create_subscription(Float32,"/current_vel",self.current_vel_callback,10)

    def current_vel_callback(self, msg):
        error = self.target_vel - msg.data
        cmd = Float32()
        if abs(error) > 0.01:
            cmd.data = self.target_vel
        else:
            cmd.data =self.target_vel

        self.publisher.publish(cmd)
        self.get_logger().info(f"Current: {msg.data:.2f}  Target: {self.target_vel:.2f}  Error: {error:.2f}")

def main(args=None):
    rclpy.init(args=args)
    node = ControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()