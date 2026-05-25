from pymavlink.dialects.v20 import common as mavlink2


class RawGPS:

    def __init__(self):

        self.fix_type = 0

        self.satellites = 0

        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0

        self.hdop = 0.0
        self.vdop = 0.0

        self.ground_speed = 0.0

        self.course_over_ground = 0.0


def request_raw_gps_stream(master):

    interval_us = int(1e6 / 10)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_GPS_RAW_INT,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_raw_gps(msg, gps):

    gps.fix_type = msg.fix_type

    gps.satellites = msg.satellites_visible

    gps.lat = msg.lat / 1e7
    gps.lon = msg.lon / 1e7

    gps.alt = msg.alt / 1000.0

    gps.hdop = msg.eph / 100.0
    gps.vdop = msg.epv / 100.0

    gps.ground_speed = msg.vel / 100.0

    gps.course_over_ground = msg.cog / 100.0