# ROS 2 Code Lab 🤖

A collection of ROS 2 projects, experiments, and implementations exploring robotics concepts, communication interfaces, custom messages, services, actions, launch systems, and robot simulation.

This repository documents my hands-on journey with ROS 2 through practical implementations and mini-projects, covering the core concepts required for developing robotic applications.

---

## Technologies

- ROS 2 Jazzy Jalisco
- Python
- Gazebo
- RViz2
- Colcon
- Ubuntu 24.04

---

## Repository Structure

```text
amr_ws
└── src
    ├── amr_basics
    ├── demo_pkg
    ├── my_robot_bringup
    ├── my_robot_interfaces
    └── turtle_controller
```

---

## Packages

### amr_basics

Implements fundamental ROS 2 communication concepts, including:

- Publishers
- Subscribers
- Services
- Service Clients
- Actions
- Action Clients
- Parameters
- Robot simulation
- Distance monitoring
- Battery monitoring
- Docking service
- Navigation action

---

### demo_pkg

Practice package containing introductory ROS 2 examples.

Includes:

- Publisher examples
- Subscriber examples
- Service examples
- Action examples
- Counter applications

---

### my_robot_interfaces

Custom ROS 2 interfaces used throughout the projects.

#### Messages

- BatteryStatus.msg
- HardwareStatus.msg

#### Services

- FindDock.srv
- ResetCounter.srv
- SetMode.srv

#### Actions

- CountUntil.action
- NavigateToGoal.action

---

### my_robot_bringup

Launch and configuration package.

Contains:

- Launch files
- Parameter configuration
- Multi-node launch examples

---

### turtle_controller

ROS 2 package for controlling the TurtleSim robot using Python.

---

## Concepts Covered

- ROS 2 Nodes
- Topics
- Publishers & Subscribers
- Services
- Clients
- Parameters
- Launch Files
- Custom Messages
- Custom Services
- Custom Actions
- TurtleSim
- Robot Simulation
- Package Creation
- Workspace Management

---

## Building the Workspace

Navigate to the workspace:

```bash
cd ~/amr_ws
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## Running Packages

Example:

```bash
ros2 run <package_name> <executable_name>
```

Launch example:

```bash
ros2 launch my_robot_bringup number_app.launch.xml
```

---

## Future Work

- Mobile robot development
- Gazebo simulations
- Navigation2 (Nav2)
- SLAM
- Sensor integration
- ROS 2 Control
- Autonomous navigation

---

## Author

**Amirtha Varshiniy**

EEE Undergraduate ⚡ | Future Microelectronics Engineer

Interested in Robotics, Embedded Systems, VLSI, and Edge AI.

---

## License

This repository is intended for learning, educational, and research purposes.
