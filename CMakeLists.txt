cmake_minimum_required(VERSION 2.8.3)
project(logger)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  geometry_msgs
  std_msgs
  message_generation
)

macro(convert_absolut_path file_list)
  foreach(src_file ${${file_list}})
    get_filename_component(src_file_path "${src_file}" NAME)
    list(REMOVE_ITEM ${file_list} "${src_file}")
    list(APPEND ${file_list} "${src_file_path}")
  endforeach()
endmacro()

file(GLOB_RECURSE MSG_FILES RELATIVE "${PROJECT_SOURCE_DIR}/msg" *.msg)

convert_absolut_path(${MSG_FILES})

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   ${MSG_FILES}
)

 generate_messages(
   DEPENDENCIES
         sensor_msgs
         std_msgs
         geometry_msgs
 )
catkin_package(
#  INCLUDE_DIRS include
  CATKIN_DEPENDS
        roscpp
        rospy
        sensor_msgs
        std_msgs
        message_generation
        message_runtime
        geometry_msgs
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
