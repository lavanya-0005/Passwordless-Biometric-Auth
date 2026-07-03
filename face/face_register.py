import os
import base64
import pickle
import numpy as np
import cv2
import face_recognition

os.makedirs("face_data", exist_ok=True)


def register_face(username, image_data):

    username = username.strip()

    if username == "":
        return False

    try:

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

        encoding = face_recognition.face_encodings(
            rgb,
            locations
        )[0]

        with open(
            f"face_data/{username}.pkl",
            "wb"
        ) as file:

            pickle.dump(
                encoding,
                file
            )

        print("Face Registered Successfully")

        return True

    except Exception as e:

        print("Face Register Error:", e)

        return False