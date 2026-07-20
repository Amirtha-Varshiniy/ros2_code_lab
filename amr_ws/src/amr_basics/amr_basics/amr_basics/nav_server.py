#!/usr/bin/env python3

import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse

from my_robot_interfaces.action import NavigateToGoal


class NavigationServer(Node):

    def __init__(self):
        super().__init__("nav_server")

        self.action_server = ActionServer(
            self,
            NavigateToGoal,
            "navigate_to_goal",
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        self.get_logger().info("Navigation Action Server Started")

    def goal_callback(self, goal_request):
        self.get_logger().info(
            f"Received Goal: ({goal_request.x}, {goal_request.y})"
        )
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info("Goal canceled")
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):

        current_x = 0.0
        current_y = 0.0

        goal_x = goal_handle.request.x
        goal_y = goal_handle.request.y

        step_size = 0.1

        start_time = time.time()

        feedback = NavigateToGoal.Feedback()
        result = NavigateToGoal.Result()

        while rclpy.ok():

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()

                result.success = False
                result.time_taken = time.time() - start_time

                self.get_logger().info("Goal canceled")

                return result

            dx = goal_x - current_x
            dy = goal_y - current_y

            distance = math.sqrt(dx * dx + dy * dy)

            feedback.distance_remaining = distance
            goal_handle.publish_feedback(feedback)

            self.get_logger().info(
                f"Distance Remaining: {distance:.2f}"
            )

            if distance < 0.1:
                goal_handle.succeed()

                result.success = True
                result.time_taken = time.time() - start_time

                self.get_logger().info("Goal Reached!")

                return result

            current_x += step_size * dx / distance
            current_y += step_size * dy / distance

            time.sleep(0.5)


def main(args=None):

    rclpy.init(args=args)

    node = NavigationServer()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
    