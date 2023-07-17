import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smartattendancesystem-76038-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "18700320009":
        {
            "name": "Ritam Majumder",
            "dept": "ECE",
            "starting_year": 2020,
            "total_attendance": 7,
            #"standing": "G",
            "year": 3,
            "phone": "+918017483866",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "18700320014":
        {
            "name": "Hrishav Karmakar",
            "dept": "ECE",
            "starting_year": 2020,
            "total_attendance": 12,
            #"standing": "B",
            "year": 3,
            "phone": "+916290120690",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "18700320050":
        {
            "name": "Jyotirmoy Biswas",
            "dept": "ECE",
            "starting_year": 2020,
            "total_attendance": 7,
            #"standing": "G",
            "year": 3,
            "phone": "+919735181682",
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "18701320010":
        {
            "name": "Debanjan Paul",
            "dept": "ECE",
            "starting_year": 2020,
            "total_attendance": 3,
            #"standing": "G",
            "year": 3,
            "phone": "+918837209106",
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)