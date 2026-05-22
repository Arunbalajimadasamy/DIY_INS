from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink2

PORT = "COM3"
BAUD = 115200


def connect_mavlink():

    master = mavutil.mavlink_connection(
        PORT,
        baud=BAUD
    )

    master.wait_heartbeat()

    print("Connected to Cube Orange PX4")

    return master


def set_message_interval(master, message_id, frequency_hz):

    interval_us = int(1e6 / frequency_hz)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        message_id,
        interval_us,

        0,
        0,
        0,
        0,
        0
    )
