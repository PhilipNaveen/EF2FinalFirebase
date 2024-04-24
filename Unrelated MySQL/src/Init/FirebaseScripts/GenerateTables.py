import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json")

try:
    app = firebase_admin.get_app("toydb_app")
except ValueError:
    app = firebase_admin.initialize_app(cred, name="toydb_app")

db = firestore.client(app)

# Create a document in the 'cameras' collection
cameras_ref = db.collection('cameras').document()
cameras_ref.set({
    'id': 1,
    'serial_no': '123456',
    'location_short': 'Location short description',
    'location_long': 'Location long description',
    'created_at': firestore.SERVER_TIMESTAMP
})

# Create a document in the 'rawmetrics' collection
rawmetrics_ref = db.collection('rawmetrics').document()
rawmetrics_ref.set({
    'id': 1,
    'source': 'Source',
    'serial_no': '123456',
    'occupancy': 10,
    'count_in': 5,
    'count_out': 5,
    'source_unixtime': 1615894140,
    'created_at': firestore.SERVER_TIMESTAMP
})

# Create a document in the 'rawmetrics_occupancy' collection
rawmetrics_occupancy_ref = db.collection('rawmetrics_occupancy').document()
rawmetrics_occupancy_ref.set({
    'id': 1,
    'serial_no': '123456',
    'occupancy': 10,
    'total_in': 5,
    'total_out': 5,
    'date': '2024-04-24',
    'time': '09:09:48',
    'day': 'Wednesday',
    'dow': 'Wed'
})

# Create a document in the 'rawmetrics_sum' collection
rawmetrics_sum_ref = db.collection('rawmetrics_sum').document()
rawmetrics_sum_ref.set({
    'id': 1,
    'serial_no': '123456',
    'count_in': 5,
    'count_out': 5,
    'date': '2024-04-24',
    'time': '09:09:48',
    'day': 'Wednesday',
    'dow': 'Wed'
})
