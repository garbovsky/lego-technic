from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
hub = TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=0, observe_channels=[5])
boom = Motor(Port.A, Direction.COUNTERCLOCKWISE)
arm = Motor(Port.B, Direction.COUNTERCLOCKWISE)
bucket = Motor(Port.C, Direction.COUNTERCLOCKWISE)
digger = Motor(Port.D, Direction.CLOCKWISE)

# Initialize variables.
boom_pwr, arm_pwr, bucket_pwr, digger_pwr = [0] * 4

# Converting speed to power.
def calc_power(speed):
    return (100 if speed > 90 else 75 if speed > 60 else 50 if speed > 30 else 
            -100 if speed < -90 else -75 if speed < -60 else -50 if speed < -30 else 0)

# Using the function.
def control_motor(motor, speed):
    if abs(speed) > 30:
        motor.dc(calc_power(speed))
        # Using a color indicator for motor power.
        hub.light.on(Color.ORANGE if abs(speed) > 90 else (Color.YELLOW if abs(speed) > 30 else Color.CYAN))
    else:
        motor.stop()

while True:
    # On status indicator.
    hub.light.on(Color.CYAN)

    # Get data sent from the lower hub.
    boom_pwr, arm_pwr, bucket_pwr, digger_pwr = hub.ble.observe(5) or [0] * 4
    
    control_motor(boom, boom_pwr)
    control_motor(arm, arm_pwr)
    control_motor(bucket, bucket_pwr)
    control_motor(digger, digger_pwr)

    wait(50)
