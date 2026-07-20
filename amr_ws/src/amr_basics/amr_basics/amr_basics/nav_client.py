#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from my_robot_interfaces.action import NavigateToGoal

class NavigationClient(Node):
    def __init__(self):
        super().__init__("nav_client")
        self.action_client = ActionClient(self,NavigateToGoal,"navigate_to_goal")

    def send_goal(self):
        goal_msg = NavigateToGoal.Goal()
        goal_msg.x = 3.0
        goal_msg.y = 4.0
        self.action_client.wait_for_server()
        self.get_logger().info("Sending Goal (3.0, 4.0)")
        self.send_goal_future = self.action_client.send_goal_async(goal_msg,feedback_callback=self.feedback_callback)
        self.send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal Rejected")
            return
        

        self.get_logger().info("Goal Accepted")
        self.result_future = goal_handle.get_result_async()
        self.result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f"Distance Remaining: {feedback.distance_remaining:.2f}")

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info("--------------------------")
        self.get_logger().info(f"Success     : {result.success}")
        self.get_logger().info(f"Time Taken  : {result.time_taken:.2f} s")
        self.get_logger().info("--------------------------")

        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)
    node = NavigationClient()
    node.send_goal()
    rclpy.spin(node)


if __name__ == "__main__":
    main()