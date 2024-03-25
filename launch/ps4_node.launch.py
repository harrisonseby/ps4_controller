from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            executable='joy_node',
            output='screen'
        ),
        
        Node(
            package='ps4_controller',
            executable='ps4_node',
            output='screen'
        )
    ])

if __name__ == '__main__':
    generate_launch_description()
