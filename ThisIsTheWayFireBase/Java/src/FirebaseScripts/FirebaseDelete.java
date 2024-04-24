import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.google.cloud.firestore.CollectionReference;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.cloud.firestore.QuerySnapshot;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.List;

public class FirebaseDelete {

    public static void main(String[] args) throws IOException {
        // Path to the JSON file containing the service account key
        FileInputStream serviceAccount = new FileInputStream("/content/toydb-fc565-firebase-adminsdk-zk77a-857e711da1.json");

        FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();

        FirebaseApp.initializeApp(options);

        Firestore db = FirestoreClient.getFirestore();

        // Collections to clear
        String[] collectionsToClear = {"cameras", "rawmetrics", "rawmetrics_occupancy", "rawmetrics_sum"};

        // Clearing collections
        for (String collectionName : collectionsToClear) {
            deleteAllDocuments(collectionName, db);
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
