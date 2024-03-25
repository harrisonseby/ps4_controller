# ps4_controller_for_ros2
This ros2 package takes input from the ps4 controller and converts it into /cmd_vel allowing us to control differential drive robot such as turtlebot3. The launch file starts the joy package which takes input from the ps4 controller as sensor_msgs/Joy. Followed by the python script that converts the input into geometry_msgs/Twist

## Prerequisites
Before installing the package make sure your controller is connected using wired or wireless method. 
You can check whether the controls are recognized by the system by using the jstest-gtk package.
### Install jstest-gtk
Run update command to update package repositories and get latest package information.
```bash
sudo apt-get update -y
```
Run the install command with -y flag to quickly install the packages and dependencies. 
```bash
sudo apt-get install -y jstest-gtk
```

## Instrctions to install and run ps4_controller
### Clone 
Clone the repository in your src folder in your workspace.
```bash
git clone https://github.com/harrisonseby/ps4_controller.git
```
### Dependencies
Make sure all the dependencies are installed using rosdep
```bash
# From the root directory of the workspace. This will install everything mentioned in package.xml
rosdep install --from-paths src --ignore-src -r -y
```
### Build
```bash
colcon build --packages-select ps4_controller
```
### Run
```bash
ros2 run ps4_controller ps4_node
```
### ROS echo
The published topic is `/cmd_vel` and the output can be viewed using `ros2 topic echo /cmd_vel`
