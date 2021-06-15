from firebaseconfiguration import get_name_from_id


def send_text_to_authority(sms_client, azure_face_id):
    name = get_name_from_id(azure_face_id)
    print("CRIMINAL DETECTED : {} ".format(name))
    sms_client.messages \
        .create(
        body="CRIMINAL DETECTED : {}".format(name),
        from_="+12058758472",
        to="+91 9580XXXXXX")
