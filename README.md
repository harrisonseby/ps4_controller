# ps4_controller_for_ros2
This ros2 package takes input from the ps4 controller and converts it into /cmd_vel allowing us to control differential drive robot such as turtlebot3. The launch file starts the joy package which takes input from the ps4 controller as sensor_msgs/Joy. Followed by the python script that converts the input into geometry_msgs/Twist

##Instrctions

Clone the repository in your src folder in your workspace.
```bash
git clone ...
```
Make sure all the dependencies are installed using rosdep
```bash
# From the root directory of the workspace. This will install everything mentioned in package.xml
rosde
