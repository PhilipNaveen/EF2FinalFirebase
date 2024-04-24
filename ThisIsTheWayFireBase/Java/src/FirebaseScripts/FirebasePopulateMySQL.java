import com.google.auth.oauth2.GoogleCredentials;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import com.google.cloud.firestore.CollectionReference;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.mysql.cj.jdbc.MysqlDataSource;
import java.io.FileInputStream;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class FirebasePopulateMySQL {

    public static void main(String[] args) throws IOException {
        // Path to the JSON file containing the service account key
        FileInputStream serviceAccount = new FileInputStream("src/content/KeyFirebaseThisIsTheWay.json");

        FirebaseOptions options = new FirebaseOptions.Builder()
            .setCredentials(GoogleCredentials.fromStream(serviceAccount))
            .build();

        FirebaseApp.initializeApp(options);

        Firestore db = FirestoreClient.getFirestore();

        // Connect to MySQL database
        MysqlDataSource dataSource = new MysqlDataSource();
        dataSource.setServerName("your_mysql_host");
        dataSource.setUser("your_mysql_user");
        dataSource.setPassword("your_mysql_password");
        dataSource.setDatabaseName("occupancy");

        try (Connection conn = dataSource.getConnection()) {
            Statement stmt = conn.createStatement();

            // Populate 'cameras' collection
            ResultSet camerasResult = stmt.executeQuery("SELECT * FROM cameras");
            populateCollection(camerasResult, "cameras", db);

            // Populate 'rawmetrics' collection
            ResultSet rawmetricsResult = stmt.executeQuery("SELECT * FROM rawmetrics");
            populateCollection(rawmetricsResult, "rawmetrics", db);

            // Populate 'rawmetrics_occupancy' collection
            ResultSet rawmetricsOccupancyResult = stmt.executeQuery("SELECT * FROM rawmetrics_occupancy");
            populateCollection(rawmetricsOccupancyResult, "rawmetrics_occupancy", db);

            // Populate 'rawmetrics_sum' collection
            ResultSet rawmetricsSumResult = stmt.executeQuery("SELECT * FROM rawmetrics_sum");
            populateCollection(rawmetricsSumResult, "rawmetrics_sum", db);

            stmt.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        System.out.println("Data population completed.");
    }

    // Function to populate Firestore collection
    private static void populateCollection(ResultSet resultSet, String collectionName, Firestore db) throws Exception {
        CollectionReference collectionRef = db.collection(collectionName);
        while (resultSet.next()) {
            DocumentReference docRef = collectionRef.document();
            docRef.set(resultSet.getObject(1).toString());
            for (int i = 2; i <= resultSet.getMetaData().getColumnCount(); i++) {
                docRef.update(resultSet.getMetaData().getColumnName(i), resultSet.getObject(i));
            }
        }
    }
}
