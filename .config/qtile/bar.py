from libqtile import bar, layout, widget, hook, qtile
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#colours = ["#171726",
#        "#1a1a28",
#        "#313244",
#        "#282938",
#        ]

background_colours = {
    "background": "#313244",
    "edge_background": "#86d5e3",
    "groups_background": "#d29de3",
    "layout_tray_background": "#86e3bd",
    "cpu_background": "#ffe46e",
    "battery_background": "#849af8",
    "date_background": "f6a8a4",
    "time_background": "f5918c",
}

text_colours = {
    "light_text": "#ffffff",
    "dark_text": "#352d30",
}

group_colours = {
    "current_group": "#ffe46e",
    "active_group": "#ffc261",
    "inactive_group": "#9771A3",
    "urgent_group": "#fc4c9b",
}

accent_1 = "#86d5e3"
accent_2 = "#d29de3"
accent_3 = "#f6a8a4"
accent_4 = "#e3a89d"
accent_5 = "#86e3bd"

def my_bar():
    return bar.Bar(
        [
            # widget.TextBox("Hello World"),
            widget.Spacer(
                length=30,

                background=background_colours["edge_background"],
            ),
            widget.TextBox(
                text="",
                fontsize=38,
                padding=0,

                foreground="#fc4c9b",
                background=background_colours["edge_background"],
            ),
            widget.Spacer(
                length=20,
                
                background=background_colours["edge_background"],
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,
                
                foreground=background_colours["groups_background"],
                background=background_colours["edge_background"],
            ),
            widget.GroupBox(
                highlight_method="text",
                use_mouse_wheel=False,
                urgent_alert_method="text",
                
                fontsize=22,
                rounded=False,
                padding_x=5,
                
                active=group_colours["active_group"], # Has windows in the desktop.
                inactive=group_colours["inactive_group"], # Inactive desktops without windows.
                background=background_colours["groups_background"],
                highlight_color=["#0000ff", "#00ff00"], # Unsure.
                urgent_text=group_colours["urgent_group"],  # Group requesting user input.
                this_current_screen_border=group_colours["current_group"], # Current screen.
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,

                foreground=background_colours["groups_background"],
                background=background_colours["layout_tray_background"],
            ),
            widget.Spacer(
                length=15,
                
                background=background_colours["layout_tray_background"],
            ),
            widget.CurrentLayoutIcon(
                scale=0.8,
                
                foreground="#ff0000",
                background=background_colours["layout_tray_background"],
            ),
            widget.Spacer(
                length=5,
                
                background=background_colours["layout_tray_background"],
            ),
            widget.TextBox(
                text="",
                fontsize=36,
                padding=0,
                
                foreground=background_colours["layout_tray_background"],
            ),
            widget.Spacer(
                length=10,
            ),
            widget.WindowName(
                font="Source Code Pro Semibold Italic",
                fontsize=20,
                center_aligned=True,
                format="{name}",
            ),
            # Add cmus here
            widget.TextBox(
                text="",
                fontsize=36,
                padding=0,
                
                foreground=background_colours["cpu_background"],
            ),
            widget.CPU(
                format="󰍛 {freq_current} GHz {load_percent} % ",
                font="Fira Code Retina",
                fontsize=25,
                
                foreground=text_colours["dark_text"],
                background=background_colours["cpu_background"],
            ),
            widget.TextBox(
                text=" ",
                font="Fira Code Retina",
                fontsize=25,

                foreground=text_colours["dark_text"],
                background=background_colours["cpu_background"],
            ),
            widget.ThermalZone(
                high=200000,
                crit=2000000,
                format="{temp}°",
                font="Fira Code Retina",
                fontsize=25,
                
                fgcolor_normal=text_colours["dark_text"],
                background=background_colours["cpu_background"],
            ),
            widget.TextBox(
                text="",
                fontsize=36,
                padding=0,
                
                foreground=background_colours["cpu_background"],
                background=accent_5,
            ),
            widget.Spacer(
                length=3,
                
                background=background_colours["layout_tray_background"],
            ),
            widget.PulseVolume(
                volume_app="pavucontrol",
                mouse_callbacks={"Button3": lazy.spawn("pavucontrol")},
                
                emoji=True,
                fontsize=20,
                background=background_colours["layout_tray_background"],
            ),
            widget.Systray(
                icon_size=47,
                background=background_colours["layout_tray_background"],
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,

                foreground=background_colours["battery_background"],
                background=background_colours["layout_tray_background"],
            ),
            widget.Spacer(
                length=5,
                
                background=background_colours["battery_background"],
            ),
            widget.Battery(
                full_char="󰁹",
                charge_char="󰂄",
                discharge_char="󰂌",
                empty_char="󰂎",
                unknown_char="󰂑",
                low_foreground="F36885",
                format="{char}",
                fontsize=30,
                background=background_colours["battery_background"],
            ),
            widget.Spacer(
                length=7,

                background=background_colours["battery_background"],
            ),
            widget.Battery(
                format="{percent:1.0%} {watt:.2f} W",
                font="Fira Code Retina",
                fontsize=25,
                low_foreground="#ffffff",
                background=background_colours["battery_background"],
                # Do notification later
            ),
            widget.Spacer(
                length=10,
                
                background=background_colours["battery_background"],
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,
                
                foreground=background_colours["date_background"],
                background=background_colours["battery_background"],
            ),
            widget.Spacer(
                length=2,
                
                background=background_colours["date_background"],
            ),
            widget.TextBox(
                text="",
                fontsize=30,
                
                foreground=text_colours["dark_text"],
                background=background_colours["date_background"],
            ),
            widget.Spacer(
                length=7,
                
                background=background_colours["date_background"],
            ),
            widget.Clock(
                format="%a, %-d %b",
                fontsize=25,
                font="Fira Code Retina",

                foreground=text_colours["dark_text"],
                background=background_colours["date_background"],
            ),
            widget.Spacer(
                length=7,
                
                background=background_colours["date_background"],
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,
                
                foreground=background_colours["time_background"],
                background=background_colours["date_background"],
            ),
            widget.TextBox(
                text="󰅐",
                fontsize=30,
                
                foreground=text_colours["dark_text"],
                background=background_colours["time_background"],
            ),
            widget.Spacer(
                length=5,
                
                background=background_colours["time_background"],
            ),
            widget.Clock(
                format="%H:%M",
                font="Fira Code Retina",
                fontsize=25,
                
                foreground=text_colours["dark_text"],
                background=background_colours["time_background"],
            ),
            widget.TextBox(
                text="",
                padding=0,
                fontsize=36,

                foreground=background_colours["time_background"],
                background=background_colours["edge_background"],
            ),
            widget.Spacer(
                length=22,

                background=background_colours["edge_background"],
            ),
        ],
        size=42,
        margin=[6, 6, 4, 6],
        opacity=0.85,
        background=background_colours["background"],
    )
