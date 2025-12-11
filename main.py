import random
from person import Person
from room_data import kitchen, living_room, basement

MIN_RESPONSE_LENGTH = 100

people = [
    Person("Aunt Sherry", "dark hair, black eyes, black purse", "introverted", "living Room"),
    Person("Cousin Emma", "wears pink, short hair", "extroverted", "Basement"),
    Person("Jerry Gary", "fanny pack + bald", "introverted", "Kitchen"),
    ]

rooms = [kitchen, living_room, basement]

# show the people in the rooms
# print(room) to do that.
def print_rooms(room_list):
    for room in room_list:
        print(room)
        
def place_people_in_rooms(p=people, r=rooms):
    for person in p:
        for room in r:
            if person.origin_position.lower() == room.name.lower():
                room.people.append(person)
               
 
def display_people_in_rooms(people_in_rooms):
    """
    This function is displays the people that are in the 
    room the player has entered.
    """
    
def player_choice(choices):
    """
    This function asks the player what they would like to do
    next based on what has just happened.
    """
    
# a function needs a name, and it needs the things necessary
# to do its job (its function)

def display_room_description(room_description):
    """
    This function displays the general description of the room,
    that the player is in / has entered.
    """
    
def display_cardinal_directions(nsew_descriptions):
    """
    This function displays the North/East/South/West
    directions....
    """

def consquences_of_your_actions(player_action):
    """
    This function takes the players action and creates
    a consequence of that action
    """
    
def display_room_features(room_features):
    """
    This function displays the features found inside the room the player 
    has entered.
    """
    
def produce_room_event(events):
    """
    This function takes a list of events and using a random percentage
    to get chances of that event happening, we return an event. 
    random.random() is a random percentage between 0 and 1.
    """
    event_chance = random.random()
    if event_chance < 0.55:
        speak_with_person()
    elif event_chance < .9:
        pass
    else:
        pass


def speak_with_person(person: Person):
    """
    Runs the game dialogue algorithm.
    
    :param person: a person object with whom the player is interacting.
    """
    satisfactory_resp = False
    while not satisfactory_resp:
        person.speak(person.personality) # personality must correlate to dialogue dict
        user_response = input('> ').strip()

        # what to do here?
        print(f"You say: {user_response}")

        # TODO: Simple heuristic would be length of response threshold based on
        # Extrovert vs. Introvert

        # TODO: Another, level of formality based on OLD or YOUNG.
        if len(user_response) >= 100:
            satisfactory_resp = True
        
        else:
            pass # reduce player time / HP.
        


def main():
    place_people_in_rooms()
    # calling the print_rooms function with rooms as an argument
    print_rooms(rooms)
    
    # player enters room
    
    
    # room description display - Tennyson
    # display people in room - Ireland
    # TODO: display particular room features, e.g. weird basement, fight! - Ray
    # display directional descriptions - Jade
    # what happens?
    # handle player choice -Ireland
    # outcomes/events from player choices - Jade
    
    
    # loop (while)

if __name__ == '__main__':
    main()
