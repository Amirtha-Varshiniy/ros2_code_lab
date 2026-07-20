#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class RobotSimNode(Node):
    def __init__(self):
        super().__init__("robot_sim")
        self.current_vel = 0.0
        self.desired_vel = 0.0

        self.subscription= self.create_subscription(Float32, "/cmd_vel",self.cmd_callback,10)

        self.publisher = self.create_publisher(Float32,"/current_vel",10)

        self.timer = self.create_timer(0.2, self.timer_callback)

    def cmd_callback(self, msg):
        self.desired_vel = msg.data

    def timer_callback(self):
        self.current_vel += 0.5 * (self.desired_vel - self.current_vel)
        msg = Float32()
        msg.data =self.current_vel
        self.publisher.publish(msg)
        self.get_logger().info(f"Current Velocity: {self.current_vel:.2f}")



def main(args=None):
    rclpy.init(args=args)
    node =RobotSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
