def azure_recognisation(face_client, image):
    face_recognition_sucessful = False
    detected_face_id = ""
    try:
        face_ids = []

        # Detect a face in an image that contains a single face

        detected_faces = face_client.face.detect_with_stream(image=image)
        if not detected_faces:
            print("No face has been detected from image")
            return "-1"

        # Display the detected face ID
        print("Detected face ID from:")
        for face in detected_faces:
            print(face.face_id)
            print()
            face_ids.append(face.face_id)

        results = face_client.face.identify(face_ids, "criminal_group")
        if not results:
            print("No photo has been matched")
            return "-1"

        for person in results:
            if float(person.candidates[0].confidence) > 0.50:
                face_recognition_sucessful = True
                detected_face_id = person.candidates[0].person_id
                print(person.candidates[0].confidence)



    except:
        print("error in face recognisation")

    finally:
        if face_recognition_sucessful:
            return detected_face_id
        else:
            return "-1"
