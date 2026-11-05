#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction
from move_base_msgs.msg import MoveBaseGoal
from actionlib_msgs.msg import GoalStatus


class HospitalDeliveryRobot:

    def __init__(self):
        rospy.init_node('hospital_delivery_manager')

        self.client = actionlib.SimpleActionClient(
            '/move_base',
            MoveBaseAction
        )

        rospy.loginfo("Waiting for move_base server...")
        self.client.wait_for_server()
        rospy.loginfo("Navigation server connected.")

    def send_goal(self, x, y, yaw=0.0):
        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y

        goal.target_pose.pose.orientation.z = 0.0
        goal.target_pose.pose.orientation.w = 1.0

        rospy.loginfo(
            "Sending delivery goal: X = %.2f, Y = %.2f",
            x, y
        )

        self.client.send_goal(goal)
        self.client.wait_for_result()

        result = self.client.get_state()

        if result == GoalStatus.SUCCEEDED:
            rospy.loginfo(
                "Delivery location reached successfully."
            )
            return True
        else:
            rospy.logwarn(
                "Navigation failed or goal was not reached."
            )
            return False


if __name__ == '__main__':
    try:
        robot = HospitalDeliveryRobot()

        # Example delivery location
        robot.send_goal(2.0, 2.0)

        rospy.loginfo("Hospital delivery task completed.")

    except rospy.ROSInterruptException:
        rospy.loginfo(
            "Hospital delivery node interrupted."
        )
