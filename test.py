class Guest:
    def __init__(self, name, major, guest_type):
        self.name = name
        self.major = major
        self.type = guest_type

class SeatingChart:
    def __init__(self, num_tables, table_size, a_count, b_count, c_count):
        self.num_tables = num_tables
        self.table_size = table_size
        self.required_a = a_count
        self.required_b = b_count
        self.required_c = c_count
        self.tables = [[None for _ in range(table_size)] for _ in range(num_tables)]
        self.first = True

    def update_seating_chart(self, new_guest):
        for table in self.tables:
            if self.first == True:
                self.tables[0][0] = new_guest
                self.first = False
                return
            if None in table:
                table_major = ""
                for guest in table:
                    if guest != None:
                        table_major = guest.major
                        break
                if table_major != "" and table_major == new_guest.major:
                    a_count = sum(1 for guest in table if guest and guest.type == 'A')
                    b_count = sum(1 for guest in table if guest and guest.type == 'B')
                    c_count = sum(1 for guest in table if guest and guest.type == 'C')
                    
                    if new_guest.type == 'A' and a_count < self.required_a:
                        table[table.index(None)] = new_guest
                        return
                    elif new_guest.type == 'B' and b_count < self.required_b:
                        table[table.index(None)] = new_guest
                        return
                    elif new_guest.type == 'C' and c_count < self.required_c:
                        table[table.index(None)] = new_guest
                        return

        # If no suitable table is found, create a new table
        if len(self.tables) < self.num_tables:
            self.tables.append([new_guest])

    def display_seating_chart(self):
        for idx, table in enumerate(self.tables, start=1):
            print(f"Table {idx}:")
            for guest in table:
                if guest:
                    print(f"  {guest.name}: {guest.major} ({guest.type})")
                else:
                    print("  Empty Seat")
            print()
                
# Example usage
num_tables = 3
table_size = 3
a_count = 2
b_count = 1
c_count = 1

seating_chart = SeatingChart(num_tables, table_size, a_count, b_count, c_count)

# Assuming new guests arrive
g1 = Guest("Alice", 'CS', 'A')
g2 = Guest("Bob", 'BIO', 'A')
g3 = Guest("Chris", 'CS', 'A')

seating_chart.update_seating_chart(g1)
seating_chart.update_seating_chart(g2)
seating_chart.update_seating_chart(g3)

# Printing the updated seating chart
seating_chart.display_seating_chart()

"""
There are different type of people such as students and proffesors. 
There is a required amount of people for each type of person for each table. 


"""
