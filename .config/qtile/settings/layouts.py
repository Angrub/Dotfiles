# Layouts and layout rules

from libqtile import layout
from libqtile.config import Match
from .theme import colors



layout_conf = {
    'border_focus': colors['light'][0],
    'border_width': 2,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.Columns(**layout_conf),
    # layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'), # gitk
        Match(wm_class='makebranch'), # gitk
        Match(wm_class='maketag'), # gitk
        Match(wm_class='ssh-askpass'), # ssh-askpass
        Match(title='branchdialog'), # gitk
        Match(title='pinentry'), # GPG key password entry
    ],
    border_focus=colors["color4"][0]
)
