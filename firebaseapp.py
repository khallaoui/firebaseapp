import json
from pyrebase import pyrebase

import firebase
from firebase_admin import credentials, initialize_app,db
cred = credentials.Certificate("pro2-a899c-firebase-adminsdk-y1zm9-be94d6c86a.json")
app = initialize_app(cred, {

    'databaseURL': 'https://pro2-a899c-default-rtdb.europe-west1.firebasedatabase.app/'
})

re = db.reference("/ETUDIANTS/")
with open(".data.json","r") as write:
    data= json.load(write)

re.set(data)
print("ok")

