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


sudo apt install cmake libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev gstreamer1.0-tools libgtk2.0-dev gstreamer1.0-omx=1.0.0.1-0+rpi12+jessiepmg gstreamer1.0-plugins-bad gstreamer1.0-plugins-good
mkdir OpenCV && cd OpenCV
wget https://github.com/opencv/opencv/archive/4.2.0.zip
unzip 4.2.0.zip
cd opencv-4.2.0
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -DINSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=ON -D　PYTHON_EXECUTABLE=/usr/bin/python3 -D BUILD_EXAMPLES=ON -D WITH_GTK=ON -D WITH_GSTREAMER=ON -D WITH_FFMPEG=OFF -D WITH_QT=OFF ..
make -j4
sudo make install
