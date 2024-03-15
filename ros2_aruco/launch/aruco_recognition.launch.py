import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    aruco_params = os.path.join(
        get_package_share_directory("ros2_aruco"), "config", "aruco_parameters.yaml"
    )

    aruco_node = Node(
        package="ros2_aruco",
        executable="aruco_node",
        namespace="/camera/color",
        parameters=[aruco_params],
    )

    ld.add_action(aruco_node)
    return ld
