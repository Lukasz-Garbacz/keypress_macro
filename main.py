import threading
import pygetwindow as gw

from pynput.keyboard import Listener, Controller
from time import sleep
from random import random
from settings import Settings as st

 
def keep_pressing_sequence(button_list: list[str], wait_times: list[float], offsets: list[float]) -> None:
    keyboard = Controller()
    while keep_pressing_flag:
        for idx, button in enumerate(button_list):
            try:
                if gw.getActiveWindow().title == st.desired_window_name:
                    keyboard.press(button)
                    keyboard.release(button)
                    sleep(wait_times[idx] + random() * offsets[idx])
                else:
                    sleep(0.18)
            except Exception:
                sleep(0.18)

def on_press(key):
    global keep_pressing_flag
    if key == st.start_health_flask and gw.getActiveWindow().title == st.desired_window_name:
        keep_pressing_flag = True
        threading.Thread(target=keep_pressing_sequence, args= (st.health_flask, st.wait_health_flask, st.wait_health_flask_offset)).start()

    elif key == st.start_quicksilver_flasks and gw.getActiveWindow().title == st.desired_window_name:
        keep_pressing_flag = True
        threading.Thread(target=keep_pressing_sequence, args= (st.quicksilver_flasks, st.wait_quicksilver_flasks, st.wait_quicksilver_flasks_offset)).start()

def on_release(key):
    if key == st.stop_all:
        # Stop listener
        global keep_pressing_flag
        keep_pressing_flag = False
        return False


if __name__ == "__main__":
    global keep_pressing_flag
    keep_pressing_flag = True

    while True:
        # Collect events until released
        try:
            with Listener(
                    on_press=on_press,
                    on_release=on_release) as listener:
                listener.join()
        except Exception:
            pass