class Room:

    def __init__(self, name, nsew_descriptions, general_description,crowding=.25, people=None):
        self.name = name
        self.crowding = crowding
        self.people = people if people is not None else []
        self.nsew_descriptions = nsew_descriptions

    def get_list_of_people(self):
        return self.people

    def display_people_in_room(self):
        """
        This function is displays the people that are in the 
        room the player has entered.
        
        # TODO: Jade
        """
        for person in self.people:
            print(person)

    def display_cardinal_directions(self):
        """
        This function displays the North/East/South/West
        directions....
        
        # TODO: move to room.py
        """
        for key,value in self.nsew_descriptions.items():
            print(key,value)

    def __repr__(self):
        
        return f'{self.name}\nPeople:{[person for person in self.people]}'


