import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def firebase_configuration():
    cred = credentials.Certificate('beattheculprit-firebase-adminsdk-ybiog-88e37adb98.json')
    firebase_admin.initialize_app(cred)


def get_name_from_id(azure_face_id):
    name_obj = firestore.client().collection(u'criminals').document(azure_face_id).get()
    if name_obj.exists:
        return name_obj.to_dict()['name']
    else:
        return 'no name found for this id'



