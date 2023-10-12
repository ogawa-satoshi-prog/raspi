# 2023/06/06
# スイッチを押して押して

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

pin = 18
led = 23

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する
GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_UP)

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
GPIO.setup(led, GPIO.OUT)

try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        GPIO.wait_for_edge(pin, GPIO.FALLING)# 電圧が下がったとき
        print("ON")
        GPIO.output(led, GPIO.HIGH)
        GPIO.wait_for_edge(pin, GPIO.RISING)
        print("OFF")
        GPIO.output(led, GPIO.LOW)


except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放