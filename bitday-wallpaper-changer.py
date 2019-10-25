#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bitday Wallpaper Changer

Dynamically changing BitDay wallpapers throughout the day

author: queeup at zoho dot com
"""

import os
import subprocess
from time import localtime, sleep, strftime

SHOW_DEBUG = False


def get_gnome_wallpaper():
    get_wallpaper = subprocess.run(
        ["gsettings", "get", "org.gnome.desktop.background", "picture-uri"],
        check=True,
        capture_output=True,
        encoding="utf-8",
    )
    if SHOW_DEBUG:
        print(f"Current Wallpaper: {get_wallpaper.stdout}")
    return get_wallpaper.stdout


def set_gnome_wallpaper(file_path):
    try:
        subprocess.run(
            ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", file_path],
            check=True,
        )
        if SHOW_DEBUG:
            print(f"Setting Wallpaper: {file_path}")
    except subprocess.CalledProcessError as err:
        print("ERROR:", err)


def calculate_background_wallpaper():
    now = strftime("%H:%M", localtime())
    # TODO: Change times accordingly to the link?
    # https://github.com/ghisvail/gnome-backgrounds-bitday/blob/master/backgrounds/bitday-timed.xml.in
    # https://stackoverflow.com/q/26502775/11391913
    if "06:29" < now < "07:30":
        set_background = "01-Early-Morning.png"
    elif "07:29" < now < "10:30":
        set_background = "02-Mid-Morning.png"
    elif "10:29" < now < "11:30":
        set_background = "03-Late-Morning.png"
    elif "11:29" < now < "13:30":
        set_background = "04-Early-Afternoon.png"
    elif "13:29" < now < "15:00":
        set_background = "05-Mid-Afternoon.png"
    elif "14:59" < now < "17:00":
        set_background = "06-Late-Afternoon.png"
    elif "16:59" < now < "18:00":
        set_background = "07-Early-Evening.png"
    elif "17:59" < now < "19:00":
        set_background = "08-Mid-Evening.png"
    elif "18:59" < now < "20:30":
        set_background = "09-Late-Evening.png"
    elif now > "20:29":
        set_background = "10-Early-Night.png"
    elif now < "02:00":
        set_background = "11-Mid-Night.png"
    elif "01:59" < now < "06:30":
        set_background = "12-Late-Night.png"
    else:
        set_background = ""
    return f"'file://{os.environ['HOME']}/.local/share/backgrounds/BitDay/{set_background}'"


def main():
    while True:
        if not get_gnome_wallpaper() == calculate_background_wallpaper():
            if SHOW_DEBUG:
                print("Wallpaper is not same. Changing wallpaper.")
            set_gnome_wallpaper(calculate_background_wallpaper())
        else:
            if SHOW_DEBUG:
                print("Wallpaper is same. Nothing changed.")
        sleep(3)


if __name__ == "__main__":
    main()
