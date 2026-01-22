import cv2
import face_recognition
import os
import pickle

# --- CONFIG ---
IMAGE_FOLDER = "student_images"
ENCODING_FILE = "encodings.pickle"

def find_encodings():
    print("--- STARTING TRAINING ---")
    known_encodings = []
    known_names = []

    # Loop through every file in the student_images folder
    if not os.path.exists(IMAGE_FOLDER):
        print(f"❌ Error: Folder '{IMAGE_FOLDER}' not found.")
        return

    files = os.listdir(IMAGE_FOLDER)
    print(f"Found {len(files)} images to process...")

    for file_name in files:
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            path = os.path.join(IMAGE_FOLDER, file_name)
            
            # 1. Load the image
            img = cv2.imread(path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Library expects RGB, not BGR

            # 2. Find the face in the image
            boxes = face_recognition.face_locations(rgb_img, model="hog")
            
            if len(boxes) > 0:
                # 3. Encode the face (Turn it into numbers)
                encoding = face_recognition.face_encodings(rgb_img, boxes)[0]
                
                # Save the result
                student_id = os.path.splitext(file_name)[0] # Removes ".jpg"
                known_encodings.append(encoding)
                known_names.append(student_id)
                print(f"✅ Trained on: {student_id}")
            else:
                print(f"⚠️ Warning: No face found in {file_name}. Skipping.")

    # 4. Saving everything to a file
    print("--- SAVING DATA ---")
    data = {"encodings": known_encodings, "names": known_names}
    f = open(ENCODING_FILE, "wb")
    pickle.dump(data, f)
    f.close()
    print(f"✅ Training Complete. Data saved to '{ENCODING_FILE}'")

if __name__ == "__main__":
    find_encodings()