import RPi.GPIO as GPIO #GPIOを使うために必要
import time #タイマーを使うために必要

ledPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try: #try~expectでひと固まり
    while True: #無限ループ（基本）
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(5)

except KeyboardInterrupt: #キーボードの入力により処理を判定
    GPIO.cleanup()  # GPIOの解放