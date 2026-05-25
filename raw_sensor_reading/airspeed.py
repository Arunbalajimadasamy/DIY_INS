from pymavlink.dialects.v20 import common as mavlink2


class Airspeed:

    def __init__(self):

        self.airspeed = 0.0

        self.groundspeed = 0.0

        self.throttle = 0

        self.climb = 0.0


def request_airspeed_stream(master):

    interval_us = int(1e6 / 20)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_VFR_HUD,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_airspeed(msg, airspeed):

    airspeed.airspeed = msg.airspeed

    airspeed.groundspeed = msg.groundspeed

    airspeed.throttle = msg.throttle

    airspeed.climb = msg.climb