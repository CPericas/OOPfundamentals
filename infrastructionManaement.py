#Task 1: Vehicle Registration System
#- Problem Statement: Create a Python class `Vehicle` with attributes `registration_number`, `type`, and `owner`. Implement a method 
# `update_owner` to change the vehicle's owner. Then, create a few instances of `Vehicle` and demonstrate changing the owner.
#- Code Example: Provide a basic structure for the `Vehicle` class without methods.
#    class Vehicle:
#        def __init__(self, reg_num, type, owner):
#            self.registration_number = reg_num
#            self.type = type
#            self.owner = owner
# Expected Outcome: Completion of the `Vehicle` class with the `update_owner` method and a demonstration script showing the creation of 
# `Vehicle` objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self):
        new_owner = input("Enter the new owner's name: ")
        self.owner = new_owner
if __name__ == "__main__":
    vehicle1 = Vehicle("ABC123", "Car", "John")
    vehicle2 = Vehicle("XYZ789", "Motorcycle", "Alice")
    
    print("Original owners:")
    print("Vehicle 1 - Owner:", vehicle1.owner)
    print("Vehicle 2 - Owner:", vehicle2.owner)
    
    while True:
        vehicle_choice = input("Enter the vehicle number (1 or 2) to update its owner (0 to finish updating): ")        
        if vehicle_choice == "0":
            break
        elif vehicle_choice == "1":
            vehicle1.update_owner()
        elif vehicle_choice == "2":
            vehicle2.update_owner()
        else:
            print("Invalid choice. Please enter 0, 1, or 2.")
    print("\nUpdated owners:")
    print("Vehicle 1 - Owner:", vehicle1.owner)
    print("Vehicle 2 - Owner:", vehicle2.owner)


#Task 2: Event Management System Enhancement
#- Problem Statement: Extend an existing `Event` class by adding a feature to keep track of the number of participants. Implement a 
# method `add_participant` that increases the count and a method `get_participant_count` to retrieve the current count.
#- Code Example: Basic `Event` class without participant tracking.
#    class Event:
#        def __init__(self, name, date):
#            self.name = name
#            self.date = date


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count

def display_menu():
    print("Menu:")
    print("1. Add Participant")
    print("2. View Participant Count")
    print("3. Exit")

if __name__ == "__main__":
    event = Event("Birthday Party", "2024-07-01")
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            event.add_participant()
            print("Participant added.")
        elif choice == '2':
            participant_count = event.get_participant_count()
            print("Participant count:", participant_count)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
