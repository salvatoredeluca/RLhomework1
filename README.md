## 🤖 Robotics Lab Homework1

This repository contains the three ROS packages required for the homework 1 of the course. In the following the instructions to run the packages correctly.

## 📦 Build and Source

Once you cloned the repository in your ROS2 workspace, build the packages.

```bash
colcon build
```
then source 
```bash
source install/setup.bash
```

## 🖼️ Visualize the manipulator in RViz

```bash
ros2 launch arm_description display.launch.py
```


## 🔥 Visualize the manipulator in Gazebo with the controllers loaded
```bash
ros2 launch arm_gazebo arm_gazebo.launch.py
```

## 📷 Visualize the image seen by the camera

On another terminal run the command
```bash
rqt
```

then open the plugin rqt_image_view

## 🤙 Run the ROS publisher and subscriber node

In another terminal run
```bash
ros2 run arm_control arm_node
```








