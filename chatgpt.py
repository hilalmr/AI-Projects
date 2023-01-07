import cv2
import pyautogui

# Load the cascade
hand_cascade = cv2.CascadeClassifier('hand.xml')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray)

    # Check if a hand is detected
    if len(hands) > 0:
        # Calculate the area of the hand
        hand = hands[0]
        x, y, w, h = hand
        area = w * h

        # Use the area to control the volume
        if area > 20000:
            pyautogui.hotkey('volumeup')
        elif area < 10000:
            pyautogui.hotkey('volumedown')

    # Display the frame
    cv2.imshow('frame', frame)

    # Stop the camera if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
