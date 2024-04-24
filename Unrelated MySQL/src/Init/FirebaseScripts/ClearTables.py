import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json")

try:
    app = firebase_admin.get_app("toydb_app")
except ValueError:
    app = firebase_admin.initialize_app(cred, name="toydb_app")

db = firestore.client(app)


# Function to delete all documents in a collection
def delete_all_documents(collection_name):
    collection_ref = db.collection(collection_name)
    docs = collection_ref.stream()
    for doc in docs:
        doc.reference.delete()

# Collections to clear
collections_to_clear = ["cameras", "rawmetrics", "rawmetrics_occupancy", "rawmetrics_sum"]

# Clearing collections
for collection_name in collections_to_clear:
    delete_all_documents(collection_name)
