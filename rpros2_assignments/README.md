<div align="justify">

# Robot Programming with ROS2 Assignments

## Setup:
create a ros2 workspace

copy the ros2 package `rpros2_week1_assignment` to your workspace

modify the areas noted by `STUDENT IMPLEMENTATION`

build your package


<div align="justify">

# Robot Programming with ROS2 Assignment Template

## 🧭 Setup

Follow the steps below to set up your environment and complete the assignment.

### 1. Create a ROS2 Workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

### 2. Copy the Assignment Package

Copy the provided ROS2 package (e.g. `rpros2_week1_assignment`) into your workspace:

```bash
cd ~/ros2_ws/src
cp -r /path/to/rpros2_week1_assignment .
```

### 3. Build the Assignment Package

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### 4. Modify the Student Sections

Open the package source files and complete the parts marked with:

```python
# >>>>>>>>>>> STUDENT IMPLEMENTATION >>>>>>>>>>>
#
# TODO: Write your code in here.
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```

Make sure your code runs correctly and meets the assignment objectives.


## Table of Contents
- [Week 1](#week-1-turtlesim-target-visualization-and-teleop)


## `Week 1` Turtlesim Target Visualization and Teleop 

### Assignment Task: 
your first projects involves developing a turtlesim visualizer and keyboard teleoperation. there exist two nodes called turtle_keyboard_control and turtle_target_plot respectively handle publishing velocity commands to `/turtle1/cmd_vel` and subscribing to `/turtle1/pose`. the first node controls the robot using keyboard and the second node runs a plotter that shows turtle's pose and orientation with a randomly plced box that whenever the robot reaches there, it disapears and teleports to another random place. there is also a lauch file `turtle_target_teleop.launch.py` that should spawn all the nodes together plus the `turtlesim_node`. modify the `STUDENT IMPLEMENTATION` share the result of your code.

### Reuslts:
here is a sample markdown code for sharing Figures. it could be .png, .jpg, or .gif files. save your figures in the folder `./figures/rpros2_week1/`

<div align="center">

| <img src=".\figures\week1\turtle_target_teleop_node_example.gif" alt="turtle_target_teleop_node_example" width="1024"/> |
|:--:| 
| <b>Fig. 1.</b> Turtlesim Target Visualization and Teleop Node Example |

</div>

<div align="center">
  
| <img src=".\figures\week1\turtle_target_teleop_launch_example.gif" alt="turtle_target_teleop_launch_example" width="1024"/> |
|:--:| 
| <b>Fig. 2.</b> Turtlesim Target Visualization and Teleop Launch Example |

</div>

### challenges:
express any errors or  challenges during homework and the solutions that helped you fix the problem.

</div>