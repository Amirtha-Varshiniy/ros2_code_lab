#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import BatteryStatus


class BatteryWatcherNode(Node):
    def __init__(self):
        super().__init__("battery_watcher")
        self.publisher_= self.create_subscription(BatteryStatus, "/battery_status", self.callback, 10)

    def callback(self, msg):
        if msg.percentage <20:
            self.get_logger().warn(f'Battery is low: {msg.percentage}%')



def main (args=None):
    rclpy.init(args=args)
    node = BatteryWatcherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()