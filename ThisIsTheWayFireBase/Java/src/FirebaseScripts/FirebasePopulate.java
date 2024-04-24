import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.google.cloud.firestore.CollectionReference;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;
import java.util.Arrays;

public class FirebasePopulate {

    public static void main(String[] args) throws IOException {
        // Path to the JSON file containing the service account key
        FileInputStream serviceAccount = new FileInputStream("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json");

        FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();

        FirebaseApp.initializeApp(options);

        Firestore db = FirestoreClient.getFirestore();

        // Data to populate Firestore
        String[][] data = {
            {"cameras", "id", "serial_no", "location_short", "location_long", "created_at"},
            {"1", "ACCC8EF6B105", "Science & Engineering", "SEL Main Entry C120", "2023-10-16 13:08:26"},
            {"2", "ACCC8EF8C88D", "Science & Engineering", "SEL Lower Level Stairwell C054", "2023-10-16 13:08:26"},
            {"3", "ACCC8EF02852", "Science & Engineering", "SEL Room C220", "2023-10-16 13:08:26"},
            {"4", "ACCC8EF03315", "Science & Engineering", "SEL Room C210", "2023-10-16 13:08:26"},
            {"5", "B8A44F4F195D", "Science & Engineering", "SEL Room C200", "2023-10-16 13:08:26"},
            {"6", "ACCC8EF0C7E4", "Science & Engineering", "SEL Upper Level Stairwell C150", "2023-10-16 13:08:26"},
            {"7", "ACCC8EF0C2F1", "Science & Engineering", "SEL Upper Level Stairwell C141", "2023-10-16 13:08:26"},
            {"8", "ACCC8EF0C7F2", "Science & Engineering", "SEL Upper Level Stairwell C152", "2023-10-16 13:08:26"}
        };

        // Populate collections
        populateFirestore(data, db);

        // Collections to clear
        String[] collectionsToClear = {"cameras", "rawmetrics", "rawmetrics_occupancy", "rawmetrics_sum"};

        // Clearing collections
        for (String collectionName : collectionsToClear) {
            deleteAllDocuments(collectionName, db);
        }
    }

    // Function to populate documents in Firestore
    private static void populateFirestore(String[][] data, Firestore db) {
        for (int i = 1; i < data.length; i++) {
            String collectionName = data[0][0];
            CollectionReference collectionRef = db.collection(collectionName);
            DocumentReference docRef = collectionRef.document();
            for (int j = 1; j < data[i].length; j++) {
                String fieldName = data[0][j];
                String value = data[i][j];
                docRef.update(fieldName, value);
            }
        }
    }

    // Function to delete all documents in a collection
    private static void deleteAllDocuments(String collectionName, Firestore db) {
        CollectionReference collectionRef = db.collection(collectionName);
        try {
            ApiFuture<QuerySnapshot> future = collectionRef.get();
            List<QueryDocumentSnapshot> documents = future.get().getDocuments();
            for (QueryDocumentSnapshot document : documents) {
                document.getReference().delete();
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
