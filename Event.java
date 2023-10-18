import java.util.ArrayList;

public class Event {

    public String title;
    public int preRegistered = 0;
    public int numTables;
    public String date;
    public ArrayList<Table> tables;
    public ArrayList<Table> guests;


    public Event(String t, int nt, String date) {
        this.title = t;
        this.numTables = nt;
        this.date = date;
        this.tables =  new ArrayList<Table>();
    }

    public void showInfo() {
        System.out.println("Welcome to "+ this.title + " on "+this.date+"!");
        for (Table t: this.tables) {
            t.showTable();
        }
    }

    public void addGuest(String tableID, Guest g) {
        for (Table t: this.tables) {
            if (t.getID().equals(tableID) == true)  {
                t.occupants.add(g);
                break;
            }
        }
    }

    public void assignTable(Guest g) {
        double maxScore = 0;
        Table mostSimTable = new Table("null", 0);
        // iterate table objects
        for (Table t: this.tables) {
            double score = 0;
            // if there is space in table
            if (t.occupants.size() < t.numChairs) {
                if (t.occupants.size() > 0) {
                    // iterate guests of table and sum major-sim score
                    for (Guest p: t.occupants) {
                        score += Driver.majorMap.get(g.major).get(p.major);
                        System.out.println(g.major+" "+p.major + " "+Driver.majorMap.get(g.major).get(p.major));
                    }
                }
                else if (t.occupants.size() == 0) {
                    score = Driver.majorMap.get(g.major).get(t.id);
                }
                if (score > maxScore) {
                    System.out.println(score);
                    maxScore = score;
                    mostSimTable = t;
                }
            }
        }
        //System.out.println(mostSimTable.id+"ppppp");
        mostSimTable.occupants.add(g);
    }





}