import rclpy

from rclpy.node import Node


class TestParameterGet(Node):
    def __init__(self):
        super().__init__("TestParamGet")

        self.declare_parameters(
            namespace='',
            parameters=[
                ('hoehe', 0.7),
                ('breite', 0.21),
                ('laenge', 5.0)
            ])

        self.timer = self.create_timer(0.1, self.callback)


    def callback(self):
        hoehe = self.get_parameter('hoehe')
        print("hoehe: ", hoehe)


def main():
    rclpy.init()

    node = TestParameterGet()

    rclpy.spin(node)