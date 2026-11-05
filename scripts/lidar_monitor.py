#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan


class LidarMonitor:

    def __init__(self):
        rospy.init_node('lidar_monitor')

        rospy.Subscriber(
            '/scan',
            LaserScan,
            self.scan_callback
        )

        rospy.spin()

    def scan_callback(self, data):
        ranges = data.ranges

        # Remove invalid measurements
        valid_ranges = [
            r for r in ranges
            if r > data.range_min
            and r < data.range_max
        ]

        if len(valid_ranges) == 0:
            return

        minimum_distance = min(valid_ranges)

        rospy.loginfo(
            "Minimum obstacle distance: %.2f m",
            minimum_distance
        )


if __name__ == '__main__':
    try:
        LidarMonitor()
    except rospy.ROSInterruptException:
        pass
