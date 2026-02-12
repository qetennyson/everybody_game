"""Main entry point and game setup."""

import random
from person import Person
from player import Player
from room_data import kitchen, living_room, basement


people = [
    Person("Aunt Sherry", 46, "dark hair + black eyes + black purse", "introverted", "Living Room"),
    Person("Cousin Emma", 16, "wears pink + short hair", "extroverted", "Basement"),
    Person("Jerry Gary", 37,"fanny pack + bald", "introverted", "Kitchen"),
    Person("Uncle Barry", 54, "fat + blue eyes + blonde hair", "extroverted", "Living Room"),
    Person("Cousin Selena", 15, "skinny + red hair + green eyes", "introverted", "Bedroom"),
    Person("Aunt Trixie", 32, "pink highlights + curly hair", "extroverted", "Basement"),
    Person("Uncle Will", 26, "blond hair + fit + the cool uncle", "extroverted", "Living Room"),
    Person("Dad", 40, "brunette + beard + hazel eyes", "extroverted", "Living Room"),
    Person("Mom", 38, "black hair + dark blue eyes", "extroverted", "Kitchen"),
    Person("Thomas", 15, "brunette + green eyes", "introverted", "Bedroom"),
    Person("Quinn", 17, "black hair + grey eyes", "extroverted", "Living Room"),
    Person("Eli", 5, "short hair + brown eyes", "extroverted", "Basement"),
    ]

rooms = [kitchen, living_room, basement]

def print_rooms(room_list):
    """Print each room and its people."""
    for room in room_list:
        print(room)
        
def place_people_in_rooms(p=people, r=rooms):
    """Place each person into their matching room."""
    for person in p:
        for room in r:
            if person.origin_position.lower() == room.name.lower():
                room.people.append(person)
               
    
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
    
    # TODO: move to room.py

    """
    
def consquences_of_your_actions(player_action):
    """
    This function takes the players action and creates
    a consquence of that action
    """


def speak_with_person(person, player):
    """Run a back-and-forth conversation with a person."""
    # person initiates the conversation
    # Flag variable
    conversation_has_failed = False
    
    while True:
        person.speak(person.personality)
    # random greeting, random question?
    # question specific to the type of person / drawn from the lists
    # player responds
    
        response = input("How do you respond?")
        
    # Check for length - Introvert/Extrovert (charcter count)
        if len(response) > 50 and (person.personality != 'extroverted'):
            print(person.personality)
            conversation_has_failed = True
            print("Yeah, sure, whatever. I don't like talking this much")
        elif len(response) <= 50 and (person.personality != 'introverted'):
            conversation_has_failed = True
            print("Yeah, sure, whatever.  I can see you don't want to talk.")
          
            
    # Check grammer - Old/Young (grammer)
        if check_for_brainrot(response) == True and person.is_old():
            conversation_has_failed = True
            print("Don't talk to an old person with such confusing language!")
       
            
    # If checks fail - set statement / decrement "HP?"
        if conversation_has_failed == True:
            print("They didn't like that response")
            # decrease player hp
            player.HP -= 1 
            # "The player has <HP> left"
            print("The player has " + str(player.HP) + "HP remaining.")
        else: 
            continue_chance = 50
            if random.randint(1, 100) <= continue_chance:
                continue
            else:
                print("They walked away.")
                return
        if is_death(player):
            print("You DED!!!!!!!☠️☠️☠️☠️☠️☠️")
            break
    # If they succeed
        # chance for the person to continue talking or leave the conversation
    # longer conversation = higher chance to end
    
def is_death(player):
    if player.HP > 0:
        return False
    else:
        return True
    
def check_punctuation(user_message):
    """
    Returns True if the user_message has proper punctuation at the end of the 
    sentence, AND the first letter is capitalized
    AND if the word 'and' is present, an Oxford comma is used UNLESS the
    'and' is the first word in the message.
    
    Otherwise return False.
    
    >>> check_punctuation('hi')
    False
    >>> check_punctuation('hi.')
    False
    >>> check_punctuation('Hi.')
    True
    >>> check_punctuation("And then?")
    True
    >>> check_punctuation("I had beans and cornbread.")
    False
    >>> check_punctuation("I had beans, and cornbread.")
    True
    """
    
    

def check_for_brainrot(user_message):
    """
    Use this link:
    https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings#the-in-and-not-in-operators
    
    Return True if the user_message contains any of the words in the school
    appropriate brain rot word list.
    
    """
    BRAIN_ROT_WORDLIST = [
        "67",  # that is dead #sshh bro 
        "Ballerina caputina",
        "negative rizz",
        "positive rizz",
        "aura",
        "brainrot vibes",
        "cheugy", 
        "cringe",
        "delulu",
        "fanum tax",
        "goated with the sauce",
        "goblin mode", 
        "hitting the griddy",
        "looksmaxxing",
        "mewing",
        "mid no cap",
        "only in ohio",
        "skibidi",
        "yeet",
        "put the fries in the bag",
        "idk",
    ]
    
    # return BRAIN_ROT_WORDLIST in user_message
    for brain_rot in BRAIN_ROT_WORDLIST:
        # check each element in the list and see if its in the message
        if brain_rot in user_message:
            return True
            
    return False

def produce_room_event(events):
    """
    This function takes a list of events and using a random percentage
    to get chances of that event happening, we return an event. 
    random.random is a random percentage between 0 and 1.
    """
    event_chance = random.random()
    if event_chance < 0.55:
        speak_with_person() # needs argument
    elif event_chance < .9:
        pass

def main():
    """Run the game loop."""
    place_people_in_rooms()
    # calling the print_rooms function with rooms as an argument

    # kitchen.display_people_in_room()
    # kitchen.display_cardinal_directions()
    # player enters room
    new_player = Player(kitchen)
    players_room = new_player.room
    # room description display - Tennyson
    # display people in room - Ireland
    # TODO: display particular room features, e.g. weird basement, fight! - Ray
    # display directional descriptions - Jade
    # what happens?
    random_person = random.choice(players_room.get_list_of_people()) #method
    print(random_person)
    speak_with_person(random_person, new_player)
    # handle player choice -Ireland
    # outcomes/events from player choices - Jade
    
    
    # loop (while)

if __name__ == '__main__':
    main()