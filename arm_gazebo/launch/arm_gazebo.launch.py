from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    path1 = get_package_share_directory('arm_gazebo')
    
    path2 = get_package_share_directory('arm_control')

    path1_c=os.path.join(path1, "launch","arm_world.launch.py")
    path2_c=os.path.join(path2, "launch", "arm_control.launch.py")

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(path1_c),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(path2_c),
        ),
    ])
