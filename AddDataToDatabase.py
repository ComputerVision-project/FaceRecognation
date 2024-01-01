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
        "email" : "rowida.elsayed@ejust.edu.eg",
        "id" : "120200181",
        "total_attendance":6,
        "year" : 4,
        "Last_attendance_time" : "2023-12-07 00:54:34"
    },
     "120200013" :
    {
        "name" : "Rewan Yehia",
        "email" : "rewan.abubakr@ejust.edu.eg",
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
        "name" : "Noha Omar",
        "email" : "noha.abdelaziz@ejust.edu.eg",
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
    "120200028":
        {
            "name": "Ahmed Abdelkader",
            "id": "120200028",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200081":
        {
            "name": "Mohamed Ayman",
            "id": "120200081",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200094":
        {
            "name": "Mariam Ayman",
            "id": "120200094",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200101":
        {
            "name": "Ahmed Hagag",
            "id": "120200094",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200045":
        {
            "name": "Mahmoud Akram",
            "id": "120200045",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200034":
        {
            "name": "Mostafa Atef",
            "id": "120200034",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
     "120200078":
        {
            "name": "Ziad Hesham",
            "id": "120200078",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200095":
        {
            "name": "Arwa Zakaria",
            "id": "120200095",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
     "120200212":
        {
            "name": "Alaa Moheb",
            "id": "120200212",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
     "120200089":
        {
            "name": "Assem Mohamed",
            "id": "120200089",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200090":
        {
            "name": "Youssef Ashraf",
            "id": "120200090",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
     "120190057":
        {
            "name": "Youssef Zaghloul",
            "id": "120190057",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
     "120200144":
        {
            "name": "Nour Elhuda",
            "id": "120200144",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
    "120200039":
        {
            "name": "Abdelrahman Essam",
            "id": "120200039",
            "total_attendance": 6,
            "year": 4,
            "Last_attendance_time": "2023-12-07 00:54:34"
        },
 }

for key, value in data.items():
    ref.child(key).set(value)