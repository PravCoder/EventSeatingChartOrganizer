
public class Guest {

    public String name;
    public String age;
    public String type;    // student, mentor, faculty, staff
    public String major;
    public int educationYear;
    public Table table;

    public Guest(String n, String major) {
        this.name = n;
        this.major = major;
    }

    public void showInfo() {
        System.out.println(this.name + ", "+this.major);
    }

    public String getName() {
        return this.name;
    }
    public String getAge() {
        return this.age;
    }

    public String getType() {
        return this.type;
    }

    public String getMajor() {
        return this.major;
    }





}