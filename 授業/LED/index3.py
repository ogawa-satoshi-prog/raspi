# 2023/05/09
# PWM(Pulse With Modulation)制御

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

pin = 18
# ledPin2 = 24 # スイッチの入力箇所指定

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
GPIO.setup(pin, GPIO.OUT)

try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        Led = GPIO.PWM(18, 50)#(ポート, 周波数)
        Led.start(70)# 一周期のONの割合(%)
        time.sleep(5)

except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放