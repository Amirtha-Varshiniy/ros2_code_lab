#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DistanceWatcherNode(Node):
    def __init__(self):
        super().__init__("distance_watcher")
        self.subscriber_ = self.create_subscription(Float32,"/sensor/front_distance", self.distance_callback,10)

    def distance_callback(self,msg):
        if msg.data < 0.3:
            self.get_logger().warn(f"Obstacle at {msg.data:.2f} m")
        else:
            self.get_logger().info(f"Clear: {msg.data:.2f} m")

def main(args=None):
    rclpy.init(args=args)
    node= DistanceWatcherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()

