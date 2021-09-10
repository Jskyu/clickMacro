from platform import version
import keyboard
import pyautogui as auto
import time


VERSION = '1.21'

DEFINE_X = 80
DEFINE_Y = 50
moveX = DEFINE_X
moveY = DEFINE_Y

print("Click Macro ver {0}".format(VERSION))
print("https://github.com/Jskyu/clickMacro")
print("ON/OFF : ` ")
print("Set X : R, T")
print("Set Y : F, G")
print("Excution : W")

key_w = 'w'

key_r = 'r'
key_t = 't'

key_f = 'f'
key_g = 'g'

key_reset = 'c'

key_execution = '`'

isOn = False

def pressEvent(key):
    global moveX, moveY
    
    # 가로 설정
    if key == key_r:
        moveX = moveX + 10

    elif key == key_t:
        moveX = moveX - 10

        
    # 세로 설정
    elif key == key_f:
        moveY = moveY + 8
    elif key == key_g:
        moveY = moveY - 8
    elif key == key_reset:
        moveX = DEFINE_X
        moveY = DEFINE_Y

    print("Set x : {0}, y : {1}".format(moveX, moveY))


def moveEvent():
    x, y = auto.position()
    auto.click()
    tempX = x
    tempY = y
    print("Execution x : {0}, y : {1}".format(moveX, moveY))
    auto.moveTo(x + moveX, y + moveY)
    auto.click()
    auto.moveTo(tempX, tempY)


while True:
    if keyboard.read_key() == key_execution:
        if not isOn:
            print("MACRO ON")
            time.sleep(0.2)
            isOn = True
        elif isOn:
            print("MACRO OFF")
            time.sleep(0.2)
            isOn = False

    if keyboard.is_pressed(key_r):
        pressEvent(key_r)
        continue
    if keyboard.is_pressed(key_t):
        pressEvent(key_t)
        continue
    
    if keyboard.is_pressed(key_f):
        pressEvent(key_f)
        continue
    if keyboard.is_pressed(key_g):
        pressEvent(key_g)
        continue
    if keyboard.is_pressed(key_w) and isOn:
        moveEvent()
        continue

from platform import version
import keyboard
import pyautogui as auto
import time


VERSION = '1.21'

DEFINE_X = 80
DEFINE_Y = 50
moveX = DEFINE_X
moveY = DEFINE_Y

print("Click Macro ver {0}".format(VERSION))
print("https://github.com/Jskyu/clickMacro")
print("ON/OFF : ` ")
print("Set X : R, T")
print("Set Y : F, G")
print("Excution : W")

key_w = 'w'

key_r = 'r'
key_t = 't'

key_f = 'f'
key_g = 'g'

key_reset = 'c'

key_execution = '`'

isOn = False

def pressEvent(key):
    global moveX, moveY
    
    # 가로 설정
    if key == key_r:
        moveX = moveX + 10

    elif key == key_t:
        moveX = moveX - 10

        
    # 세로 설정
    elif key == key_f:
        moveY = moveY + 8
    elif key == key_g:
        moveY = moveY - 8
    elif key == key_reset:
        moveX = DEFINE_X
        moveY = DEFINE_Y

    print("Set x : {0}, y : {1}".format(moveX, moveY))


def moveEvent():
    x, y = auto.position()
    auto.click()
    tempX = x
    tempY = y
    print("Execution x : {0}, y : {1}".format(moveX, moveY))
    auto.moveTo(x + moveX, y + moveY)
    auto.click()
    auto.moveTo(tempX, tempY)


while True:
    nowKey = keyboard.read_key()
    if nowKey == key_execution:
        if not isOn:
            print("MACRO ON")
            time.sleep(0.2)
            isOn = True
        elif isOn:
            print("MACRO OFF")
            time.sleep(0.2)
            isOn = False

    if keyboard.is_pressed(key_r):
        pressEvent(key_r)
        continue
    if keyboard.is_pressed(key_t):
        pressEvent(key_t)
        continue
    
    if keyboard.is_pressed(key_f):
        pressEvent(key_f)
        continue
    if keyboard.is_pressed(key_g):
        pressEvent(key_g)
        continue
    if keyboard.is_pressed(key_w) and isOn:
        moveEvent()
        continue
