# 2023/06/20

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

pin = 18

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する
GPIO.setup(pin, GPIO.IN)

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
# GPIO.setup(led, GPIO.OUT)

try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        if(GPIO.input(pin) == GPIO.HIGH):
            print("反応あり")
        else:
            print("反応なし")
        time.sleep(1)

except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放