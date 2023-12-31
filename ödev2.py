import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    sonuc = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Orijinal', frame)
    cv2.imshow('Sonuc', sonuc)

    # Çıkış için 'q' tuşuna bas.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
