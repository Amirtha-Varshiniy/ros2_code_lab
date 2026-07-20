#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import FindDock

class DockServer(Node):
    def __init__(self):
        super().__init__("dock_server")
        self.docks = [(0.0, 0.0),(5.0, 5.0),(-3.0, 4.0)]
        self.service= self.create_service(FindDock,"find_dock",self.find_dock_callback)
        self.get_logger().info("Dock Server Ready")

    def find_dock_callback(self, request, response):
        x = request.x
        y = request.y
        if abs(x) > 20 or abs(y) > 20:
            response.dock_x = 0.0
            response.dock_y= 0.0
            response.distance= 0.0
            response.reachable = False
            return response

        nearest = None
        minimum_distance = float("inf")

        for dock in self.docks:
            distance = math.dist((x, y), dock)
            if distance < minimum_distance:
                minimum_distance= distance
                nearest= dock

        response.dock_x= nearest[0]
        response.dock_y= nearest[1]
        response.distance= minimum_distance
        response.reachable= True
        return response




def main(args=None):
    rclpy.init(args=args)
    node = DockServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()