import cv2
import pyautogui
import tkinter as tk

hand_cascade = cv2.CascadeClassifier('hand.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

hands_detected = False # Initialize hands_detected to False
volume_action = 'increase' # Initialize volume_action to 'increase'

def start_tracking():
    global hands_detected, volume_action
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
        if len(hands) > 0:
            hands_detected = True
            if volume_action == 'increase':
                pyautogui.press('volumeup')
            else:
                pyautogui.press('volumedown')
            for (x, y, w, h) in hands:
                # Set circle color based on volume action
                if volume_action == 'increase':
                    circle_color = (0, 255, 0) # Green
                else:
                    circle_color = (0, 0, 255) # Red

                # Draw circle around hand
                cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+h)/4), circle_color, 2)
                # Draw circle inside hand
                cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+h)/8), circle_color, 2)
                # Add text inside hand
                if volume_action == 'increase':
                    cv2.putText(frame, 'Increasing Volume', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circle_color, 2)
                    print("\033[32mIncreasing Volume\033[0m")

                else:
                    cv2.putText(frame, 'Decreasing Volume', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, circle_color, 2)
                    print("\033[31mDecreasing Volume\033[0m")

        else:
            if hands_detected:
                hands_detected = False
                volume_action = 'decrease' if volume_action == 'increase' else 'increase'
                # Toggle volume action between 'increase' and 'decrease'

        cv2.imshow('AI Volume APP', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def stop_tracking():
    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()

start_button = tk.Button(root, text="Start Tracking", command=start_tracking)
start_button.pack(side="left")

stop_button = tk.Button(root, text="Stop Tracking", command=stop_tracking)
stop_button.pack(side="left")

root.mainloop()
