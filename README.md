# Pepper-Play-Motion-Capture

# Prerequisites
Make sure your ROS environment is set up to run either an emulated Pepper or connect to a real Pepper robot. See https://github.com/rosielab/ROStoNAO-Bridge-Docker-Setup if you do not have your ROS environment configured. 

You need a Pepper robot to run the motion capture code on. This can be an [emulated Pepper](https://github.com/emily-zhang021/QiBullet-ROS-Setup) from QiBullet or a [physical Pepper](https://github.com/rosielab/ROStoNAO-Bridge-Docker-Setup) robot. 

# How to Run

## 1. Set up your Catkin Workspace
Clone the repository and place the repository folders into your ~/catkin_ws/src folder.

Build the project with catkin_make. 
```
catkin_make
```

## 2. Run a roscore
If you don't already have one running, run:
```
roscore
```

## 3. Run the input_bvh Node
After running this, you will be prompted to enter the path of the bvh file you want to play on Pepper.
```
rosrun input_bvh bvh_path_publisher
```
## 4. Run the pepper_play_bvh Node
In a new terminal, run the pepper_play_bvh node. This will listen for messages published to the bvh_path_topic. 
```
rosrun pepper_play_bvh playmotion.py
```
## 5. Switch terminals and Enter your File Path 
In the terminal you ran the input_bvh node, enter the path of your bvh file you wish to execute on Pepper. This will publish to the bvh_path_topic. Your motion should now execute on Pepper.

# Notes
bvh files have inconsistent joint names and the order of rotation for the joints can differ from file to file or even joint to joint. The code currently does not account for this, and follows the mapping convention that is most commonly seen in the [CMU Mocap Database](http://mocap.cs.cmu.edu/). 

If you find that Pepper is not executing any motions or only certain joints:
1. Double check the bvh file's joint names. You may need to create a new joint mapping dictionary if it does not follow the convention of the existing dictionaries in playmotion.py.
2. Check the order of rotation for the joints and see if they correspond to the order of rotation in the following code block in playmotion.py:
```
        # Transform bvh file in the rotation order of "Z X Y" to Pepper
        rx, ry, rz = euler_from_matrix(rot_mat, axes='rzxy')
```

# Resources

As Pepper is missing a few degrees of freedom and generally has limited motion, the motion executed on Pepper may not be exactly the same as the one from the bvh file which is based on human subjects. 

The implementation of the joint mapping from bvh to Pepper joints is adapted from [pepper-gesture-mapping](https://github.com/SamuelCahyawijaya/pepper-gesture-mapping) and the math is explained in [transforms3d](https://github.com/matthew-brett/transforms3d/blob/main/transforms3d/euler.py#L237). 

This implementation does not address this issue, but from further research, there are 2 additional possible ways of calculating the joint angles from a bvh file onto a Nao robot. 

Combination of inverse kinematics and forward kinematics 
https://github.com/TomKingsfordUoA/NaoGestures

Machine learning
https://www.diva-portal.org/smash/get/diva2:1524432/FULLTEXT01.pdf
