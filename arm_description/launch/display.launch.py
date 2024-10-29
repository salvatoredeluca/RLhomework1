from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit


 
def generate_launch_description():
    declared_arguments = []
    
    rlhomework1_path = os.path.join(
        get_package_share_directory('arm_description'))

    declared_arguments.append(
        DeclareLaunchArgument(
            "rviz_config_file",   
            default_value=PathJoinSubstitution(
                [FindPackageShare("arm_description"), "config", "rviz", "arm.rviz"]
            ),
            description="RViz config file (absolute path) to use when launching rviz.",
        )
    )



    xacro_arm = os.path.join(rlhomework1_path, "urdf", "arm.urdf.xacro")
    

    robot_description_arm_xacro = {"robot_description": Command(['xacro ', xacro_arm])}


   

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )
   
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description_arm_xacro,
                    {"use_sim_time": True},
            ],
        remappings=[('/robot_description', '/robot_description')]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="log",
        arguments=["-d", LaunchConfiguration("rviz_config_file")],
    )

    

    
    
    nodes_to_start = [
        robot_state_publisher_node,
        joint_state_publisher_node,
        # joint_state_broadcaster,
        rviz_node
        
    ]


    return LaunchDescription( declared_arguments+nodes_to_start) 



 