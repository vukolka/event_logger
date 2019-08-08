# Event Logger
This is a package that allows handling logs of drone events
Supported events:
* Mission started
* Vehicle deployed
* Take off 
* Mission ended
* Destination reached
* Low battery
### Building package
Build as any other ROS package with catkin build system

### Running logger:
rosrun logger event_logger_app.py _rate:=10 _log_stdout:=True
set _log_stdout to False if you don't want additional console output
you can also specify _file_name, otherwise the log will be saved to default '/home/logger_client_log.txt'

### Running publisher:
`rosrun logger event_publisher_app.py _rate:=10 _log_stdout:=True`

set `_log_stdout` to False if you don't want additional console output

### Running demo
`roslaunch logger demo.launch`

It launches both nodes and saves output to default directory.
You can tune params in the launch file
