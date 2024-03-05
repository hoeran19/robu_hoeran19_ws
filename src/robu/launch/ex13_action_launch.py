import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
   
    #fibonacci_server = os.path.join(
    #    os.getcwd(), '/home/robu/work/robu_hoeran19_ws/src/robu/robu/ex12_fibonacci_server.py')
    #fibonacci_client = os.path.join(
    #    os.getcwd(), '/home/robu/work/robu_hoeran19_ws/src/robu/robu/ex12_fibonacci_client.py')

    # Erstelle eine Liste von Actions für die Launch-Datei
    return LaunchDescription([
    
#        Node(
#           package='robu',
#            executable='fibonacci_server',
#            output='screen',
#            name='fibonacci_server'
#        ),
#        # Starte den Fibonacci Action-Client als ROS 2 Node
#        Node(
#            package='robu',
#            executable='fibonacci_client',
#            output='screen',
#            name='fibonacci_client'
#        ),
        
        # Warte 5 Sekunden, bevor die CLI-Anweisung ausgeführt wird
        SetEnvironmentVariable(name='ROS_DOMAIN_ID', value='7'),

        ExecuteProcess(
            cmd=['sleep', '5'],
            output='screen',
            name='sleep'
        ),
        # Führe die CLI-Anweisung zum Aufruf der Fibonacci-Action aus
        ExecuteProcess(
            cmd=['ros2', 'action', 'send_goal', '/fibonacci', 'robu_interfaces/action/Fibonacci', '{order: 5}'],
            output='screen',
            name='call_fibonacci_action'
        )
    ])

