import java.util.ArrayList;

public class Table {

    public String id;
    public ArrayList<Guest> occupants;
    public int numChairs;

    public Table(String id, int c) {
        this.id = id;
        this.numChairs = c;
        this.occupants = new ArrayList<Guest>();
    }

    public void showTable() {
        System.out.println("Table: "+this.id);
        for (Guest g: this.occupants) {
            g.showInfo();
        }
        System.out.println("------");
    }

    public ArrayList<Guest> getOccupants() {
        return this.occupants;
    }
    public int getNumChairs() {
        return this.numChairs;
    }
    public String getID() {
        return this.id;
    }

    
}
