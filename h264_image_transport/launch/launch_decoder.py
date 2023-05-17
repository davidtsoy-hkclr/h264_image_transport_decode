from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_transport',
            executable='republish',
            name='h264_decoder',
            arguments=['h264', 'raw'],
            remappings=[
                ('out', 'image_uncompressed')
            ]
        )
    ])
