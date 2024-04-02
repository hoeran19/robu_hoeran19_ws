import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch_ros.actions import Node

def generate_launch_description():
   
    return LaunchDescription([
    
        SetEnvironmentVariable('ROS_DOMAIN_ID', '7'),

        Node(
           package='robu',
            executable='fibonacci_server',
            output='screen',
            name='fibonacci_server'
        ),
        
        Node(
            package='robu',
            executable='fibonacci_client',
            output='screen',
            name='fibonacci_client'
        ),
        
        ExecuteProcess(
            cmd=['sleep', '5'],
            output='screen',
            name='sleep',
            on_exit=[ExecuteProcess(
            cmd=['ros2', 'action', 'send_goal', '/fibonacci', 'robu_interfaces/action/Fibonacci', '{order: 5}'],
            output='screen',
            name='call_fibonacci_action'
        )]
        ),
        
    ])

