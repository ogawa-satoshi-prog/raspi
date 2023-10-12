# 2023/05/09
# PWM(Pulse With Modulation)制御
# 5秒間点滅

import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要
import sys

pin = 18
# ledPin2 = 24 # スイッチの入力箇所指定

### GPIOのピンを指定する方法 ###
GPIO.setmode(GPIO.BCM) #GPIOの番号で指定する

### ピンのセットアップ（指定用途の確定） ###
# LEDピンの出力
GPIO.setup(pin, GPIO.OUT)

#PWMの設定
Led = GPIO.PWM(pin, 10)         #GPIO.PWM(ポート番号, 周波数[Hz])

#初期化処理
Led.start(0)                        #PWM信号0%出力
bright = 0                          #変数"bright"に0を代入

while True:
    try:
        # 繰り返し処理を行うコード
        Led.ChangeDutyCycle(bright)    #PWM信号出力(デューティ比は変数"bright")
        time.sleep(5)               #0.05秒間待つ
        bright += 1                    #変数"bright"を+1
    except KeyboardInterrupt:               #Ctrl+Cキーが押された
        GPIO.cleanup()                      #GPIOをクリーンアップ
        sys.exit()                          #プログラムを終了