from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

# Launch description specifically for the NTRIP base station on the rooftop
def generate_launch_description():
  
    # Node for the NTRIP client
    ntrip_client_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([
        PathJoinSubstitution([
          FindPackageShare('ntrip_client'), 'ntrip_client_launch.py'
        ])
      ]),
      launch_arguments={
        'host': "caster.emlid.com",
        'port': "2101",
        'mountpoint': "MP9395",
        'username': "u98842",
        'password': "373rhf"
        }.items()
    )      

    # combine all the launch actions
    ld.add_action(ntrip_client_node)
    
    # finally return the completed launch sequence
    return ld
  
