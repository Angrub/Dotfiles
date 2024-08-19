# Qtile keybindings

from libqtile.config import Key
from libqtile.lazy import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    ([mod], "h", lazy.layout.left(), "Move focus to left"),
    ([mod], "l", lazy.layout.right(), "Move focus to right"),
    ([mod], "j", lazy.layout.down(), "Move focus down"),
    ([mod], "k", lazy.layout.up(), "Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    ([mod, "shift"], "h", lazy.layout.shuffle_left(), "Move window to the left"),
    ([mod, "shift"], "l", lazy.layout.shuffle_right(), "Move window to the right"),
    ([mod, "shift"], "j", lazy.layout.shuffle_down(), "Move window down"),
    ([mod, "shift"], "k", lazy.layout.shuffle_up(), "Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    ([mod, "control"], "h", lazy.layout.grow_left(), "Grow window to the left"),
    ([mod, "control"], "l", lazy.layout.grow_right(), "Grow window to the right"),
    ([mod, "control"], "j", lazy.layout.grow_down(), "Grow window down"),
    ([mod, "control"], "k", lazy.layout.grow_up(), "Grow window up"),
    ([mod], "n", lazy.layout.normalize(), "Reset all window sizes"),
    ([mod], "t", lazy.window.toggle_floating(), "Toggle floating on the focused window"),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout(), "Toggle between layouts"),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart/Shutdown Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # Lock Lightdm dm-tool lock
    ([mod], "i", lazy.spawn("dm-tool lock")),
    # ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show run")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 5000")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([], "Print", lazy.spawn("scrot -s -e 'mv $f ~/Images/Screenshots/' ")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
