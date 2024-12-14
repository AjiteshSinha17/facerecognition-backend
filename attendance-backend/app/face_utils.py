import face_recognition
import os
import pickle

REGISTERED_FACES_DIR = "registered_faces"
if not os.path.exists(REGISTERED_FACES_DIR):
    os.makedirs(REGISTERED_FACES_DIR)

def register_face(name, file):
    file_path = os.path.join(REGISTERED_FACES_DIR, f"{name}.jpg")
    file.save(file_path)

    image = face_recognition.load_image_file(file_path)
    encoding = face_recognition.face_encodings(image)

    if encoding:
        with open(file_path.replace('.jpg', '.pkl'), 'wb') as f:
            pickle.dump(encoding[0], f)
        return {"message": f"{name} registered successfully!", "status": 200}
    else:
        os.remove(file_path)
        return {"error": "Failed to register face!", "status": 400}

def recognize_face(file):
    image = face_recognition.load_image_file(file)
    unknown_encoding = face_recognition.face_encodings(image)

    if unknown_encoding:
        unknown_encoding = unknown_encoding[0]

        for file_name in os.listdir(REGISTERED_FACES_DIR):
            if file_name.endswith('.pkl'):
                with open(os.path.join(REGISTERED_FACES_DIR, file_name), 'rb') as f:
                    known_encoding = pickle.load(f)
                
                if face_recognition.compare_faces([known_encoding], unknown_encoding)[0]:
                    name = file_name.replace('.pkl', '')
                    return {"message": f"Attendance marked for {name}!", "status": 200}

        return {"error": "Face not recognized!", "status": 400}
    else:
        return {"error": "No face found in the image!", "status": 400}
