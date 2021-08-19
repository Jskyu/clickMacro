import keyboard
import pyautogui as auto


def pressEvent(key):
    tempX = 0
    tempY = 0
    moveY = 0
    moveX = 0

    x, y = auto.position()
    # 정사각형
    if key == key_r:
        moveX = 100
        moveY = 100
    elif key == key_t:
        moveX = 70
        moveY = 70
    elif key == key_y:
        moveX = 50
        moveY = 50
    elif key == key_u:
        moveX = 40
        moveY = 40
    elif key == key_i:
        moveX = 30
        moveY = 30

    #   가로 직사각형
    elif key == key_z:
        moveX = 100
        moveY = 65
    elif key == key_x:
        moveX = 80
        moveY = 50
    elif key == key_c:
        moveX = 60
        moveY = 35
    elif key == key_v:
        moveX = 40
        moveY = 20
    elif key == key_b:
        moveX = 30
        moveY = 15

    #   세로직사각형
    elif key == key_f:
        moveX = 50
        moveY = 100
    elif key == key_g:
        moveX = 40
        moveY = 80
    elif key == key_h:
        moveX = 30
        moveY = 60
    elif key == key_j:
        moveX = 20
        moveY = 40
    elif key == key_k:
        moveX = 15
        moveY = 30

    auto.click()
    tempX = x
    tempY = y
    auto.moveTo(x + moveX, y + moveY)
    auto.click()
    auto.moveTo(tempX, tempY)

key_r = 'r'
key_t = 't'
key_y = 'y'
key_u = 'u'
key_i = 'i'

key_f = 'f'
key_g = 'g'
key_h = 'h'
key_j = 'j'
key_k = 'k'

key_z = 'z'
key_x = 'x'
key_c = 'c'
key_v = 'v'
key_b = 'b'

isOn = False

while True:
    if(keyboard.is_pressed('`')) :
        isOn = True
    while isOn:
        if(keyboard.is_pressed('`')) :
            isOn = False
            break
        if keyboard.is_pressed(key_r):
            pressEvent(key_r)
        if keyboard.is_pressed(key_t):
            pressEvent(key_t)
        if keyboard.is_pressed(key_y):
            pressEvent(key_y)
        if keyboard.is_pressed(key_u):
            pressEvent(key_u)
        if keyboard.is_pressed(key_i):
            pressEvent(key_i)
        if keyboard.is_pressed(key_z):
            pressEvent(key_z)
        if keyboard.is_pressed(key_x):
            pressEvent(key_x)
        if keyboard.is_pressed(key_c):
            pressEvent(key_c)
        if keyboard.is_pressed(key_v):
            pressEvent(key_v)
        if keyboard.is_pressed(key_b):
            pressEvent(key_b)
        if keyboard.is_pressed(key_f):
            pressEvent(key_f)
        if keyboard.is_pressed(key_g):
            pressEvent(key_g)
        if keyboard.is_pressed(key_h):
            pressEvent(key_h)
        if keyboard.is_pressed(key_j):
            pressEvent(key_j)
        if keyboard.is_pressed(key_k):
            pressEvent(key_k)
