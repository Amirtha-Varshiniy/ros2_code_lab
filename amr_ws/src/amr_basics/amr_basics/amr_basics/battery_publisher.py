#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import BatteryStatus


class BatteryPublisherNode(Node):
    def __init__(self):
        super().__init__("battery_publisher")
        self.publisher_= self.create_publisher(BatteryStatus, "/battery_status", 10)
        self.timer= self.create_timer(1.0, self.publish_status)
        self.percentage =100

    def publish_status(self):
        msg=BatteryStatus()
        msg.voltage = 12.0
        msg.percentage = self.percentage
        msg.is_charging =False
        self.publisher_.publish(msg)

        self.get_logger().info(f"Battery = {self.percentage}%")
        self.percentage -=1
        if self.percentage <=0:
            self.percentage =100

def main (args=None):
    rclpy.init(args=args)
    node = BatteryPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()