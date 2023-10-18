
class Guest:

    def __init__(self, name, major, person):
        self.name = name
        self.major = major
        self.person = person


class Table:
    def __init__(self, id, major, max_seats):
        self.id = id
        self.major =  major
        self.max_seats = max_seats
        self.guests = []

    def show(self):
        print("Table: "+str(self.id) +": Major: "+self.major+ ": Seats: "+str(self.max_seats))
        for g in self.guests:
            print(g.name +": "+g.major+": Type: "+g.person)
        print("-----")

    def get_type(self, type_str):
        count = 0
        for g in self.guests:
            if g.person == type_str:
                count += 1
        return count

class SeatingChart:

    def __init__(self, event_name, num_tables, max_constants):
        self.event_name = event_name
        self.num_tables = num_tables
        self.tables = []
        self.majors = ["CS","BIO"]
        self.initalize_tables()

        self.max_constants = max_constants

    def initalize_tables(self):
        for i in range(self.num_tables):
            t = Table(i+1, self.majors[i], 3)
            self.tables.append(t)
    def show(self):
        for t in self.tables:
            t.show()


    def assign_guest(self, new_guest):
        for table in self.tables:
            if table.major == new_guest.major:

                if table.get_type(new_guest.person) < self.max_constants[new_guest.person] and len(table.guests) < table.max_seats:
                    table.guests.append(new_guest)
                    break

chart = SeatingChart("Womens Engineering", 2, {"student":1, "prof":1, "mentor":1})

g1 = Guest("Bob","CS","student")
g2 = Guest("Sam","CS","mentor")
chart.assign_guest(g1)
chart.assign_guest(g2)
chart.show()

    



"""
- Simulate randomness of of how guests arrive

"""