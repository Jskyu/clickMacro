from platform import version
import keyboard
import pyautogui as auto
import time


VERSION = '2.0'

DEFINE_X = 80
DEFINE_Y = 50
moveX = DEFINE_X
moveY = DEFINE_Y

print("Click Macro ver {0}".format(VERSION))
print("https://github.com/Jskyu/clickMacro")
print("ON/OFF : ` ")
print("Plus X : R,  Minus X : F")
print("Plus Y : T,  Minus X : G")
print("Reset X And Y : C")
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
    isKey = False
    
    # 가로 설정
    if key == key_r:
        moveX = moveX + 10
        isKey = True
    elif key == key_f:
        moveX = moveX - 10
        isKey = True

    # 세로 설정
    elif key == key_t:
        moveY = moveY + 8
        isKey = True
    elif key == key_g:
        moveY = moveY - 8
        isKey = True
    elif key == key_reset:
        moveX = DEFINE_X
        moveY = DEFINE_Y
        isKey = True

    if isKey:
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
            isOn = True
            time.sleep(0.2)
        elif isOn:
            print("MACRO OFF")
            isOn = False
            time.sleep(0.2)
        continue

    if nowKey == key_w and isOn:
        moveEvent()
        continue
    
    pressEvent(nowKey)
    time.sleep(0.2)
    
