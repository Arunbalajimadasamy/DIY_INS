from pymavlink.dialects.v20 import common as mavlink2


class RawIMU:

    def __init__(self):

        self.xacc = 0.0
        self.yacc = 0.0
        self.zacc = 0.0

        self.xgyro = 0.0
        self.ygyro = 0.0
        self.zgyro = 0.0

        self.xmag = 0.0
        self.ymag = 0.0
        self.zmag = 0.0


def request_imu_stream(master):

    interval_us = int(1e6 / 100)

    master.mav.command_long_send(

        master.target_system,
        master.target_component,

        mavlink2.MAV_CMD_SET_MESSAGE_INTERVAL,

        0,

        mavlink2.MAVLINK_MSG_ID_HIGHRES_IMU,

        interval_us,

        0,
        0,
        0,
        0,
        0
    )


def update_imu(msg, imu):

    imu.xacc = msg.xacc
    imu.yacc = msg.yacc
    imu.zacc = msg.zacc

    imu.xgyro = msg.xgyro
    imu.ygyro = msg.ygyro
    imu.zgyro = msg.zgyro

    imu.xmag = msg.xmag
    imu.ymag = msg.ymag
    imu.zmag = msg.zmag