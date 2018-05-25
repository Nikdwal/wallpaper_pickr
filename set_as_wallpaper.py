import subprocess

def set_wallpaper(filename):
    # change this bit if you use a different window manager (see below)
    set_wallpaper_gnome(filename)

def set_wallpaper_gnome(filename):
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", filename])

def set_wallpaper_mac(filename):
    raise NotImplementedError()

