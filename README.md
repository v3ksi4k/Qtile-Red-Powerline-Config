# I won't accept any pull requests

## Qtile-Red-Powerline-Config

A simple qtile configuration that utilizes powerline characters in the bar.

The default color scheme is red, but it can be eaisly changed.

This config is made for arch linux. If you want to use it on other distros, please configure it to support your system by following the qtile's documentation.

## Setup tutorial:

**Read before installing! This config currently is not full and won't provide high quality experience wihout later configuration.**

1) Make sure that qtile is installed on your machine

2) **Backup your existing qtile configuration files** which are usually located in:

  `~/.config/qtile`

3) **When you're sure that everything is safe and backed up**, remove the configuration files from your qtile's config directory

4) Clone this repository into the right directory:

`git clone https://github.com/v3ksi4k/Qtile-Red-Powerline-Config/tree/master` 

5) Modify the config to your liking. Focus on the variables in the beggining of the file.

6) If you want, add startup commands by editing autostart.sh and autostart_once.sh files. They are linked to the config by default

## Keybinds

* Have in mind that only the most important keybinds are listed. 

*() - Requirements*

#[alt] + 
- Space - Switch focus to the next window.
- h,j,k,l - Switch focus to the window located in the specified direction.
- f - Toggle fullscreen on a currently focused window.
- 1,2,3...9 - Switch to a workspace with a specific number.

(rofi)
- c - Open rofi application launcher. (Currently requires personal configuration)

#[alt] + [shift] +
- h,j,k,l - Shuffle the currently focused window in a specific direction.
- 1,2,3...9 - Move a currently focused to a workspace with a specific number.
- w - Toggle the floating of a currently focused window.
- q - Kill the currently focused window.
- m - Toggle the splitting between a group of windows.

(playerctl)
- z - Play the previous song.
- x - Play/Pause the music player.
- c - Play the next song.

- a - Spawn a browser specified at the beggining of the config.
- s - Spawn a file manager specified at the beggining of the config.
- d,Return - Spawn a terminal specified at the beggining og the config.

(flameshot)
- f - Open the screenshot menu.

#[alt] + [control] +
- h,j,k,l - Control the size of the currently focused window.
- r - Reload the config.

(rofi + a custom script)
- s - Open the power menu.

(betterlockscreen)
- c - Lock the screen 
