import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import java.io.FileInputStream;
import java.io.IOException;

public class FirebaseCreateDocuments {

    public static void main(String[] args) throws IOException {
        // Path to the JSON file containing the service account key
        FileInputStream serviceAccount = new FileInputStream("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json");

        FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();

        FirebaseApp.initializeApp(options);

        Firestore db = FirestoreClient.getFirestore();

        // Create a document in the 'cameras' collection
        createDocument("cameras", db, "123456", "Location short description", "Location long description");

        // Create a document in the 'rawmetrics' collection
        createDocument("rawmetrics", db, "123456", "Source", 10, 5, 5, 1615894140);

        // Create a document in the 'rawmetrics_occupancy' collection
        createDocument("rawmetrics_occupancy", db, "123456", 10, 5, 5, "2024-04-24", "09:09:48", "Wednesday", "Wed");

        // Create a document in the 'rawmetrics_sum' collection
        createDocument("rawmetrics_sum", db, "123456", 5, 5, "2024-04-24", "09:09:48", "Wednesday", "Wed");

        System.out.println("Documents creation completed.");
    }

    // Function to create a document in Firestore collection
    private static void createDocument(String collectionName, Firestore db, String serialNo, String locationShort, String locationLong) {
        DocumentReference docRef = db.collection(collectionName).document();
        docRef.set(new Object() {
            public final String id = "1";
            public final String serial_no = serialNo;
            public final String location_short = locationShort;
            public final String location_long = locationLong;
            public final Object created_at = com.google.firebase.database.ServerValue.TIMESTAMP;
        });
    }

    // Overloaded function to create a document in Firestore collection with rawmetrics data
    private static void createDocument(String collectionName, Firestore db, String serialNo, String source, int occupancy, int countIn, int countOut, long sourceUnixTime) {
        DocumentReference docRef = db.collection(collectionName).document();
        docRef.set(new Object() {
            public final String id = "1";
            public final String serial_no = serialNo;
            public final String source = source;
            public final int occupancy = occupancy;
            public final int count_in = countIn;
            public final int count_out = countOut;
            public final long source_unixtime = sourceUnixTime;
            public final Object created_at = com.google.firebase.database.ServerValue.TIMESTAMP;
        });
    }

    // Overloaded function to create a document in Firestore collection with rawmetrics_occupancy data
    private static void createDocument(String collectionName, Firestore db, String serialNo, int occupancy, int totalIn, int totalOut, String date, String time, String day, String dow) {
        DocumentReference docRef = db.collection(collectionName).document();
        docRef.set(new Object() {
            public final String id = "1";
            public final String serial_no = serialNo;
            public final int occupancy = occupancy;
            public final int total_in = totalIn;
            public final int total_out = totalOut;
            public final String date = date;
            public final String time = time;
            public final String day = day;
            public final String dow = dow;
        });
    }

    // Overloaded function to create a document in Firestore collection with rawmetrics_sum data
    private static void createDocument(String collectionName, Firestore db, String serialNo, int countIn, int countOut, String date, String time, String day, String dow) {
        DocumentReference docRef = db.collection(collectionName).document();
        docRef.set(new Object() {
            public final String id = "1";
            public final String serial_no = serialNo;
            public final int count_in = countIn;
            public final int count_out = countOut;
            public final String date = date;
            public final String time = time;
            public final String day = day;
            public final String dow = dow;
        });
    }
}
