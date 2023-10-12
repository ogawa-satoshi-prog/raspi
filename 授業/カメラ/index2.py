import cv2

# カメラを初期化
cap = cv2.VideoCapture(0)  # カメラデバイスのインデックス（通常は0）を指定

# カメラが正しく初期化されたか確認
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # カメラからフレームを読み込む
        ret, frame = cap.read()

        # フレームの読み込みができたか確認
        if not ret:
            print("Error: Could not read frame.")
            break

        # フレームを表示
        cv2.imshow("Camera", frame)

        # 'q'キーを押すとプログラムを終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # カメラを解放し、ウィンドウを閉じる
    cap.release()
    cv2.destroyAllWindows()
