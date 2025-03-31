from dataclasses import dataclass
from pynput.keyboard import Key


@dataclass
class Settings:
    health_flask= ['1']
    quicksilver_flasks = ['3', '4', '5']
    start_quicksilver_flasks= Key.f6
    start_health_flask= Key.f7
    stop_all= Key.f8
    
    #constant wait times between flask uses
    wait_health_flask= [3.2]
    wait_quicksilver_flasks = [3.7, 2.9, 2.9]
    #random wait between 0 and wait_offset in seconds (in addition to wait times above)
    wait_health_flask_offset= [0.33]
    wait_quicksilver_flasks_offset = [0.32, 0.25, 0.25]

    desired_window_name = 'Path of Exile'