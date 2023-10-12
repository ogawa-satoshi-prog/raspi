# 2023/07/20
# スイッチを押すたびにLED緑→赤→黄（チャタリング対策）

import sys
import time
import datetime
import RPi.GPIO as GPIO
 
 
# ボタンは"GPIO5"に接続
BUTTON = 5
LED1 = 23 #緑
LED2 = 24 #赤
LED3 = 25 #黄色
FLG = 0
 
# 主処理
def main():
     
    try:
        # 操作対象のピンは「GPIOn」の"n"を指定する
        GPIO.setmode(GPIO.BCM)
        # BUTTONがつながるGPIOピンの動作は「入力」「プルアップあり」
        GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
         
        # LEDピンの出力
        GPIO.setup(LED1, GPIO.OUT)
        GPIO.setup(LED2, GPIO.OUT)
        GPIO.setup(LED3, GPIO.OUT)

        # 立ち下がり（GPIO.FALLING）を検出する（プルアップなので通常時1／押下時0）
        GPIO.add_event_detect(BUTTON, GPIO.FALLING, bouncetime=200)
        # イベント発生時のコールバック関数を登録
        GPIO.add_event_callback(BUTTON, button_pressed)
         
        # 無限ループ
        while True:
            # 主処理は何もしない
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
            GPIO.output(LED1, GPIO.HIGH)
            FLG = 1
        elif FLG == 1:
            GPIO.output(LED1, GPIO.LOW)
            GPIO.output(LED2, GPIO.HIGH)
            FLG = 2
        elif FLG == 2:
            GPIO.output(LED2, GPIO.LOW)
            GPIO.output(LED3, GPIO.HIGH)
            FLG = 3
        elif FLG == 3:
            GPIO.output(LED3, GPIO.LOW)
            FLG = 0
    # メッセージを表示
    print_message("ボタンが押されました")
 
 
# ターミナル上に「日付 時刻.マイクロ秒: メッセージ」を表示する関数
# message: 表示する「メッセージ」
def print_message(message):
     
    # 現在の日付時刻を取得して「年-月-日 時:分:秒.マイクロ秒」にフォーマット
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
     
    # 引数で送られたメッセージを表示
    print("{}: {}".format(timestamp, message))
 
 
if __name__ == "__main__":
    sys.exit(main())