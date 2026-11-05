cmake_minimum_required(VERSION 3.0.2)
project(hospital_delivery)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  sensor_msgs
  nav_msgs
  tf
  actionlib
  move_base_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
  scripts/delivery_task_manager.py
  DESTINATION
  ${CATKIN_PACKAGE_BIN_DESTINATION}
)
