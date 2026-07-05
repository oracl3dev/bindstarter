import evdev
import subprocess
import sys

TARGET = "ENTER YOUR KEYPHRASE HERE"
DEVICE_PATH = sys.argv[1] if len(sys.argv) > 1 else None

KEYMAP = {
    "KEY_A": "a", "KEY_B": "b", "KEY_C": "c", "KEY_D": "d", "KEY_E": "e",
    "KEY_F": "f", "KEY_G": "g", "KEY_H": "h", "KEY_I": "i", "KEY_J": "j",
    "KEY_K": "k", "KEY_L": "l", "KEY_M": "m", "KEY_N": "n", "KEY_O": "o",
    "KEY_P": "p", "KEY_Q": "q", "KEY_R": "r", "KEY_S": "s", "KEY_T": "t",
    "KEY_U": "u", "KEY_V": "v", "KEY_W": "w", "KEY_X": "x", "KEY_Y": "y",
    "KEY_Z": "z", "KEY_SPACE": " ", "KEY_1": "1", "KEY_2": "2",
}

def find_keyboard():
    devices = [evdev.InputDevice(p) for p in evdev.list_devices()]
    for d in devices:
        caps = d.capabilities().get(evdev.ecodes.EV_KEY, [])
        if evdev.ecodes.KEY_A in caps and evdev.ecodes.KEY_SPACE in caps:
            return d
    return None

def main():
    dev = evdev.InputDevice(DEVICE_PATH) if DEVICE_PATH else find_keyboard()
    if dev is None:
        print("ne rabotaet, manual put' bi")
        return

    print(f"Listening on {dev.path} ({dev.name})")
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

        char = KEYMAP.get(keycode)
        if char is None:
            buffer = ""
            continue

        buffer += char
        buffer = buffer[-len(TARGET):]

        if buffer == TARGET:
            subprocess.run(["steam", "game id (example: steam://rungameid/570"])
            buffer = ""

if __name__ == "__main__":
    main()

# you can pass the exact same code after this message substituing the lines 54(process) and 5(keyphrase) in order to change the scripts behaviour, or even include all of the actions in one single script if you feel like launchers are toooo slow :D