from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Axis, Button, Direction, Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import XboxController


# Set up all devices.
hub = TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=5)
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
turntable = Motor(Port.D, Direction.COUNTERCLOCKWISE)
xbox = XboxController()

# Initialize variables for upper hub.
boom, arm, bucket, digger = [0] * 4

# The main program starts here.
while True:
    # On status indicator.
    hub.light.on(Color.CYAN)
    
    # Use direction pad left and right to control the turn table.
    if Button.LEFT in xbox.buttons.pressed():
        turntable.dc(-100)
    elif Button.RIGHT in xbox.buttons.pressed():
        turntable.dc(100)
    else:
        turntable.stop()

    # Use RB, LB, RT, LT for driving.
    right.run(xbox.triggers()[1] * 20)
    left.run(xbox.triggers()[0] * 20)
    if Button.RB in xbox.buttons.pressed():
        right.run(-2000)
    if Button.LB in xbox.buttons.pressed():
        left.run(-2000)

    # Boom and arm using left stick, bucket and digger with the right.
    boom = xbox.joystick_left()[1]
    arm = xbox.joystick_left()[0]
    bucket = xbox.joystick_right()[1]
    digger = xbox.joystick_right()[0]
    # Broadcast the values, so the upper hub can observe it.
    hub.ble.broadcast([boom, arm, bucket, digger])

    wait(50)
