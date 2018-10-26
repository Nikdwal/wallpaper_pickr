import subprocess
from sys import stderr
from os import path

def set_wallpaper(filename):
    f = choose_wallpaper_setter()
    f(filename)

# returns the function that can edit the file name
# This function corresponds to the window manager entered in winmgr.conf
def choose_wallpaper_setter():
    conf_file_rel = "winmgr.conf"
    conf_file     = path.join(path.dirname(path.abspath(__file__)), conf_file_rel)
    with open(conf_file, "r") as f:
        winmgr = None
        for line in f:
            if line.strip() and line[0] != "#":
                winmgr = line
                break
        if winmgr is None:
            print("Please enter the name of your window manager in the file " + conf_file_rel + ".", file=stderr)
            exit(1)

    winmgr = winmgr.lower().replace("\n","")
    if winmgr == "macos":
        func = set_wallpaper_mac
    elif winmgr == "gnome":
        func = set_wallpaper_gnome
    elif winmgr == "plasma":
        func = set_wallpaper_plasma
    else:
        print("Your window manager is not supported.", file=stderr)
        exit(1)
    return func

def set_wallpaper_gnome(filename):
    subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", filename])

def set_wallpaper_mac(filename):
    subprocess.call(["osascript", "-e", "tell application \"Finder\" to set desktop picture to POSIX file \"" + filename + "\""])

def set_wallpaper_plasma(filename):
    subprocess.call(["qdbus", "org.kde.plasmashell", "/PlasmaShell", "org.kde.PlasmaShell.evaluateScript", """
    var allDesktops = desktops();
    for (i=0;i<allDesktops.length;i++) {{
        d = allDesktops[i];
        d.wallpaperPlugin = "org.kde.image";
        d.currentConfigGroup = Array("Wallpaper",
                                     "org.kde.image",
                                     "General");
        d.writeConfig("Image", "file:///""" + filename + """\")
    }}
    """])
