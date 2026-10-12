import cv2
import numpy as np

# 嘗試匯入 MediaPipe 相關模組
try:
    from mediapipe.python.solutions import hands as mp_hands
    from mediapipe.python.solutions import drawing_utils as mp_drawing
except ImportError:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

# ==========================================
# 1. 設定你的測試圖片路徑
# ==========================================
image_path = r"C:\Users\jimmy\Downloads\thumb.jpg" 

# 2. 初始化手部偵測模型
hands_detector = mp_hands.Hands(
    static_image_mode=True,       # 辨識靜態圖片設為 True
    max_num_hands=2,              # 辨識圖片中的手數
    min_detection_confidence=0.5  # 偵測信心水準
)

def recognize_gesture(landmarks):
    """
    根據 21 個手部關鍵點座標判斷簡單手勢
    """
    fingers_extended = []
    
    # 食指到小指 (尖端與第一關節的 Y 軸比較)
    tip_ids = [8, 12, 16, 20]
    pip_ids = [6, 10, 14, 18]
    
    for tip, pip in zip(tip_ids, pip_ids):
        # Y 軸座標越小代表位置越高
        if landmarks[tip].y < landmarks[pip].y:
            fingers_extended.append(True)
        else:
            fingers_extended.append(False)
            
    # 判斷手勢邏輯
    if all(fingers_extended):
        return "Open Hand (Five)"
    
    if fingers_extended[0] and fingers_extended[1] and not fingers_extended[2] and not fingers_extended[3]:
        return "V Sign (Peace)"
    
    if not any(fingers_extended):
        if landmarks[4].y < landmarks[3].y and landmarks[4].y < landmarks[2].y:
            return "Thumbs Up"
        return "Fist"
        
    return "Unknown Gesture"

# ==========================================
# 3. 讀取並縮放圖片
# ==========================================
image = cv2.imread(image_path)

if image is None:
    print(f"無法讀取圖片檔案：{image_path}，請檢查檔案是否存在或路徑是否正確。")
    exit()

# 【新增】自動縮放過大的圖片，避免顯示超出螢幕
max_dimension = 1000  # 限制最大寬或高不超過 1000 像素
h, w = image.shape[:2]
if max(h, w) > max_dimension:
    scale = max_dimension / max(h, w)
    new_w = int(w * scale)
    new_h = int(h * scale)
    image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    print(f"圖片過大，已自動等比例縮放至: {new_w}x{new_h}")

# 將 BGR 轉為 RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 執行 MediaPipe 手部偵測
results = hands_detector.process(rgb_image)

# ==========================================
# 4. 辨識與結果視覺化
# ==========================================
processed_image = image.copy() # 建立一個複製本來畫圖

if results.multi_hand_landmarks:
    print(f"在圖片中偵測到 {len(results.multi_hand_landmarks)} 隻手：")
    for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
        # 1. 辨識手勢
        gesture_text = recognize_gesture(hand_landmarks.landmark)
        print(f"  - 手 #{i+1}: {gesture_text}")

        # 2. 在複製的圖片上繪製骨架與節點
        mp_drawing.draw_landmarks(
            processed_image, hand_landmarks, mp_hands.HAND_CONNECTIONS
        )
        
        # 3. 若是多隻手，稍微錯開文字位置
        y_offset = i * 40
        
        # 4. 在畫面上顯示辨識結果文字
        cv2.putText(
            processed_image, f"Hand #{i+1}: {gesture_text}", (20, 50 + y_offset),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA
        )
else:
    print("圖片中沒有偵測到手。")
    cv2.putText(
        processed_image, "No Hand Detected", (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA
    )

# 顯示辨識結果圖片視窗
cv2.imshow('Hand Gesture Recognition (Image)', processed_image)

print("按任意鍵關閉圖片視窗...")
cv2.waitKey(0)
cv2.destroyAllWindows()