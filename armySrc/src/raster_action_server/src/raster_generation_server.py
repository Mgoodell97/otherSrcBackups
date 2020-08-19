#! /usr/bin/env python

import rospy
import actionlib
import raster_action_server.msg

class RasterAction(object):
    #messages that hold the feedback/result
    _feedback = raster_action_server.msg.rasterFeedback()
    _result = raster_action_server.msg.rasterResult();

    def __init__(self, name):
        self._action_name = name
        self._action_server = actionlib.SimpleActionServer(self._action_name,
            raster_action_server.msg.rasterAction, execute_cb = self.execute_cb,
            auto_start = False)
        self._action_server.start()
        rospy.loginfo("Server started...")

    def execute_cb(self, goal):
        # do raster things in here
        rospy.loginfo('Got a request for a %d X %d box', goal.width, goal.height)
        if self._action_server.is_preempt_requested():
            self._action_server.set_preempted()
            return
        self._result.foo = 42
        self._result.bar = 23
        self._action_server.set_succeeded(self._result)

if __name__ == '__main__':
    rospy.init_node('raster_generator')
    server = RasterAction(rospy.get_name())
    rospy.spin()
