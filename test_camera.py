import cv2

# Initialize the camera (0 is usually the default webcam)
print("Attempting to open camera...")
video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Error: Could not access the camera.")
    exit()

print("Camera opened! Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow('My First Computer Vision Test', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
video_capture.release()
cv2.destroyAllWindows()