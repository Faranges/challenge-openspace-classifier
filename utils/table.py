"""
table.py
Contains the Seat and Table classes.
 """
class Seat:
    """
    Represents a single seat in the workspace.

    Attributes: 
        free: (bool): True if the seat is available.
        occupant (str): Name of the person occupying the seat.
    """
    def __init__(self, free: bool = True, occupant: str = "") -> None:
        
        self.free: bool = free
        self.occupant: str = occupant
    
    def set_occupant(self,name: str) -> None:
        """Assign a person to the seat if it's free."""
       
        if self.free:
            self.occupant = name
            self.free = False
            print(f"{name} has been assigned to the seat.")
        else:
            print(f"Seat is already occupied by {self.occupant}.")

    def remove_occupant(self) -> str:
        """Remove the person from the seat and make it free again."""
       
        if self.free == False:
            name = self.occupant
            self.occupant = " "
            self.free = True
            print(f"{name} has left the seat")
            return name
        else:
            print("Seat is already free")
            return None
    
    def __str__(self) -> str:
        """Return a readable representation of the seat."""
        
        if self.free:
            return "Empty seat"
        else: 
            return f"Seat occupied by {self.occupant})"

class Table:
    """ 
    Represents a table containing several seats.

    Attributes: 
        capacity(int): number of seats at the table
        seats (list): a list of seat objects
    """
    def __init__(self, capacity: int = 4) -> None:
       
        self.capacity = capacity
        # Create an empty list to hold the seats
        seats = []
        # Add Seat() objects one by one
        for _ in range(capacity):
            new_seat = Seat()       # create a new Seat object
            seats.append(new_seat)  # add it to the list
        self.seats = seats          # assign the finished list to the attribute
    
    def has_free_spot(self) -> bool:
        """Return True if at least one seat is free."""
        
        for seat in self.seats:
            if seat.free:
                print("A seat is available.")
                return True
        print(f"No free seats available.")
        return False
    
    def assign_seat(self,name: str) -> bool:
        """Assign a person to the first free seat."""
        
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        
        print(f"No free seats available for {name}.")
        return False
    
    def left_capacity(self) -> int:
        """Return the number of free seats left."""
        
        free_count = 0               # Start counting from zero
        for seat in self.seats:      # Loop through all seats
            if seat.free:            # Check if this seat is free
                free_count += 1      # Increase our counter
        return free_count            # Return the final count
    
    def __str__(self) -> str:
        """Return a readable summary of the table"""
        
        return f"This table has a capacity of {self.capacity} and has {self.left_capacity} seats left."
    

    

