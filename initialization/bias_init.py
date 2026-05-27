import numpy as np


class BiasInitializer:

    def __init__(self):

        # ==========================================
        # Gyro Bias
        # ==========================================

        self.gyro_bias = np.zeros(3)

        # ==========================================
        # Accel Bias
        # ==========================================

        self.accel_bias = np.zeros(3)

        # ==========================================
        # Sample Buffers
        # ==========================================

        self.gyro_samples = []

        self.accel_samples = []

        # ==========================================
        # Required Samples
        # ==========================================

        self.required_samples = 500

        # ==========================================
        # Initialization Flag
        # ==========================================

        self.initialized = False

    # ==================================================
    # COLLECT IMU SAMPLES
    # ==================================================

    def collect_samples(self, imu):

        gyro = np.array([
            imu.xgyro,
            imu.ygyro,
            imu.zgyro
        ])

        accel = np.array([
            imu.xacc,
            imu.yacc,
            imu.zacc
        ])

        self.gyro_samples.append(gyro)

        self.accel_samples.append(accel)

    # ==================================================
    # COMPUTE BIASES
    # ==================================================

    def compute_biases(self):

        gyro_array = np.array(self.gyro_samples)

        accel_array = np.array(self.accel_samples)

        # ==========================================
        # Mean Gyro Bias
        # ==========================================

        self.gyro_bias = np.mean(
            gyro_array,
            axis=0
        )

        # ==========================================
        # Mean Accel Bias
        # ==========================================

        accel_mean = np.mean(
            accel_array,
            axis=0
        )

        # Remove gravity from Z-axis

        self.accel_bias = np.array([

            accel_mean[0],

            accel_mean[1],

            accel_mean[2] + 9.81
        ])

        self.initialized = True

        print("\\n==============================")
        print("IMU BIAS INITIALIZED")
        print("==============================")

        print("\\nGYRO BIAS")

        print(self.gyro_bias)

        print("\\nACCEL BIAS")

        print(self.accel_bias)