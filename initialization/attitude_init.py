import numpy as np

from navigation.quaternion import (
    euler_to_quaternion
)


class AttitudeInitializer:

    def __init__(self):

        # ==========================================
        # Euler Angles
        # ==========================================

        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

        # ==========================================
        # Quaternion
        # ==========================================

        self.q = np.array([
            1.0,
            0.0,
            0.0,
            0.0
        ])

        # ==========================================
        # Initialization Flag
        # ==========================================

        self.initialized = False

    # ==================================================
    # INITIALIZE FROM PX4 ATTITUDE
    # ==================================================

    def initialize_attitude(self, attitude):

        self.roll = attitude.roll

        self.pitch = attitude.pitch

        self.yaw = attitude.yaw

        self.q = euler_to_quaternion(

            self.roll,

            self.pitch,

            self.yaw
        )

        self.initialized = True

        print("\\n==============================")
        print("ATTITUDE INITIALIZED")
        print("==============================")

        print(f"ROLL  : {self.roll:.2f}")

        print(f"PITCH : {self.pitch:.2f}")

        print(f"YAW   : {self.yaw:.2f}")

        print("\\nINITIAL QUATERNION")

        print(self.q)
