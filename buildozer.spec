[app]
title = AI Translator Pro
package.name = aitranslator
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,deep-translator,pyjnius
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.permissions = INTERNET, RECORD_AUDIO

# تثبيت إصدارات مستقرة ومجربة سحابياً لمنع انهيار البناء
android.api = 33
android.minapi = 21
android.ndk = 25.2.9519653
android.ndk_api = 21
android.build_tools_version = 33.0.2

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
[buildozer]
log_level = 2
warn_on_root = 1
