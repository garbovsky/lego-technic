from pybricks.iodevices import XboxController
from pybricks.hubs import TechnicHub
from pybricks.parameters import Button, Direction, Port, Color, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import Car
from pybricks.tools import wait, StopWatch

# Set up all devices.
steering = Motor(Port.B, Direction.CLOCKWISE)
drive = Motor(Port.A, Direction.COUNTERCLOCKWISE)
car = Car(steering, drive)
hub = TechnicHub()
watch = StopWatch()
xbox = XboxController()


# The main program starts here.
while True:
    # On status indicator.
    hub.light.on(Color.MAGENTA)

    # Control steering using the left joystick.
    car.steer(xbox.joystick_left()[0])
    # Control drive power using the trigger buttons.
    car.drive_power(xbox.triggers()[1] - xbox.triggers()[0])
    if Button.B in xbox.buttons.pressed():
        drive.brake()
        hub.light.on(Color.ORANGE)
        while Button.B in xbox.buttons.pressed():
            wait(1)

    # Makes rumble if the car is stuck.
    if abs(drive.load()) > 150:
        if watch.time() == 0:
            watch.resume()
        elif watch.time() > 300:
            hub.light.on(Color.RED)
            xbox.rumble(70, 150)
    else:
        watch.reset()
    wait(50)
