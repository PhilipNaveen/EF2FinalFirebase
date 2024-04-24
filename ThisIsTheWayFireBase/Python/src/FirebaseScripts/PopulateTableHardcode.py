import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json")

try:
    app = firebase_admin.get_app("toydb_app")
except ValueError:
    app = firebase_admin.initialize_app(cred, name="toydb_app")

db = firestore.client(app)


# Function to populate documents in Firestore
def populate_firestore(collection_name, data):
    collection_ref = db.collection(collection_name)
    for row in data:
        doc_ref = collection_ref.document()
        doc_ref.set(row)

# Data hardcoded
cameras_data = [
    {"id": 1, "serial_no": "ACCC8EF6B105", "location_short": "Science & Engineering", "location_long": "SEL Main Entry C120", "created_at": "2023-10-16 13:08:26"},
    {"id": 2, "serial_no": "ACCC8EF8C88D", "location_short": "Science & Engineering", "location_long": "SEL Lower Level Stairwell C054", "created_at": "2023-10-16 13:08:26"},
    {"id": 3, "serial_no": "ACCC8EF02852", "location_short": "Science & Engineering", "location_long": "SEL Room C220", "created_at": "2023-10-16 13:08:26"},
    {"id": 4, "serial_no": "ACCC8EF03315", "location_short": "Science & Engineering", "location_long": "SEL Room C210", "created_at": "2023-10-16 13:08:26"},
    {"id": 5, "serial_no": "B8A44F4F195D", "location_short": "Science & Engineering", "location_long": "SEL Room C200", "created_at": "2023-10-16 13:08:26"},
    {"id": 6, "serial_no": "ACCC8EF0C7E4", "location_short": "Science & Engineering", "location_long": "SEL Upper Level Stairwell C150", "created_at": "2023-10-16 13:08:26"},
    {"id": 7, "serial_no": "ACCC8EF0C2F1", "location_short": "Science & Engineering", "location_long": "SEL Upper Level Stairwell C141", "created_at": "2023-10-16 13:08:26"},
    {"id": 8, "serial_no": "ACCC8EF0C7F2", "location_short": "Science & Engineering", "location_long": "SEL Upper Level Stairwell C152", "created_at": "2023-10-16 13:08:26"}
]

rawmetrics_data = [
    {"id": 1003631, "source": "sum", "serial_no": "ACCC8EF02852", "occupancy": 0, "count_in": 41, "count_out": 24, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003632, "source": "sum", "serial_no": "ACCC8EF03315", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003633, "source": "sum", "serial_no": "B8A44F4F195D", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003634, "source": "sum", "serial_no": "ACCC8EF6B105", "occupancy": 5, "count_in": 21, "count_out": 15, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003635, "source": "sum", "serial_no": "ACCC8EF8C88D", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003636, "source": "sum", "serial_no": "ACCC8EF0C7E4", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003637, "source": "sum", "serial_no": "ACCC8EF0C2F1", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"},
    {"id": 1003638, "source": "sum", "serial_no": "ACCC8EF0C7F2", "occupancy": 0, "count_in": 0, "count_out": 0, "source_unixtime": 1684972824, "created_at": "2023-10-16 14:16:48"}
]

rawmetrics_occupancy_data = [
    {"id": 1003631, "serial_no": "ACCC8EF6B105", "occupancy": 5, "total_in": 206, "total_out": 201, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003632, "serial_no": "B8A44F4F195D", "occupancy": 0, "total_in": 0, "total_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003633, "serial_no": "ACCC8EF0C7E4", "occupancy": 0, "total_in": 0, "total_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003634, "serial_no": "ACCC8EF0C2F1", "occupancy": 0, "total_in": 0, "total_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003635, "serial_no": "ACCC8EF0C7F2", "occupancy": 0, "total_in": 0, "total_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3}
]

rawmetrics_sum_data = [
    {"id": 1003631, "serial_no": "ACCC8EF02852", "count_in": 41, "count_out": 24, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003632, "serial_no": "ACCC8EF03315", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003633, "serial_no": "B8A44F4F195D", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003634, "serial_no": "ACCC8EF6B105", "count_in": 21, "count_out": 15, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003635, "serial_no": "ACCC8EF8C88D", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003636, "serial_no": "ACCC8EF0C7E4", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003637, "serial_no": "ACCC8EF0C2F1", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3},
    {"id": 1003638, "serial_no": "ACCC8EF0C7F2", "count_in": 0, "count_out": 0, "date": "2023-05-24", "time": "20:00:24", "day": "Wednesday", "dow": 3}
]

# Populate Firestore collections
populate_firestore("cameras", cameras_data)
populate_firestore("rawmetrics", rawmetrics_data)
populate_firestore("rawmetrics_occupancy", rawmetrics_occupancy_data)
populate_firestore("rawmetrics_sum", rawmetrics_sum_data)
