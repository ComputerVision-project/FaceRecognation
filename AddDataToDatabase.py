import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://facerecognition-159b3-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "120200181" :
    {
        "name" : "Rowida Elsayed",
        "id" : "120200181",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },
     "120200013" :
    {
        "name" : "Rewan Yehia",
        "id" : "120200013",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },
     "120200244" :
    {
        "name" : "Bassant Tarek",
        "email" : "bassant.tarek@ejust.edu.eg",
        "id" : "120200244",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },
     "120200211" :
    {
        "name" : "Noha Mahmoud",
        "id" : "120200211",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },
     "120200067" :
    {
        "name" : "Gasser Amr",
        "email": "gasser.amr@ejust.edu.eg",
        "id" : "120200067",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },

    "120190071":
        {
            "name": "Mario Medhat",
            "id": "120190071",
            "email" : "mario.medhat@ejust.edu.eg",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },

    "120200062":
        {
            "name": "Sohila Kandil",
            "id": "120200062",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },

    "120200027":
        {
            "name": "Ahmed Ali",
            "id": "120200027",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200245":
        {
            "name": "Ahmed Fathy",
            "id": "120200245",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200033":
        {
            "name": "Ahmed Mongy",
            "id": "120200033",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200156":
        {
            "name": "Omnia Nabil",
            "id": "120200156",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
 }

for key, value in data.items():
    ref.child(key).set(value)