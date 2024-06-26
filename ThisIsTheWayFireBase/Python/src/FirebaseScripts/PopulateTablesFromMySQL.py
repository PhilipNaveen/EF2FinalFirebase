# Written by Philip Naveen, Arathi Ponneth, and Athira Ponneth

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("src/content/KeyFirebaseThisIsTheWay.json")

try:
    app = firebase_admin.get_app("thisistheway_app")
except ValueError:
    app = firebase_admin.initialize_app(cred, name="thisistheway_app")
    
    
# If we don't want to edit the room's at all, and only want to edit the ToyDB
# ToyDB is our tester database (hosted on both MySQL and NoSQL, soon MongoDB as well)     
    
"""   
cred = credentials.Certificate("src/content/KeyFirebaseToyDB.json")

try:
    app = firebase_admin.get_app("toydb_app")
except ValueError:
    app = firebase_admin.initialize_app(cred, name="toydb_app")

db = firestore.client(app)
"""

# Connect to MySQL database
mysql_conn = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="occupancy"
)
mysql_cursor = mysql_conn.cursor(dictionary=True)

# Function to convert MySQL date and time to Firestore timestamp
def convert_to_firestore_timestamp(date_str, time_str):
    return firestore.SERVER_TIMESTAMP

# Populate 'cameras' collection
mysql_cursor.execute("SELECT * FROM cameras")
cameras_data = mysql_cursor.fetchall()
for camera in cameras_data:
    camera_ref = db.collection('cameras').document()
    camera_ref.set({
        'id': camera['id'],
        'serial_no': camera['serial_no'],
        'location_short': camera['location_short'],
        'location_long': camera['location_long'],
        'created_at': convert_to_firestore_timestamp(camera['created_at'], None)
    })

# Populate 'rawmetrics' collection
mysql_cursor.execute("SELECT * FROM rawmetrics")
rawmetrics_data = mysql_cursor.fetchall()
for rawmetric in rawmetrics_data:
    rawmetric_ref = db.collection('rawmetrics').document()
    rawmetric_ref.set({
        'id': rawmetric['id'],
        'source': rawmetric['source'],
        'serial_no': rawmetric['serial_no'],
        'occupancy': rawmetric['occupancy'],
        'count_in': rawmetric['count_in'],
        'count_out': rawmetric['count_out'],
        'source_unixtime': rawmetric['source_unixtime'],
        'created_at': convert_to_firestore_timestamp(rawmetric['created_at'], None)
    })

# Populate 'rawmetrics_occupancy' collection
mysql_cursor.execute("SELECT * FROM rawmetrics_occupancy")
rawmetrics_occupancy_data = mysql_cursor.fetchall()
for rawmetric_occupancy in rawmetrics_occupancy_data:
    rawmetric_occupancy_ref = db.collection('rawmetrics_occupancy').document()
    rawmetric_occupancy_ref.set({
        'id': rawmetric_occupancy['id'],
        'serial_no': rawmetric_occupancy['serial_no'],
        'occupancy': rawmetric_occupancy['occupancy'],
        'total_in': rawmetric_occupancy['total_in'],
        'total_out': rawmetric_occupancy['total_out'],
        'date': rawmetric_occupancy['date'],
        'time': rawmetric_occupancy['time'],
        'day': rawmetric_occupancy['day'],
        'dow': rawmetric_occupancy['dow']
    })

# Populate 'rawmetrics_sum' collection
mysql_cursor.execute("SELECT * FROM rawmetrics_sum")
rawmetrics_sum_data = mysql_cursor.fetchall()
for rawmetric_sum in rawmetrics_sum_data:
    rawmetric_sum_ref = db.collection('rawmetrics_sum').document()
    rawmetric_sum_ref.set({
        'id': rawmetric_sum['id'],
        'serial_no': rawmetric_sum['serial_no'],
        'count_in': rawmetric_sum['count_in'],
        'count_out': rawmetric_sum['count_out'],
        'date': rawmetric_sum['date'],
        'time': rawmetric_sum['time'],
        'day': rawmetric_sum['day'],
        'dow': rawmetric_sum['dow']
    })

# Close MySQL connection
mysql_cursor.close()
mysql_conn.close()

print("Data population completed.")
