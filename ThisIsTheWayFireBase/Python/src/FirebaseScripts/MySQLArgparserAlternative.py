"""
Experimental alternative use for the SQL queries to achieve lower lateny.
Uses argument parser for one large package rather than multiple query calls rather than repeated low latency packages.

"""

import argparse
import mysql.connector
import firebase_admin
from firebase_admin import credentials, firestore

def convert_to_firestore_timestamp(date_str, time_str):
    return firestore.SERVER_TIMESTAMP

def populate_collections(mysql_cursor, db):
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

def main(args):
    cred = credentials.Certificate(args.firebase_key_path)

    try:
        app = firebase_admin.get_app(args.app_name)
    except ValueError:
        app = firebase_admin.initialize_app(cred, name=args.app_name)

    db = firestore.client(app)

    # Connect to MySQL database
    mysql_conn = mysql.connector.connect(
        host=args.mysql_host,
        user=args.mysql_user,
        password=args.mysql_password,
        database=args.mysql_database
    )
    mysql_cursor = mysql_conn.cursor(dictionary=True)

    populate_collections(mysql_cursor, db)

    # Close MySQL connection
    mysql_cursor.close()
    mysql_conn.close()

    print("Data population completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate Firebase collections from MySQL database.")
    parser.add_argument("--firebase_key_path", type=str, help="Path to Firebase key JSON file")
    parser.add_argument("--app_name", type=str, default="thisistheway_app", help="Firebase app name")
    parser.add_argument("--mysql_host", type=str, help="MySQL host")
    parser.add_argument("--mysql_user", type=str, help="MySQL username")
    parser.add_argument("--mysql_password", type=str, help="MySQL password")
    parser.add_argument("--mysql_database", type=str, help="MySQL database name")
    args = parser.parse_args()

    main(args)
