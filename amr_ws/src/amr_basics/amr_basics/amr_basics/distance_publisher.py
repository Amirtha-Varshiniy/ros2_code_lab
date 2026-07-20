#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DistancePublisherNode(Node):
    def __init__(self):
        super().__init__("distance_publisher")
        self.publisher_= self.create_publisher(Float32, "/sensor/front_distance", 10)
        self.timer= self.create_timer(0.5, self.publisher_distance)

    def publisher_distance(self):
        msg=Float32()
        msg.data = random.uniform(0.05,4.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f"front distance = {msg.data:.2f} m")

def main (args=None):
    rclpy.init(args=args)
    node = DistancePublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()