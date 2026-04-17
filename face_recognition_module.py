import face_recognition

def encode_face(image_path):
    """Encodes the face from the image provided."""
    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)
    return encoding[0] if encoding else None

def detect_faces(image_path):
    """Detects faces in the image provided."""
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

def compare_faces(known_face_encoding, test_face_encoding):
    """Compares known face encoding with test face encoding."""
    results = face_recognition.compare_faces([known_face_encoding], test_face_encoding)
    return results[0] if results else False
