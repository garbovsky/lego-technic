from pybricks.hubs import TechnicHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

hub = TechnicHub()

# Linear actuator autostop testing.
finished = False;

# Move the gripper up and down.
async def check_load():
    global finished
    while not finished:
        await wait(1000)
        print(f'load: {first.load()} speed: {first.speed()}')
        if first.speed() == 0:
            first.stop()
            finished = True

# Drive forward, turn move gripper at the same time, and drive backward.
async def main():
    await multitask(first.run_angle(1440,360*20), check_load())

# Runs the main program from start to finish.
run_task(main())