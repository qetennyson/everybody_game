class Room:

    def __init__(self, name, nsew_descriptions, crowding=.25, people=None):
        self.name = name
        self.crowding = crowding
        self.people = people if people is not None else []
        self.nsew_descriptions = nsew_descriptions

    def __repr__(self):
        
        return f'{self.name}\nPeople:{[person for person in self.people]}'


