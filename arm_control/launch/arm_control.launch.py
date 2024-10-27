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
from launch.actions import TimerAction


 
def generate_launch_description():
    # declared_arguments = []

    # rl_21_10_2024_exercise_path = os.path.join(
    #     get_package_share_directory('ros2_sensors_and_actuators'))

    # declared_arguments.append(
    #     DeclareLaunchArgument(
    #         "rviz_config_file", 
    #         default_value=PathJoinSubstitution(
    #             [FindPackageShare("ros2_sensors_and_actuators"), "config", "rviz", "iiwa.rviz"]
    #         ),
    #         description="RViz config file (absolute path) to use when launching rviz.",
    #     )
    # )
  

    # xacro_iiwa = os.path.join(rl_21_10_2024_exercise_path, "urdf", "iiwa.urdf.xacro")


    # robot_description_iiwa_xacro = {"robot_description": Command(['xacro ', xacro_iiwa, ' joint_a3_pos:=2.0', ' joint_a4_pos:=0.2'])}

    # joint_state_publisher_node = Node(
    #     package="joint_state_publisher_gui",
    #     executable="joint_state_publisher_gui",
    # )
   
    # robot_state_publisher_node = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     output="both",
    #     parameters=[robot_description_iiwa_xacro,
    #                 {"use_sim_time": True},
    #         ],
    # )
    
    # rviz_node = Node(
    #     package="rviz2",
    #     executable="rviz2",
    #     name="rviz2",
    #     output="log",
    #     arguments=["-d", LaunchConfiguration("rviz_config_file")],
    # )


    # declared_arguments.append(DeclareLaunchArgument('gz_args', default_value='-r -v 1 empty.sdf',
    #                           description='Arguments for gz_sim'),)
    
    # gazebo_ignition = IncludeLaunchDescription(
    #         PythonLaunchDescriptionSource(
    #             [PathJoinSubstitution([FindPackageShare('ros_gz_sim'),
    #                                 'launch',
    #                                 'gz_sim.launch.py'])]),
    #         launch_arguments={'gz_args': LaunchConfiguration('gz_args')}.items()
    # )

    # position = [0.0, 0.0, 0.65]

    # gz_spawn_entity = Node(
    #     package='ros_gz_sim',
    #     executable='create',
    #     output='screen',
    #     arguments=['-topic', 'robot_description',
    #                '-name', 'iiwa',
    #                '-allow_renaming', 'true',],
    # )
 
    # ign = [gazebo_ignition, gz_spawn_entity]

     

    joint_state_broadcaster =Node(
            package="controller_manager",
            executable="spawner",
            arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
            
            
        )



    position_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["position_controller", "--controller-manager", "/controller_manager"],  
    ) 

    #Launch the ros2 controllers after the model spawns in Gazebo 
    # delay_joint_traj_controller = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=gz_spawn_entity,
    #         on_exit=[position_controller],
    #     )
    # )

    # delay_joint_state_broadcaster = (
    #     RegisterEventHandler(
    #         event_handler=OnProcessExit(
    #             target_action=gz_spawn_entity,
    #             on_exit=[joint_state_broadcaster],
    #         )
    #     )
    # )

    # bridge_camera = Node(
    #     package='ros_ign_bridge',
    #     executable='parameter_bridge',
    #     arguments=[
    #         '/camera@sensor_msgs/msg/Image@gz.msgs.Image',
    #         '/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo',
    #         '--ros-args', 
    #         '-r', '/camera:=/videocamera',
    #     ],
    #     output='screen'
    # )
    
    nodes_to_start = [
        joint_state_broadcaster,
        position_controller,
       
        
    ]

    return LaunchDescription(nodes_to_start) 