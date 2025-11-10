[app]
title = KVTODO
package.name = kvtodo
package.domain = devusimple.inc
source.dir = .
source.include_exts = py, kv, png, jpg, json
version = 1.0
requirements = python3, kivy==2.3.0, kivymd==2.0.1
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 27
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1