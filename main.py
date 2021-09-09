from platform import version
import keyboard
import pyautogui as auto
import time


VERSION = '1.21'

DEFINE_X = 150
DEFINE_Y = 135
moveX = 0
moveY = 0

print("Click Macro ver {0}".format(VERSION))
print("https://github.com/Jskyu/clickMacro")
print("ON/OFF : ` ")
print("Set X : R, T, Y, U, I, O, P")
print("Set Y : F, G, H, J, K, L, ;")
print("Excution : W")

def pressEvent(key):
    global moveX, moveY
    # 가로 설정
    if key == key_r:
        moveX = DEFINE_X
    elif key == key_t:
        moveX = DEFINE_X - 20
    elif key == key_y:
        moveX = DEFINE_X - 40
    elif key == key_u:
        moveX = DEFINE_X - 60
    elif key == key_i:
        moveX = DEFINE_X - 80
    elif key == key_o:
        moveX = DEFINE_X - 100
    elif key == key_p:
        moveX = DEFINE_X - 120

    # 세로 설정
    elif key == key_f:
        moveY = DEFINE_Y
    elif key == key_g:
        moveY = DEFINE_Y - 20
    elif key == key_h:
        moveY = DEFINE_Y - 40
    elif key == key_j:
        moveY = DEFINE_Y - 60
    elif key == key_k:
        moveY = DEFINE_Y - 80
    elif key == key_l:
        moveY = DEFINE_Y - 100
    elif key == key_semiClone:
        moveY = DEFINE_Y - 120

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


key_w = 'w'

key_r = 'r'
key_t = 't'
key_y = 'y'
key_u = 'u'
key_i = 'i'
key_o = 'o'
key_p = 'p'

key_f = 'f'
key_g = 'g'
key_h = 'h'
key_j = 'j'
key_k = 'k'
key_l = 'j'
key_semiClone = ';'

# key_z = 'z'
# key_x = 'x'
# key_c = 'c'
# key_v = 'v'
# key_b = 'b'

key_execution = '`'

isOn = False


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
    if keyboard.is_pressed(key_y):
        pressEvent(key_y)
        continue
    if keyboard.is_pressed(key_u):
        pressEvent(key_u)
        continue
    if keyboard.is_pressed(key_i):
        pressEvent(key_i)
        continue
    if keyboard.is_pressed(key_o):
        pressEvent(key_o)
        continue
    if keyboard.is_pressed(key_p):
        pressEvent(key_p)
        continue
    
    if keyboard.is_pressed(key_f):
        pressEvent(key_f)
        continue
    if keyboard.is_pressed(key_g):
        pressEvent(key_g)
        continue
    if keyboard.is_pressed(key_h):
        pressEvent(key_h)
        continue
    if keyboard.is_pressed(key_j):
        pressEvent(key_j)
        continue
    if keyboard.is_pressed(key_k):
        pressEvent(key_k)
        continue
    if keyboard.is_pressed(key_l):
        pressEvent(key_l)
        continue
    if keyboard.is_pressed(key_semiClone):
        pressEvent(key_semiClone)
        continue
    if keyboard.is_pressed(key_w) and isOn:
        moveEvent()
        continue