# OpenCV & MediaPipe Hand Gesture Recognition

這是一個基於 Python、OpenCV 與 MediaPipe 實作的即時手勢辨識專案。它可以支援即時攝影機輸入、影片檔以及靜態圖片的處理，並透過手部 21 個 3D 關鍵點來進行簡單的手勢邏輯判斷。

## 🚀 功能特色
- 支援 **Webcam 即時串流**、**影片檔案 (.mp4)** 與 **靜態圖片 (.jpg/.png)** 辨識。
- 結合 MediaPipe 進行高精度的 21 個手部關鍵點與骨架繪製。
- 支援多種基礎手勢判斷：
  - 開掌 (Open Hand / Five)
  - V 手勢 (V Sign / Peace)
  - 比讚 (Thumbs Up)
  - 拳頭 (Fist)

## 🛠️ 環境需求與安裝
1. 建立並啟動虛擬環境：
   ```bash
   conda create -n cv_env python=3.10 -y
   conda activate cv_env
2. 安裝必要套件：
   ```bash
   pip install -r requirements.txt
3. 執行python hand_gesture_recognition.py