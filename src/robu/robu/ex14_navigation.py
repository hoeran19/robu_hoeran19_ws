#CLI - commands
#1. action list: ros2 action list
#2. action info: ros2 action info <action_name> -t
#3. interface list: ros2 interface show <interface_name>
#4. action call: ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "{pose: {header: {frame_id: 'map'}, pose: {position: {x: 3.75, y: 1.0, z: 0.01}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}}"

from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped

import rclpy
from rclpy.duration import Duration
from rclpy.node import Node

from std_msgs.msg import String

class Nav2Pose(Node):
    def __init__(self):
        super().__init__('nav2_pose')
        self.pose_subscriber = self.create_subscription(String, '/nav2_pose', self.nav2_pose_callback, 10)

        self.declare_parameters('', [('pose_initial', [0.0, 0.0, 0.0, 1.0]), 
                                     ('pose_a', [3.75, 1.0, 0.0, 1.0])])

        self.navigator = BasicNavigator()

        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = self.get_parameter('pose_initial').value[0]
        initial_pose.pose.position.y = self.get_parameter('pose_initial').value[1]
        initial_pose.pose.orientation.z = self.get_parameter('pose_initial').value[2]
        initial_pose.pose.orientation.w = self.get_parameter('pose_initial').value[3]

        self.navigator.setInitialPose(initial_pose)
        self.navigator.waitUntilNav2Active()


        pose_a = PoseStamped()
        pose_a.header.frame_id = 'map'
        pose_a.header.stamp = self.navigator.get_clock().now().to_msg()
        pose_a.pose.position.x = self.get_parameter('pose_a').value[0]
        pose_a.pose.position.y = self.get_parameter('pose_a').value[1]
        pose_a.pose.orientation.z = self.get_parameter('pose_a').value[2]
        pose_a.pose.orientation.w = self.get_parameter('pose_a').value[3]

        self.goal_poses = [initial_pose, pose_a]

        self.goal_poses_index = -1
        self.timer = self.create_timer(1.0, self.timer_callback)


    def nav2_pose_callback(self, msg):
        if msg.data == "Halle A":
            self.navigator.goToPose(self.goal_poses[1])
            self.goal_poses_index = 1
        elif msg.data == "Home":
            self.navigator.goToPose(self.goal_poses[0])
            self.goal_poses_index = 0

    def timer_callback(self):
        if self.goal_poses_index >= 0:
            pose = self.goal_poses[self.goal_poses_index]
            if not self.navigator.isTaskComplete():
                feedback = self.navigator.getFeedback()
                print(Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
            else:
                result = self.navigator.getResult()
                if result == TaskResult.SUCCEEDED:
                    print("Task succeeded")
                elif result == TaskResult.FAILED:
                    print("Task failed")
                elif result == TaskResult.CANCELED:
                    print("Task canceled")
                self.goal_poses_index = -1


def main(args=None):
    rclpy.init(args=args)
    nav2pose_node = Nav2Pose()
    rclpy.spin(nav2pose_node)
    nav2pose_node.destroy_node()
    rclpy.shutdown()


if __name__=='__main__':
    main()