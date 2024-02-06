import rclpy

from rclpy.node import Node


class TestParameter(Node):
    def __init__(self):
        super().__init__("TestParam")


        self.declare_parameters(
            namespace='',
            parameters=[
                ('hoehe', 0.7),
                ('breite', 0.21),
                ('laenge', 5.0)
            ])
        
        self.timer = self.create_timer(2.0, self.callback)


    def callback(self):

        hoehe = self.get_parameter("hoehe").value
        breite = self.get_parameter("breite").value
        laenge = self.get_parameter("laenge").value

        print("\nhoehe: ", hoehe)
        print("breite: ", breite)
        print("laenge: ", laenge)


def main():
    rclpy.init()

    node = TestParameter()

    rclpy.spin(node)