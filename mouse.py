from evdev import InputDevice
import time
from pymouse import PyMouse
from threading import Timer
import subprocess


def rightclick():
    subprocess.check_call(['xinput', '--disable', 'touchscreen'])
    m.press(endx, endy, 2)
    m.release(endx, endy, 2)
    subprocess.check_call(['xinput', '--enable', 'touchscreen'])

dev = InputDevice('/dev/input/event0')  
m = PyMouse()
print(dev)

fingersmax = 1
fingers = 1

for event in dev.read_loop():
    if event.type == 3 and event.code == 57 and event.value > 0: 
        timestart = time.time()

    # Have to implement scroll function, or use this
    # https://github.com/SavinaRoja/PyUserInput

    if event.type == 3 and event.code == 53:
        if 'startx' not in vars():
            startx = event.value
        elif fingers == 2:
            if 'lastx' not in vars():
                lastx = event.value
            # m.scroll(horizontal=lastx-event.value)
        lastx = event.value
    if event.type == 3 and event.code == 54: 
        if 'starty' not in vars():
            starty = event.value
        elif fingers == 2:
            if 'lasty' not in vars():
                lasty = event.value
            # m.scroll(vertical=lasty-event.value)
        lasty = event.value

    if event.type == 3 and event.code == 57 and event.value == -1: 
        deltatime = time.time() - timestart
        endx, endy = m.position()

        try:
            deltax = abs(startx - endx)
            deltay = abs(starty - endy)

            fingers -= 1
            if fingers == 0:
                del startx
                del starty
                fingersmax = 1
                fingers = 1

            if fingersmax == 1 and deltatime > 0.2 and deltax < 10 and deltay < 10:
                rightclick()
        except Exception:
            print('exception', fingers, fingersmax)
            fingers = 1
            fingersmax = 1

    if event.type == 3 and event.code == 47: 
        fingersmax += event.value
        fingers += event.value
