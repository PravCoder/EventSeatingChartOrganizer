import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;

public class Driver {

    public static HashMap<String, HashMap<String, Double>> majorMap = new HashMap<>();

    public static void main(String args[]) {
        // {major: {other-major: rating, other:rating, other:score}}
        String[] tableIDS = {
            "Aerospace Engineering",
            "Architectural Engineering",
            "Biomedical Engineering",
            "Chemical Engineering",
            "Chemical Engineering: Bioengineering",
            "Civil Engineering",
            "Computer Engineering",
            "Computer Science",
            "Electrical Engineering",
            "Engineering Physics",
            "Environmental Engineering",
            "Environmental Science",
            "Industrial and Systems Engineering",
            "Industrial and Systems Engineering: Analytics",
            "Mechanical Engineering"
        };

        try (BufferedReader br = new BufferedReader(new FileReader("weights.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains(" = ")) {
                    // Split the line into major A, major B, and similarity rating
                    String[] parts = line.split(" \\+ | = ");
                    String majorA = parts[0];
                    String majorB = parts[1];
                    double similarity = Double.parseDouble(parts[2]);
                    // key doesnt exists add (String, Map) pair to majorMap, adding the reverse aswell
                    majorMap.computeIfAbsent(majorA, k -> new HashMap<>()).put(majorB, similarity);
                    majorMap.computeIfAbsent(majorB, k -> new HashMap<>()).put(majorA, similarity);
                } 
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // SIMULATION
        Event e1 = new Event("Women's Engineering Event", 15, "07/13/2005");
        for (String tableName: tableIDS) {
            e1.tables.add(new Table(tableName, 1));
        }
        
        Guest g1 = new Guest("Sally", "Computer Science");
        Guest g2 = new Guest("Mary", "Computer Science");
        e1.assignTable(g1);
        e1.assignTable(g2);
        e1.showInfo();


    }

    public static void getSimilarity(String a, String b, HashMap<String, HashMap<String, Double>> map) {
        double similarityRating = map.get(a).get(b);
        System.out.println("Similarity Rating between "+a+" & "+b+" " + similarityRating);
    }
    
}
