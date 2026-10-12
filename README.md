# OpenCV & MediaPipe Hand Gesture Recognition

這是一個基於 Python、OpenCV 與 MediaPipe 實作的即時手勢辨識專案。本專案支援攝影機即時串流、影片檔與靜態圖片處理，透過 MediaPipe 擷取手部 21 個 3D 關鍵點座標，並運用幾何邏輯進行高效率的手勢判定，適合作為電腦視覺與邊緣運算應用的入門作品。

---

## 🚀 功能特色

- **多種輸入模式**：
  - **Webcam 即時串流**：支援電腦內建或外接攝影機進行即時手勢辨識。
  - **影片檔案**：支援主流格式（如 `.mp4`）的影片檔分析。
  - **靜態圖片**：支援 `.jpg`、`.png` 等格式的單張圖片檢測。
- **高精度關鍵點偵測**：整合 Google MediaPipe 機器學習模型，精準標記並繪製手部 21 個 3D 關節與骨架連線。
- **基礎手勢邏輯判定**：
  - 開掌 (`Open Hand / Five`)
  - V 手勢 / 和平手勢 (`V Sign / Peace`)
  - 比讚 (`Thumbs Up`)
  - 拳頭 (`Fist`)
- **畫面自適應調整**：自動等比例縮放過大的輸入畫面，確保顯示視窗完美貼合螢幕尺寸。

---

## 🛠️ 環境需求與安裝步驟

建議在 Windows 環境下透過 Anaconda 建立乾淨的虛擬環境以避免套件衝突：

### 1. 建立並啟動虛擬環境
打開終端機（Terminal / PowerShell），執行以下指令建立名為 `cv_env` 的 Python 3.10 環境：
```bash
conda create -n cv_env python=3.10 -y
conda activate cv_env