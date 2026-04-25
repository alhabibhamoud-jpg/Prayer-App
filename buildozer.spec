[app]

title = Prayer Times
package.name = prayertimes
package.domain = org.example

source.dir = .
source.include_exts = py,ttf,mp3,json

version = 1.0

requirements = python3, kivy==2.3.0, requests, certifi, openssl

orientation = portrait

fullscreen = 0

android.permissions = INTERNET

android.api = 31
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-xxxxxxxx~xxxxxx

[buildozer]

log_level = 2
warn_on_root = 1
