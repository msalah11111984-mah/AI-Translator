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

# دع النظام يختار أحدث إصدار مستقر متاح تلقائياً لمنع خطأ الـ 404
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
[buildozer]
log_level = 2
warn_on_root = 1
