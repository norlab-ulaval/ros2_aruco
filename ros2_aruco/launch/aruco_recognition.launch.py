import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    aruco_params_5x5 = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'config',
        'aruco_parameters_5x5.yaml'
        )
    
    aruco_params_4x4 = os.path.join(
        get_package_share_directory('ros2_aruco'),
        'config',
        'aruco_parameters_4x4.yaml'
        )

    aruco_node_obstacle = Node(
        package='ros2_aruco',
        namespace='obstacle',
        executable='aruco_node',
        parameters=[aruco_params_4x4]
    )

    aruco_node_street = Node(
        package='ros2_aruco',
        namespace='street',
        executable='aruco_node',
        parameters=[aruco_params_5x5]
    )

    return LaunchDescription([
        aruco_node_obstacle,
        aruco_node_street
    ])
