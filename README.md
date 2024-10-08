# ROS 2 Simple Publisher-Subscriber Project

This is a basic ROS 2 project that demonstrates the implementation of a simple publisher and subscriber using Python. The publisher sends messages at regular intervals, and the subscriber receives and processes these messages. This project is a great starting point for understanding the basics of ROS 2 communication between nodes.

## Project Structure

- **Publisher Node**: Sends out messages at regular intervals.
- **Subscriber Node**: Listens for incoming messages and processes them.

## Getting Started

Follow these steps to set up and run the project on your machine.

### Prerequisites

Before you begin, ensure you have the following installed:

- **ROS 2 Humble**: Follow the [official installation guide](https://docs.ros.org/en/humble/Installation.html) for your operating system.
- **Python**: This project is implemented in Python.

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/karank4/ROS2_project00.git
   cd ROS2_project00
   ```

2. **Set Up ROS 2 Workspace:**
   - If you don’t already have a ROS 2 workspace, create one:

     ```bash
     mkdir -p ~/ros2_ws/src
     cd ~/ros2_ws/src
     ```

   - Move the project folder into your workspace:

     ```bash
     mv ~/ROS2_project00 ~/ros2_ws/src/
     ```

   - Navigate to your workspace directory:

     ```bash
     cd ~/ros2_ws/
     ```

   - Build the workspace using `colcon`:

     ```bash
     colcon build
     ```

3. **Source the Setup Files:**
   - Source the ROS 2 setup file to ensure your environment is set up correctly:

     ```bash
     source /opt/ros/humble/setup.bash
     ```

   - Also, source the setup file for your workspace:

     ```bash
     source ~/ros2_ws/install/setup.bash
     ```

### Running the Project

1. **Launch the ROS 2 Publisher Node:**
   - Open a new terminal window, source the ROS 2 environment, and run the publisher node:

     ```bash
     source ~/ros2_ws/install/setup.bash
     ros2 run my_package publisher
     ```

2. **Launch the ROS 2 Subscriber Node:**
   - Open another terminal window, source the ROS 2 environment, and run the subscriber node:

     ```bash
     source ~/ros2_ws/install/setup.bash
     ros2 run my_package subscriber
     ```

### Project in Action

Once both nodes are running, you should see the publisher sending messages and the subscriber receiving and processing them. This setup simulates a simple communication process between two ROS 2 nodes.

### Customization

- **Message Content**: You can modify the message content in the publisher node by editing the source code located in `~/ros2_ws/src/ROS2_project00/publisher.py`.
- **Publishing Frequency**: Adjust the publishing rate by modifying the timer settings in the publisher node's code.

### Troubleshooting

- Ensure you have sourced the setup files before running any ROS 2 commands.
- If you encounter build issues, try cleaning the workspace with:

  ```bash
  colcon build --packages-select <package_name>
  ```

---
