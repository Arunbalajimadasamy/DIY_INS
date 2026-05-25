from pymavlink.dialects.v20 import common as mavlink2


class NavGPS:

    def __init__(self):

        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0

        self.relative_alt = 0.0

        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0

        self.heading = 0.0


def request_nav_gps_stream(master):

    interval_us = int(1e6 / 20)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_GLOBAL_POSITION_INT,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_nav_gps(msg, gps):

    gps.lat = msg.lat / 1e7
    gps.lon = msg.lon / 1e7

    gps.alt = msg.alt / 1000.0

    gps.relative_alt = msg.relative_alt / 1000.0

    gps.vx = msg.vx / 100.0
    gps.vy = msg.vy / 100.0
    gps.vz = msg.vz / 100.0

    gps.heading = msg.hdg / 100.0