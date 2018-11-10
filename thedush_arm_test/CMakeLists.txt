cmake_minimum_required(VERSION 2.8.3)
project(thedush_arm_test)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  interactive_markers
  moveit_core
  moveit_ros_perception
  moveit_ros_planning_interface
  pluginlib
  roscpp
  std_msgs
)

## System dependencies are found with CMake's conventions
find_package(Boost REQUIRED COMPONENTS system)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES seven_dof_arm_test
#  CATKIN_DEPENDS cmake_modules interactive_markers moveit_core moveit_ros_perception moveit_ros_planning_interface pluginlib roscpp std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


## Declare a cpp executable
add_executable(test_random_node src/test_random.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(test_random_node thedush_arm_test_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(test_random_node
   ${catkin_LIBRARIES}
 )


include_directories(
  ${catkin_INCLUDE_DIRS}
)


## Declare a cpp executable
add_executable(test_custom_node src/test_custom.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(test_custom_node thedush_arm_test_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(test_custom_node
   ${catkin_LIBRARIES}
 )



