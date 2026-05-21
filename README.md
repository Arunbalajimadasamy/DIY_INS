# DIY_INS
Custom Inertial Navigation System (INS) for fixed-wing UAVs using Cube Orange Plus IMU data for GPS-denied environments.

This project is about building my own Inertial Navigation System (INS) using the inbuilt sensors of the Cube Orange Plus for GPS-denied environments.

GPS data will be used only for initial position estimation and periodic drift correction. The main objective is to develop an INS capable of independently estimating the UAV’s global position and navigation states.

Let’s build our own INS 

Note:
INS is an algorithm that predicts the global position and provides navigation data to the main guidance and control system.

The INS I’m developing is specifically designed for fixed-wing UAVs 

Dependencies:
• PX4 running on Cube Orange Plus
• OBC (Onboard Computer): Raspberry Pi or Jetson. As of now, I’m using a laptop directly connected to the Cube via a USB cable for development and testing.
• PyMAVLink as the middleware for communication between the flight controller and the INS algorithm

From raw IMU data to autonomous navigation — teaching a UAV to know where it is, even when GPS disappears
