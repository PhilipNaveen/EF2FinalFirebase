package FirebaseScripts;

import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        // Populate Firestore collections from MySQL
        FirebasePopulateMySQL.populateFromMySQL();

        // Create documents in Firestore collections
        FirebaseCreateDocuments.createDocuments();

        // Clear Firestore collections
        FirebaseClearCollections.clearCollections();
    }
}
