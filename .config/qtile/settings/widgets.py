from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(_padding=5, _bg='dark'):
    return widget.Sep(**base(bg=_bg), linewidth=0, padding=_padding)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def edge(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-ple-upper_right_triangle
        fontsize=60,
        padding=-1,
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='CaskaydiaCove Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    # ------------- Software Updates -------------
    edge('color4', 'dark'),

    separator(8, 'color4'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='N/A',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    separator(10, 'color4'),

    # ------------- Net -------------
    edge('color3', 'color4'),

    separator(8, 'color3'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(
        **base(bg='color3'),
        interface='wlp0s20f3',
    ),

    separator(5, 'color3'),
    
    # ------------- Memory stats -------------
    edge('color2', 'color3'),

    widget.Memory(
        **base(bg='color2'),
        padding=10,
        measure_mem='M',
        format='RAM{MemUsed: .0f}{mm} /{MemTotal: .0f}{mm}'
    ),

    # ------------- CPU stats -------------
    edge('color1', 'color2'),

    widget.CPU(**base(bg='color1'), padding=11),

    widget.CPUGraph(
        **base(bg='color1'),
        padding=15,
        type='box',
        graph_color=colors['text']
    ),

    widget.ThermalSensor(
        **base(bg='color1'),
        format='{temp:.1f}{unit}',
        tag_sensor='CPU',
        padding=10
    ),

    # ------------- Systray & Clock -------------
    edge('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),

    separator(20),

    icon(bg="dark", fg='light', fontsize=17, text='󰃰 '), # Icon: nf-md-calendar_clock

    widget.Clock(**base(bg='dark', fg='light'), format='%d-%m-%Y - %H:%M '),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    edge('color4', 'dark'),

    widget.CPU(**base(bg='color4'), padding=11),

    widget.CPUGraph(
        **base(bg='color4'),
        padding=15,
        type='box',
        graph_color=colors['text']
    ),

    widget.ThermalSensor(
        **base(bg='color4'),
        format='{temp:.1f}{unit}',
        tag_sensor='CPU',
        padding=10
    ),

    edge('color3', 'color4'),

    icon(bg="color3", fg='text', fontsize=17, text='󰃰 '), # Icon: nf-md-calendar_clock

    widget.Clock(**base(bg='color3', fg='text'), format='%d-%m-%Y - %H:%M '),

    edge('dark', 'color3'),
]

terciary_widgets = [
    *workspaces(),

    separator(),

    edge('color4', 'dark'),

    widget.CPU(**base(bg='color4'), padding=11),

    widget.CPUGraph(
        **base(bg='color4'),
        padding=15,
        type='box',
        graph_color=colors['text']
    ),

    widget.ThermalSensor(
        **base(bg='color4'),
        format='{temp:.1f}{unit}',
        tag_sensor='CPU',
        padding=10
    ),

    edge('color3', 'color4'),

    icon(bg="color3", fg='text', fontsize=17, text='󰃰 '), # Icon: nf-md-calendar_clock

    widget.Clock(**base(bg='color3', fg='text'), format='%d-%m-%Y - %H:%M '),

    edge('dark', 'color3'),
]

widget_defaults = {
    'font': 'CaskaydiaCove Nerd Font',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()