from pynput import mouse, keyboard
import threading
import time
import sys
from time import sleep
import ctypes
from assest.setting import RECOIL_VALUE 
from colorama import Fore

mouse_left_button = False
mouse_right_button = False
right_click_start_time = 0 
threads_ = False

controll = mouse.Controller()


def printf(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        sleep(0.045)

def isTesting():
    if RECOIL_VALUE == " " or isinstance(RECOIL_VALUE, str):
        return input("반동제어 값은 항상 숫자형 이어야 하거나 공백이면 안 됩니다.")
    else:
        Start()

def clear():
    import os
    return os.system("cls")

def IsKeyPressed(key_):
    from assest.SoundPlay import isOnSound, isOffSound
    global threads_
    if key_ == keyboard.Key.f10:
        isOffSound()
        threads_ = True
        clear()
        return printf("종료 되었습니다.\n다시 시작할려면 f9를 눌러주세요")
        
    elif key_ == keyboard.Key.f9:
        isOnSound()
        clear()
        threads_ = False
        return printf("매크로가 다시 시작되었습니다.\n종료 할려면 f10를 눌러주세요")

def IsClick(x, y, btn, press):
    global mouse_left_button, mouse_right_button, right_click_start_time
    if btn == mouse.Button.left:
        mouse_left_button = press
    elif btn == mouse.Button.right:
        if press:
            right_click_start_time = time.time()
            mouse_right_button = True
        else:
            mouse_right_button = False

def MagicMouse_Move(x, y):
    ctypes.windll.user32.mouse_event(0x0001, x, y, 0, 0)

def RecoilMouse():
    global threads_
    print(f"현재 반동 제어 값 : {RECOIL_VALUE}")
    while True:  # 무한 루프
        if threads_ == True:
            time.sleep(0.01)
        while not threads_:  # threads_ 플래그가 True가 아닐 때 반복
            if mouse_left_button:
                if mouse_right_button and (time.time() - right_click_start_time >= 0.1):
                    MagicMouse_Move(0, int(RECOIL_VALUE)) 
                    time.sleep(0.01)    
            else:
                time.sleep(0.01)

mouse_listener = mouse.Listener(on_click=IsClick)
keyboard_listener = keyboard.Listener(on_press=IsKeyPressed)
threads = threading.Thread(target=RecoilMouse)
threads.daemon = True


def window_sizes():
    import os
    os.system("title PARTYNEXTDOOR")
    os.system("mode con: cols=30 lines=8")
    

def Start():
    sleep(2)
    clear()
    mouse_listener.start()
    keyboard_listener.start()
    threads.start()
    mouse_listener.join()
    keyboard_listener.join()

if __name__ == "__main__":
    window_sizes()
    isTesting()
