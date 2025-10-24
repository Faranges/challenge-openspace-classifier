import random                     # use this to randomly shuffle the list of names

from utils.table import Table     # This import allows us to use Table and Seat objects inside our OpenSpace class   

class OpenSpace:
    """ 
    Represents an open workspace containing multiple tables.

    Attributes: 
        number_of_tables(int): Number of tables in the space
        tables(list): A list of Table objects
    """
    def __init__(self, number_of_tables: int = 6) -> None:
        # Save the number of tables as an attribute 
        self.number_of_tables = number_of_tables

        # Create an empty list that will hold all the Table objects
        self.tables = []

        # Loop as many times as there are tables
        for i in range(number_of_tables):
            # Create one new Table object (each table will have its own seats)
            table = Table()

            # Add the newly created Table to the list of tables
            self.tables.append(table)
    
    def organize(self,names: list[str]) -> None:
        """Randomly assign people to available seats across all tables."""
        
        random.shuffle(names)                                   # Shuffle the list of names so the order is random
        name_index = 0                                          # Keep track of which person we're assigning
        for table in self.tables:                               # Loop through all the tables in OpenSpace
            for seat in table.seats:                            # Loop through each seat in the current table
                if name_index < len(names) and seat.free:       # If there are still people left to assign AND seat is free
                    seat.set_occupant(names[name_index])        # Assign this person
                    name_index += 1                             # Move to the next person
        
        if name_index < len(names):
            print("Warning:some people could net be seated.")   # If there were more people than seats, print a warning
        else:
            print("Everyone has been seated successfully.")

    def display(self) -> None:
        """SHow  all tables and their occupants in a readable way."""
        print("\n Open Space Seating Plan")
        
        for i, table in enumerate(self.tables, start=1):        # Go through all tables one by one
            print(f"Table {i}:")                             # Display the table number

            for j, seat in enumerate(table.seats, start=1):     # Go through all seats in this table
                if seat.free:
                    print(f"  Seat {j}: [Empty]")
                else:
                    print(f"  Seat {j}: {seat.occupant}")

        print("End of Seating Plan\n")

    def store(self,filename: str) -> None:
        """Save the current seating arrangement into a text file."""
        with open (filename, "w") as file:                      # Open a file in write mode
            file.write("Open Space Seating Plan\n")             # Write a title at the top
            
            for i, table in enumerate(self.tables, start=1):    # Go through each table and each seat
                file.write(f"Table {i}:")
                for j, seat in enumerate(table.seats, start=1):
                    if seat.free:
                        file.write(f"  Seat {j}: [Empty]")
                    else:
                        file.write(f"  Seat {j}: {seat.occupant}")

        print(f"Seating plan saved successfully in '{filename}'.")

    def __str__(self) -> str:
        """Short summary of the OpenSpace"""
        return f"Openspace with {len(self.tables)} tables."
            



        
