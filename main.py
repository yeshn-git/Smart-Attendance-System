import cv2
import face_recognition
import pickle
import numpy as np
from mark_attendance import mark_present 

# --- CONFIG ---
ENCODING_FILE = "encodings.pickle"

def start_recognition(subject_name):
    print("--- LOADING BRAIN ---")
    # 1. Load the known faces
    try:
        file = open(ENCODING_FILE, "rb")
        data = pickle.load(file)
        file.close()
        known_encodings = data["encodings"]
        known_names = data["names"]
        print("✅ Models loaded successfully.")
    except:
        print("❌ Error: Could not load encodings. Did you run train_faces.py?")
        return

    # 2. Open Camera
    print("--- STARTING CAMERA ---")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to 1/4 size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # 3. Find all faces in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        # 4. Compare with known faces
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            
            # Find the best match index
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                    
                    # If we recognize them, mark attendance!
                    mark_present(name, subject_name) 

            # 5. Draw a box around the face
            top, right, bottom, left = face_location
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # Draw name
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        cv2.imshow("Smart Attendance System", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_recognition()