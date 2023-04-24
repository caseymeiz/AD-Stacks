set x+



docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)

docker run -p 2000-2002:2000-2002 --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.10.1 /bin/bash ./CarlaUE4.sh > /dev/null 2>&1 &
#docker run -p 2000-2002:2000-2002 --privileged --gpus all --net=host  carlasim/carla:0.9.10.1 /bin/bash ./CarlaUE4.sh > /dev/null 2>&1 &


cd ~/git/carla-autoware && ./build.sh
#cd ~/git/carla-autoware

./run.sh

# [0.019, 0.007, 0.005, 0.018, 0.011, 0.006, 0.011, 0.022, 0.013, 0.017, 0.011]