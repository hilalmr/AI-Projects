import cv2
import pyautogui

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)

hands_detected = False # Initialize hands_detected to False

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    if len(hands) > 0:
        hands_detected = True
        pyautogui.press('volumeup')
        for (x, y, w, h) in hands:
            # Draw circle around hand
            cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+h)/4), (0, 255, 0), 2)
            # Draw circle inside hand
            cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+h)/8), (0, 255, 0), 2)
            # Add text inside hand
            cv2.putText(frame, 'Increasing Volume', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    else:
        if hands_detected:
            hands_detected = False
           
            
            

    cv2.imshow('Hand Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
