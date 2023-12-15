import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

#--------------------------------------------------#
#                                                  #
#              VEKSIAK'S QTILE CONFIG              #
#                  FOR ARCH LINUX                  #
#                                                  #
#--------------------------------------------------#

# In order to display the icons on the bar download a nerd font. 

#<-----MODKEY----->#

mod = "mod1"

#<-----DEFAULT APPS [MUST BE SET IN ORDER TO ACHIEVE AN ACCEPTABLE WORKFLOW]----->#

terminal = "alacritty"
browser = "firefox"
file_manager = "nemo"

#<-----ROFI CONFIGURATION FILE PATH----->#

rofi_config_path = "" #Fill this in by yourself

#<-----SCRIPTS----->#

power_menu_script_path = "" #Fill this in by yourself
autostart_script_path = os.path.expanduser("~/.config/qtile/autostart.sh")  
autostart_once_script_path = os.path.expanduser("~/.config/qtile/autostart_once.sh")

#<-----CPU THERMAL ZONE [TEMPERATURE FILE PATH]------>#

cpu_thermal_zone = "" #Fill this in by yourself

#<-----WIFI NETWORK INTERFACE NAME----->#

wifi_interface = "" #Fill this in by yourself

#<-----KEYBINDS----->#

keys = [
                          #<[Window Control Section]>#

    Key([mod], "space", lazy.layout.next()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "w", lazy.window.toggle_floating()),
    Key([mod, "shift"], "q", lazy.window.kill()),
   
                       	  #<[System Control Section]># 

    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "s", lazy.spawn(power_menu_script_path)),
	Key([mod, "control"], "c", lazy.spawn("betterlockscreen -l")),

						#<[Layout Control Section]>#

    Key([mod, "shift"], "m", lazy.layout.toggle_split()),
    Key([mod], "Tab", lazy.next_layout()),

                        #<[Media Control Section]>#

    Key([mod, "shift"], "z", lazy.spawn("playerctl previous")),
    Key([mod, "shift"], "x", lazy.spawn("playerctl play-pause")),
    Key([mod, "shift"], "c", lazy.spawn("playerctl next")),

                           	   #<[App Section]>#

    Key([mod, "shift"], "a", lazy.spawn(browser)),
    Key([mod, "shift"], "s", lazy.spawn(file_manager)),
    Key([mod, "shift"], "d", lazy.spawn(terminal)),
    Key([mod, "shift"], "Return", lazy.spawn(terminal)),
	Key([mod], "c", lazy.spawn(f"rofi -config {rofi_config_path} -show drun")),
    Key([mod, "shift"], "f", lazy.spawn("flameshot gui")),
]

#<-----GROUPS----->#
	
groups = [
	Group (name="1", label="1"),
    Group (name="2", label="Firefox", matches=[Match(wm_class=["firefox", "mpv"])], layout=("stack"), exclusive=True),
	Group (name="3", label="Discord", matches=[Match(wm_class=["discord"])], layout=("stack"), exclusive=True),
	Group (name="4", label="Game", matches=[Match(wm_class=["cs2"])], layout=("max"), exclusive=False),
	Group (name="5", label="Steam", matches=[Match(wm_class=["steam"])], layout=("stack"), exclusive=True),
	Group (name="6", label="6"),
	Group (name="7", label="7"),
	Group (name="8", label="8"),
	Group (name="9", label="9"),
]

#<-----COLORS/THEME----->#

colors = [
    ["#14181F", "#14181F"], #-> Background color of the bar
    ["#9494b8", "#9494b8"], #-> Foreground color of the bar
    ["#d9262f", "#d9262f"], #-> First alt color of the bar
    ["#c60609", "#c60609"], #-> Second alt color of the bar
    ["#d9262f", "#d9262f"], #-> Color of the focused window borders
    ["#494b50", "#494b50"]  #-> Color of the unfocused window borders
]

#<-----WIDGETS DEFAULTS----->#

widget_defaults = dict(
        font="sans",
    fontsize=12,
    padding=3,
)

#<-----RECURRING WIDGETS----->#

pltextbox1 = widget.TextBox(background=colors[3], foreground=colors[2], text="", padding=0, fontsize=30)
pltextbox2 = widget.TextBox(background=colors[2], foreground=colors[3], text="", padding=0, fontsize=30)
pltextbox3 = widget.TextBox(background=colors[0], foreground=colors[2], text="", padding=0, fontsize=25)
pltextbox4 = widget.TextBox(background=colors[0], foreground=colors[3], text="", padding=0, fontsize=30)

#<-----BAR WIDGETS----->#

def init_bar_widgets():
	return [
		widget.GroupBox(background=colors[0],highlight_color=colors[0], disable_drag=True, highlight_method="line", this_current_screen_border=colors[2][1]),
        widget.WindowName(background=colors[0], fmt='[ {} ]', max_chars=60),
        widget.Spacer(background=colors[0]),
		pltextbox3,
		widget.Systray(background=colors[2]),
        pltextbox2,
		widget.CheckUpdates(background=colors[3], distro="Arch_checkupdates", display_format="   {updates}  "),
        pltextbox1,
		widget.CPU(background=colors[2], format='   {load_percent}%'),
		widget.ThermalZone(background=colors[2], zone=cpu_thermal_zone, high=60, crit=75, fmt='󰔏  {}  '),
		pltextbox2,
		widget.Memory(background=colors[3], format='󰧑   {MemUsed:.0f} {mm}  '),
		pltextbox1,
		widget.Wlan(background=colors[2], interface=wifi_interface, measure_mem='G', format='󰖩   {essid} {percent:2.0%}  '), 
		pltextbox2,
		widget.PulseVolume(background=colors[3], fmt='    {}  ', limit_max_volume=True, step=5),
		pltextbox1,
		widget.Clock(background=colors[2], fmt="   {}   "),
	]

#<-----ACTIVE LAYOUTS----->#

layouts = [
    layout.Columns(
        border_width=2,
        margin=8,
        border_focus=[colors[4][1]],
		border_normal=[colors[5][1]],
		border_on_single=True
	),
    layout.Max(),
    layout.Stack( 
		num_stacks=1,
		margin=8,
		border_width=2,
		border_focus=[colors[4][1]],
		border_normal=[colors[5][1]]
	)
]

#<-----MOUSE BINDS----->#

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
]

#<-----AUTOSTART SCRIPT----->#

@hook.subscribe.startup_once
def autostart_once():
	home = autostart_once_script_path
	subprocess.Popen([home])

@hook.subscribe.startup
def autostart():
	home = autostart_script_path 
	subprocess.Popen([home])

dgroups_key_binder = None
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[Match(wm_class=["feh"])],
	border_width=2,
	border_focus=colors[4][1],
	border_normal=colors[5][1],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False 
wl_input_rules = None
wmname = "Qtile"


for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen()
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True)
            )
        ]
    )

screens = [
	Screen(
		top=bar.Bar(init_bar_widgets(), 24)
	)
]

