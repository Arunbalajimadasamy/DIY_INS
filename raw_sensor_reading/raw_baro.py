from pymavlink.dialects.v20 import common as mavlink2


class RawBaro:

    def __init__(self):

        self.press_abs = 0.0

        self.press_diff = 0.0

        self.temperature = 0.0


def request_baro_stream(master):

    interval_us = int(1e6 / 50)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_SCALED_PRESSURE,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_baro(msg, baro):

    baro.press_abs = msg.press_abs

    baro.press_diff = msg.press_diff

    baro.temperature = msg.temperature / 100.0