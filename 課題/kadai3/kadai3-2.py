# 2023/07/20
# 人感センサーで反応した時にLEDを変化

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

pin = 18 #人感センサのgpioに使用するポート番号
LED1 = 23
LED2 = 24

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する
GPIO.setup(pin, GPIO.IN)

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        if(GPIO.input(pin) == GPIO.HIGH):
            print("反応あり")
            GPIO.output(LED1, GPIO.HIGH)
            GPIO.output(LED2, GPIO.LOW)
        else:
            print("反応なし")
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放