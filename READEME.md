# some functions for personal use

## function 1. use pyppteer and chronium to detect reflected-xss

1. 安装chronium headless  
环境：centos 7
```
# 安装环境依赖
yum install -y ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils
xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc pango.x86_64
libXcomposite.x86_64 libXcursor.x86_64 libXdamage.x86_64 libXext.x86_64 libXi.x86_64
libXtst.x86_64 cups-libs.x86_64 libXScrnSaver.x86_64 libXrandr.x86_64 GConf2.x86_64 alsalib.
x86_64 atk.x86_64 gtk3.x86_64
```

下载安装chronium
chromium\575458
```
git clone https://github.com/scheib/chromium-latest-linux
cd chromium-latest-linux
./update.sh
nohup ./latest/chrome --headless --disable-gpu --remote-debugging-port=9222 --remote-debugging-address=0.0.0.0 --disable-web-security --disable-xss-auditor --no-sandbox --disable-setuid-sandbox &
```