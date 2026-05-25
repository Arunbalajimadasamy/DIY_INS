from pymavlink.dialects.v20 import common as mavlink2
import math


class Attitude:

    def __init__(self):

        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

        self.rollspeed = 0.0
        self.pitchspeed = 0.0
        self.yawspeed = 0.0


def request_attitude_stream(master):

    interval_us = int(1e6 / 100)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_ATTITUDE,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_attitude(msg, attitude):

    attitude.roll = math.degrees(msg.roll)

    attitude.pitch = math.degrees(msg.pitch)

    attitude.yaw = math.degrees(msg.yaw)

    attitude.rollspeed = msg.rollspeed

    attitude.pitchspeed = msg.pitchspeed

    attitude.yawspeed = msg.yawspeed