import rclpy

from rclpy.node import Node

class MinimalParameter(Node):
    def __init__(self):
        super().__init__('MinimalParameter')