#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.parameter import Parameter

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")

        self.declare_parameter("direction",-1.0)
        self.declare_parameter("turtle_velocity",1.0)

        self.direction_ = self.get_parameter("direction").value
        self.velocity_ = self.get_parameter("turtle_velocity").value

        self.cmd_vel_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.pose_sub_ = self.create_subscription(Pose,"/turtle1/pose",self.callback_pose,10)

    def callback_pose(self, pose):
        cmd = Twist()
        cmd.linear.x = self.velocity_
        cmd.angular.z = self.direction_
        self.cmd_vel_pub_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node=TurtleControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ =="__main__":
    main()
