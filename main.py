
# represents each Guest, given their name, major, and person_type which is either "student","prof","mentor"
class Guest:
    def __init__(self, name, major, person):
        self.name = name
        self.major = major
        self.person_type = person
# represents each Table, given its primary-key unique id-number, major-string, and its maximum occupancy integer
class Table:
    def __init__(self, id, major, max_seats):
        self.id = id
        self.major =  major
        self.max_seats = max_seats
        self.guests = []        # stores Guest-objs for all the guests currently seated at that table
    # prints table to console
    def show(self):
        print("TABLE-"+str(self.id) +": Major: "+self.major+ ": Seats: "+str(self.max_seats))
        for g in self.guests:
            print(g.name +": "+g.major+": Type: "+g.person_type)
        print("-----")
    # returns number of people of type-str currently seated at this table
    def get_type(self, type_str):
        count = 0
        for g in self.guests:
            if g.person_type == type_str:
                count += 1
        return count
# represents the seating chart, given number of tables per major, and max number allowed of each person type
class SeatingChart:

    def __init__(self, event_name, major_tables ,max_constants):
        self.event_name = event_name
        self.major_tables = major_tables
        self.tables = []
        self.unqiue_majors = ["CS","BIO"]
        self.initalize_tables()
        self.max_constants = max_constants

    def initalize_tables(self):
        cur_id = 1
        for major_name, num_tables in self.major_tables.items():
            for _ in range(num_tables):
                temp = Table(cur_id, major_name, 8)
                cur_id += 1
                self.tables.append(temp)

    def show(self):
        for t in self.tables:
            t.show()

    def assign_guest(self, new_guest): # given new Guest-obj
        # iterate all table-objs
        for table in self.tables:
            # if table major is same as guest-major
            if table.major == new_guest.major:
                # if number guests with same as type as guest-type at cur-table is less than max-amount and 
                if table.get_type(new_guest.person_type) < self.max_constants[new_guest.person_type] and len(table.guests) < table.max_seats:
                    table.guests.append(new_guest)
                    break

# {major-label: number of tables allocated}
major_tables = {"Aero/Mech":3,"Archi/Civil":3,"Elec":1,"Indus":1,"Env":1,"Bio":4,"Chem":3,"CS":3,"Deans/Chairmen/IndustryFriends":2}
# {person-type: }
max_constants = {"student":2, "prof":1, "mentor":1, "seats":8}
# 
chart = SeatingChart("Womens Engineering", major_tables, max_constants)

"""
chart.assign_guest(Guest("Bob","CS","student"))
chart.assign_guest(Guest("Kai","CS","student"))
chart.assign_guest(Guest("Sam","CS","student"))
chart.assign_guest(Guest("Mary","Bio","student"))
chart.show()
"""
    



"""
- Simulate randomness of how guests arrive
- A student major table is full add them to table with most similar score. Overflow Error. 

TODO:
- Create different number of tables per major
- Number of tables = 
- Number of seats per = 8
- Number of students per = 
- Number of prof per = 
- Number of mentor per = 
- All tables = []
"""