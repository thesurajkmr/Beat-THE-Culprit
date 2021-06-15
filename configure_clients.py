from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from firebaseconfiguration import firebase_configuration
from twilio.rest import Client


def configure_face_client():
    face_client = FaceClient("https://beattheculprits.cognitiveservices.azure.com/",
                             CognitiveServicesCredentials("8e7f8b81cb1c44fdba666fae65525a46"))
    return face_client


def configure_firebase():
    firebase_configuration()


def configure_twilio_sms_client():
    account_sid = "AC941f338a2b12a4c49c8bee2e0053561" 
    auth_token = "9908a14b1d8b845eb0dc9df5e882f002"
    sms_client = Client(account_sid, auth_token)
    return sms_client
