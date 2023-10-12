import sys
import time
import RPi.GPIO as GPIO
 
 
# ボタンは"GPIO5"に接続
BUTTON = 5
pin = 18
LED1 = 23
LED2 = 24
FLG = 0
 
# 主処理
def main():
    try:
        # 操作対象のピンは「GPIOn」の"n"を指定する
        GPIO.setmode(GPIO.BCM)
        # BUTTONがつながるGPIOピンの動作は「入力」「プルアップあり」
        GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # 人感センサピンの出力
        GPIO.setup(pin, GPIO.IN)

        # LEDピンの出力
        GPIO.setup(LED1, GPIO.OUT)
        GPIO.setup(LED2, GPIO.OUT)

        # 立ち下がり（GPIO.FALLING）を検出する（プルアップなので通常時1／押下時0）
        GPIO.add_event_detect(BUTTON, GPIO.FALLING, bouncetime=200)
        # イベント発生時のコールバック関数を登録
        GPIO.add_event_callback(BUTTON, button_pressed)
         
        # 無限ループ
        while True:
            # 主処理
            if FLG == 1:
                if(GPIO.input(pin) == GPIO.HIGH):
                    print("反応あり")
                    GPIO.output(LED1, GPIO.HIGH)
                    GPIO.output(LED2, GPIO.LOW)
                else:
                    print("反応なし")
                    GPIO.output(LED1, GPIO.LOW)
                    GPIO.output(LED2, GPIO.HIGH)
            else:
                pass
            time.sleep(1)
         
    # キーボード割り込みを捕捉
    except KeyboardInterrupt:
        print("例外'KeyboardInterrupt'を捕捉")
     
    print("処理を終了します")
     
    # GPIOの設定をリセット
    GPIO.cleanup()
     
    return 0
 
 
# ボタンＡが押された時に呼び出されるコールバック関数
# gpio_no: イベントの原因となったGPIOピンの番号
def button_pressed(gpio_no):
    global FLG
    sw = GPIO.input(gpio_no)
    if sw == 0:
        if FLG == 0:
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW)
            FLG = 1
        else:
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.LOW)
            FLG = 0
 
 
if __name__ == "__main__":
    sys.exit(main())