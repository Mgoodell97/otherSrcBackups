#! /usr/bin/env python
from __future__ import print_function
import rospy


# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the fibonacci action, including the
# goal message and the result message.
import raster_action_server.msg

def raster_client():
    client = actionlib.SimpleActionClient('raster_generator', raster_action_server.msg.rasterAction)
    print("waiting for server")
    client.wait_for_server()
    print("server connected")
    goal = raster_action_server.msg.rasterGoal(width=123, height=839)
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(10))
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('raster_client')
        result = raster_client()
        print("result: ", result.foo)
    except rospy.ROSInterruptException:
        print("programm stopped")
