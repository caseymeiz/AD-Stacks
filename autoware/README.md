# Point a to point b

1. Go over instructions in ./carla

2. Run CarLA

```shell
sudo docker run -p 2000-2002:2000-2002 --privileged --gpus all --net=host -e DISPLAY=$DISPLAY carlasim/carla:0.9.10.1 /bin/bash ./CarlaUE4.sh
```
3. follow carla-autoware instructions
```shell
cd carla-autoware && ./build.sh
./run.sh
roslaunch carla_autoware_agent carla_autoware_agent.launch town:=Town01
```