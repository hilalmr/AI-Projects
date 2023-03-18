import cv2
from playsound import playsound

# Load the Haar cascade for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Set up the camera capture
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Play the alarm sound
        playsound('alarm.wav')

        # Save the detected face as a PNG image
        cv2.imwrite('face.png', frame[y:y+h, x:x+w])

    # Display the frame
    cv2.imshow('Frame', frame)

    # Check for a key press
    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to quit
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
