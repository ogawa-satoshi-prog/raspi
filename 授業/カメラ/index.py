# 2023/09/26
# カメラモジュール

import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read() # カメラから画像を読み込んでくる
print(frame)
cv2.imshow("frame", frame) # ウィンドウに表示させる
cv2.waitkey(0) # 何かキーが押されるまで待つ
cap.release()
cv2.destoryAllWindows()

#日付を取得
import datetime
dt_now = datetime.datetime.now() # 現在の日時
filename = dt_now.strftime("%Y年%m月%d日%H時%M分%s秒")

# 画像ファイルを書き出す
ret,frame = cap.read()
cv2.imwrite(filename + ".jpg", frame)