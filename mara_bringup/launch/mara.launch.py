import sys
import os

from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    args = sys.argv[1:]
    if "--urdf" in args:
        urdfName = args[args.index("--urdf")+1]
        if ("train" in urdfName) or ("run" in urdfName):
            urdfName = "reinforcement_learning/" + urdfName
    else:
        urdfName = 'mara_robot'

    urdf = os.path.join(get_package_share_directory('mara_description'), 'urdf/', urdfName + '.urdf')
    assert os.path.exists(urdf)

    install_dir = get_package_prefix('mara_gazebo_plugins')

    try:
        envs = {}
        for key in os.environ.__dict__["_data"]:
            key = key.decode("utf-8")
            if (key.isupper()):
                envs[key] = os.environ[key]
    except Exception as e:
        print("Error with Envs: " + str(e))
        return Non

    ld = LaunchDescription([
        Node(package='robot_state_publisher', node_executable='robot_state_publisher', output='screen', arguments=[urdf]),
        Node(package='hros_cognition_mara_components', node_executable='hros_cognition_mara_components', output='screen',
            arguments=["-motors", install_dir + "/share/hros_cognition_mara_components/link_order.yaml"])
    ])
    return ld
