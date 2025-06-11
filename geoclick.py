import pygame
import threading
import time
import psutil
import subprocess
from pynput import keyboard, mouse

# === The Path to Sound ===
SOUND_PATH = "/home/admin/Downloads/mouse-click-153941.mp3"

GAME_PROCESS_NAME = "GeometryDash.exe"
pressed_keys = set()

pygame.mixer.init()
click_sound = pygame.mixer.Sound(SOUND_PATH)

def play_sound():
    click_sound.play()

def is_gd_focused():
    try:
        active_win = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode().strip()
        return "Geometry Dash" in active_win
    except Exception:
        return False

def is_game_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == GAME_PROCESS_NAME:
            return True
    return False

def on_press(key):
    if not is_gd_focused():
        return
    try:
        if key.char.lower() == 'w' and key not in pressed_keys:
            pressed_keys.add(key)
            play_sound()
    except AttributeError:
        if key in [keyboard.Key.space, keyboard.Key.up] and key not in pressed_keys:
            pressed_keys.add(key)
            play_sound()

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def on_click(x, y, button, pressed):
    if not is_gd_focused():
        return
    if button == mouse.Button.left and pressed:
        play_sound()

def watch_game():
    while True:
        if not is_game_running():
            exit(0)
        time.sleep(2)

if __name__ == "__main__":
    print("== ClickSound Mod active ==")
    print(f"path to sound: {SOUND_PATH}")

    threading.Thread(target=watch_game, daemon=True).start()

    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    mouse_listener = mouse.Listener(on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()

    keyboard_listener.join()
    mouse_listener.join()
