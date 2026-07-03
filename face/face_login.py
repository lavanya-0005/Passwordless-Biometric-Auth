import os
import base64
import pickle
import numpy as np
import cv2
import face_recognition


def login_face(username, image_data):

    username = username.strip()

    if username == "":
        return False

    filepath = f"face_data/{username}.pkl"

    if not os.path.exists(filepath):
        print("Face not registered.")
        return False

    try:

        with open(filepath, "rb") as file:
            stored_encoding = pickle.load(file)

        # Remove data:image/jpeg;base64,
        image_data = image_data.split(",")[1]

        image_bytes = base64.b64decode(image_data)

        image_array = np.frombuffer(image_bytes, dtype=np.uint8)

        frame = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        locations = face_recognition.face_locations(rgb)

        if len(locations) != 1:
            print("Exactly one face must be visible.")
            return False

        login_encoding = face_recognition.face_encodings(
            rgb,
            locations
        )[0]

        match = face_recognition.compare_faces(
            [stored_encoding],
            login_encoding,
            tolerance=0.5
        )

        distance = face_recognition.face_distance(
            [stored_encoding],
            login_encoding
        )[0]

        print("Face Distance:", distance)

        if match[0]:
            print("Face Login Successful")
            return True

        print("Face Login Failed")
        return False

    except Exception as e:

        print("Face Login Error:", e)
        return False  