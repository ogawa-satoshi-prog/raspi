# 2023/04/25
# LEDを２つ点灯させるプログラム

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

ledPin1 = 23 # LEDの出力箇所を指定
ledPin2 = 24 # スイッチの入力箇所指定

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)

timer = 2
try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        ### 処理を記述 ###（インデント大事）
        GPIO.output(ledPin1, GPIO.HIGH)
        GPIO.output(ledPin2, GPIO.LOW)
        time.sleep(timer)
        GPIO.output(ledPin2, GPIO.HIGH)
        GPIO.output(ledPin1, GPIO.LOW)
        time.sleep(timer)
        


except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放