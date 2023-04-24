import subprocess


start_carla_cmd = "sudo docker run -p 2000-2002:2000-2002 --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.10.1 /bin/bash ./CarlaUE4.sh"
