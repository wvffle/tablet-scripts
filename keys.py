from evdev import InputDevice
import time
import os
import thread


def brightness():
    return open("/sys/class/backlight/panel/actual_brightness", "r").read()

last_brightness = 255
pwrswitch = int(int(brightness()) > 0)

def back_press():
    pass
def back_release():
    pass
def apps_press():
    pass
def apps_release():
    pass
def power_press():
    pass
def power_release():
    global pwrswitch
    global last_brightness
    print(pwrswitch, last_brightness)

    if pwrswitch == 1:
        last_brightness = brightness()
        with open("/sys/class/backlight/panel/brightness", "w") as f:
            f.write('0')
            f.close()
    else:
        with open("/sys/class/backlight/panel/brightness", "w") as f:
            f.write(last_brightness)
            f.close()

    pwrswitch = abs(pwrswitch - 1)

def home_press():
    pass
def home_release():
    os.system('xdotool key ctrl+alt+d')

def vol_up_press():
    pass
def vol_up_release():
    last_brightness = os.system('~/brightness.sh +')

def vol_down_press():
    pass
def vol_down_release():
    last_brightness = os.system('~/brightness.sh -')

touch = '/dev/input/event0'  
power = '/dev/input/event1'  
gpio  = '/dev/input/event5'  

def listen_gpio():
    device = InputDevice(gpio)
    print(device)
    for event in device.read_loop():
        if event.type == 1:
            if event.code == 102: # home
                if event.value == 1:
                    home_press()
                else:
                    home_release()
            if event.code == 115: # vol_up
                if event.value == 1:
                    vol_up_press()
                else:
                    vol_up_release()
            if event.code == 114: # vol_down
                if event.value == 1:
                    vol_down_press()
                else:
                    vol_down_release()

def listen_power():
    device = InputDevice(power)
    print(device)
    for event in device.read_loop():
        if event.type == 1:
            if event.code == 116: # power
                if event.value == 1:
                    power_press()
                else:
                    power_release()

def listen_touch():
    device = InputDevice(touch)
    print(device)
    for event in device.read_loop():
        if event.type == 1:
            if event.code == 158: # back
                if event.value == 1:
                    back_press()
                else:
                    back_release()
            if event.code == 254: # apps
                if event.value == 1:
                    apps_press()
                else:
                    apps_release()

thread.start_new_thread(listen_gpio,  ())
thread.start_new_thread(listen_touch, ())
#thread.start_new_thread(listen_power, ())
listen_power()
