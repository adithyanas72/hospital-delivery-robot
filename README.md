# Smart Hospital Delivery Robot (ROS Noetic + Gazebo)

Simulation of a differential-drive delivery robot with a 2-D LiDAR in a Gazebo hospital world (one corridor, four rooms). The package covers robot modelling, SLAM mapping with gmapping, AMCL localization, move_base navigation and a Python delivery task manager.

**Status:** simulation, mapping and the navigation stack run. Reliable autonomous entry into every room is still being tuned.

## Requirements

- Ubuntu 20.04, ROS Noetic, Gazebo
- `ros-noetic-gmapping`, `ros-noetic-amcl`, `ros-noetic-map-server`, `ros-noetic-navigation`, `ros-noetic-teleop-twist-keyboard`

## Package structure

```
hospital_delivery/
├── CMakeLists.txt
├── package.xml
├── scripts/    delivery_task_manager.py, lidar_monitor.py
├── launch/     gazebo.launch, slam.launch, navigation.launch
├── urdf/       hospital_robot.urdf
├── worlds/     hospital.world
├── maps/       hospital_map.pgm, hospital_map.yaml
├── config/     costmap and planner parameters
└── rviz/       hospital_navigation.rviz
```

## Build

```
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## Run

Mapping (SLAM):

```
roslaunch hospital_delivery gazebo.launch navigation:=false
roslaunch hospital_delivery slam.launch
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
rosrun map_server map_saver -f ~/catkin_ws/src/hospital_delivery/maps/hospital_map
```

Navigation (Gazebo, AMCL, move_base and RViz together):

```
roslaunch hospital_delivery gazebo.launch
rosrun hospital_delivery delivery_task_manager.py
```

The robot spawns at the world origin (the pharmacy), so the map frame matches the Gazebo world frame.

## Scripts

- `delivery_task_manager.py` sends a navigation goal to move_base through `actionlib` and reports whether it was reached.
- `lidar_monitor.py` prints the minimum obstacle distance from `/scan`.
