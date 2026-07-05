import evdev
import subprocess
import sys

TRIGGERS = { 
    
    #example triggers (phrases you need to type), 
    #you may check those you don't need and add those you do need following the shown format :D

    "dota 2": "steam steam://rungameid/570",
    "cs2": "steam steam://rungameid/730",
    "lock": "hyprlock",
}

DEVICE_PATH = sys.argv[1] if len(sys.argv) > 1 else None

KEYMAP = {
    "KEY_A": "a", "KEY_B": "b", "KEY_C": "c", "KEY_D": "d", "KEY_E": "e",
    "KEY_F": "f", "KEY_G": "g", "KEY_H": "h", "KEY_I": "i", "KEY_J": "j",
    "KEY_K": "k", "KEY_L": "l", "KEY_M": "m", "KEY_N": "n", "KEY_O": "o",
    "KEY_P": "p", "KEY_Q": "q", "KEY_R": "r", "KEY_S": "s", "KEY_T": "t",
    "KEY_U": "u", "KEY_V": "v", "KEY_W": "w", "KEY_X": "x", "KEY_Y": "y",
    "KEY_Z": "z", "KEY_SPACE": " ",
    "KEY_0": "0", "KEY_1": "1", "KEY_2": "2", "KEY_3": "3", "KEY_4": "4",
    "KEY_5": "5", "KEY_6": "6", "KEY_7": "7", "KEY_8": "8", "KEY_9": "9",
}

def find_keyboard():
    devices = [evdev.InputDevice(p) for p in evdev.list_devices()]
    for d in devices:
        caps = d.capabilities().get(evdev.ecodes.EV_KEY, [])
        if evdev.ecodes.KEY_A in caps and evdev.ecodes.KEY_SPACE in caps:
            return d
    return None

def main():
    max_len = max(len(p) for p in TRIGGERS)

    dev = evdev.InputDevice(DEVICE_PATH) if DEVICE_PATH else find_keyboard()
    if dev is None:
        print("Keyboard not found. Pass device path manually, see /dev/input/by-id/")
        return

    print(f"Listening on {dev.path} ({dev.name})")
    print(f"Loaded triggers: {list(TRIGGERS.keys())}")
    buffer = ""

    for event in dev.read_loop():
        if event.type != evdev.ecodes.EV_KEY:
            continue
        key_event = evdev.categorize(event)
        if key_event.keystate != key_event.key_down:
            continue

        keycode = key_event.keycode
        if isinstance(keycode, list):
            keycode = keycode[0]

        if keycode == "KEY_BACKSPACE":
            buffer = buffer[:-1]
            continue

        char = KEYMAP.get(keycode)
        if char is None:
            buffer = ""
            continue

        buffer += char
        buffer = buffer[-max_len:]

        for phrase, command in TRIGGERS.items():
            if buffer.endswith(phrase):
                subprocess.run(command, shell=True)
                buffer = ""
                break

if __name__ == "__main__":
    main()