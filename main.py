import keyboard
import pyautogui as auto


def pressEvent(key):
    global tempX, tempY
    global moveY, moveX

    x, y = auto.position()
    # 정사각형
    if key == 'q':
        moveX = 100
        moveY = 100
    elif key == 'w':
        moveX = 70
        moveY = 70
    elif key == 'e':
        moveX = 50
        moveY = 50
    elif key == 'r':
        moveX = 40
        moveY = 40
    elif key == 't':
        moveX = 30
        moveY = 30

    #   가로 직사각형
    elif key == 'z':
        moveX = 100
        moveY = 50
    elif key == 'x':
        moveX = 80
        moveY = 40
    elif key == 'c':
        moveX = 60
        moveY = 30
    elif key == 'v':
        moveX = 40
        moveY = 20
    elif key == 'b':
        moveX = 30
        moveY = 15

    #   세로직사각형
    elif key == '1':
        moveX = 50
        moveY = 100
    elif key == '2':
        moveX = 40
        moveY = 80
    elif key == '3':
        moveX = 30
        moveY = 60
    elif key == '4':
        moveX = 20
        moveY = 40
    elif key == '5':
        moveX = 15
        moveY = 30

    auto.click()
    tempX = x
    tempY = y
    auto.moveTo(x + moveX, y + moveY)
    auto.click()
    auto.moveTo(tempX, tempY)


while True:
    if keyboard.is_pressed('q'):
        pressEvent('q')
    if keyboard.is_pressed('w'):
        pressEvent('w')
    if keyboard.is_pressed('e'):
        pressEvent('e')
    if keyboard.is_pressed('r'):
        pressEvent('r')
    if keyboard.is_pressed('t'):
        pressEvent('t')
    if keyboard.is_pressed('z'):
        pressEvent('z')
    if keyboard.is_pressed('x'):
        pressEvent('x')
    if keyboard.is_pressed('c'):
        pressEvent('c')
    if keyboard.is_pressed('v'):
        pressEvent('v')
    if keyboard.is_pressed('b'):
        pressEvent('b')
    if keyboard.is_pressed('1'):
        pressEvent('1')
    if keyboard.is_pressed('2'):
        pressEvent('2')
    if keyboard.is_pressed('3'):
        pressEvent('3')
    if keyboard.is_pressed('4'):
        pressEvent('4')
    if keyboard.is_pressed('5'):
        pressEvent('5')
