# stopped_container_check
This checks if we have any stopped docker containers. Exits with a critical message if any of the containers are stopped and returns a 0 exit code if everything is running. 

Requirements:

1. Python3

2. Docker module for python3:

pip3 install docker --user
