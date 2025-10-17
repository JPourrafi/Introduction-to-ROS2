<div align="justify">

## Robot Programming with ROS2 Assignment Template

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
In this first project, you will develop a Turtlesim visualizer and keyboard teleoperation interface.

The package contains two main nodes:

1. turtle_keyboard_control — Publishes velocity commands to the topic `/turtle1/cmd_vel`, allowing you to control the turtle using the keyboard.

2. turtle_target_plot — Subscribes to `/turtle1/pose` and visualizes the turtle’s position and orientation. It also spawns a randomly placed box in the Turtlesim window. When the turtle reaches the box, the box disappears and respawns at another random location.

A launch file named `turtle_target_teleop.launch.py` should start all required nodes together, including turtlesim_node. Modify the `STUDENT IMPLEMENTATION` sections and then run your launch file to verify correct functionality.

### Reuslts:
You should include figures or screen recordings of your results in the folder `./figures/rpros2_week1/`. Below is a sample markdown structure for embedding figures (e.g., `.png`, `.jpg`, or `.gif`):

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

### Challenges:
Describe any errors, issues, or challenges you encountered during this assignment.
Explain the steps or solutions you used to fix them.

**For Example:**
- Missing dependencies during build.
- Incorrect topic names or launch configuration.
- Logical errors in handling keyboard inputs or random target generation.

</div>