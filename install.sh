#!/usr/bin/env sh

mkdir -p ~/.local/bin \
         ~/.config/autostart \
         ~/.local/share/backgrounds/BitDay

set -- 01-Early-Morning.png \
       02-Mid-Morning.png \
       03-Late-Morning.png \
       04-Early-Afternoon.png \
       05-Mid-Afternoon.png \
       06-Late-Afternoon.png \
       07-Early-Evening.png \
       08-Mid-Evening.png \
       09-Late-Evening.png \
       10-Early-Night.png \
       11-Mid-Night.png \
       12-Late-Night.png

echo "[1/4] Downloading wallpapers..."
for i in "$@"
do
    if [ ! -f ~/.local/share/backgrounds/BitDay/$i ]; then
        curl -sSL "https://github.com/queeup/bitday-wallpaper-changer/raw/main/wallpapers/$i" --output ~/.local/share/backgrounds/BitDay/$i
    fi
done

echo "[2/4] Installing files..."
curl -sSL "https://github.com/queeup/bitday-wallpaper-changer/raw/main/bitday-wallpaper-changer.py" --output ~/.local/bin/bitday-wallpaper-changer.py
curl -sSL "https://github.com/queeup/bitday-wallpaper-changer/raw/main/bitday-wallpaper-changer.desktop" --output ~/.config/autostart/bitday-wallpaper-changer.desktop

echo "[3/4] Starting bitday-wallpaper-changer..."
chmod +x ~/.local/bin/bitday-wallpaper-changer.py
~/.local/bin/bitday-wallpaper-changer.py &

echo "[4/4] Done."