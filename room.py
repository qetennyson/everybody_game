"""Room model and display helpers for the game."""


class Room:
    """Represents a room the player can enter."""

    def __init__(
        self,
        name,
        nsew_descriptions,
        general_description,
        crowding=.25,
        people=None,
    ):
        """Create a room with descriptions, people, and crowding."""
        self.name = name
        self.crowding = crowding
        self.people = people if people is not None else []
        self.nsew_descriptions = nsew_descriptions
        self.general_description = general_description

    def get_list_of_people(self):
        """Return the list of people currently in the room."""
        return self.people

    def display_people_in_room(self):
        """
        Display the people that are in the room the player has entered.
        """
        for person in self.people:
            print(person)

    def display_cardinal_directions(self):
        """
        Display the North/East/South/West directions.
        """
        for key,value in self.nsew_descriptions.items():
            print(key,value)

    def __repr__(self):
        
        return f'{self.name}\nPeople:{[person for person in self.people]}'


