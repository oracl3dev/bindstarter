# bindstarter

Keyboard listener for Wayland/Hyprland that runs a shell command when you type a configured phrase. Reads raw keycodes via evdev, so it works regardless of active keyboard layout.

## Requirements

- Python 3
- `evdev` (`pip install evdev --break-system-packages`)
- User in the `input` group (`sudo usermod -aG input $USER`, re-login after)

## Usage

Edit the `TRIGGERS` dict at the top of `bindstarter.py`:

```python
TRIGGERS = {
    "doka 2": "steam steam://rungameid/570",
    "cs2": "steam steam://rungameid/730",
    "lock": "hyprlock",
}
```

Run:

```
python3 bindstarter.py
```

Pass a device path manually if autodetection picks the wrong keyboard:

```
python3 bindstarter.py /dev/input/eventX
```

Find your keyboard's path via `ls /dev/input/by-id/`.

## Autostart (Hyprland)

```
exec-once = python3 /path/to/bindstarter.py
```

## Limitations

- Handles letters, space, digits, and backspace — no other special keys
- Commands run via `shell=True`, so don't put untrusted input in TRIGGERS
