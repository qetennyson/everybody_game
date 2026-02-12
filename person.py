"""People and dialogue behavior for the game."""

import random
from dialogue import (
    OLDER_DIALOGUE,
    YOUNGER_DIALOGUE,
    EXTROVERT_DIALOGUE,
    INTROVERT_DIALOGUE,
)

class Person:
    """Blueprint for all people that we make in our game."""

    DEFAULT_DIALOGUE = [
        "Hi",
        "Hello.",
        "What's up?",
        "How are you?",
        "How have you been?",
    ]
    
    # TODO:
    # SEPPARATE
    # GREETING_DIALOGUE
    # CONCLUDING_DIALOGUE

    # dictionary - looks up data w/ key-value pairs
    DIALOGUE_OPTIONS = {
        'OLD' : OLDER_DIALOGUE,
        'YOUNG' : YOUNGER_DIALOGUE,
        'EXTROVERTED' : EXTROVERT_DIALOGUE,
        'INTROVERTED' : INTROVERT_DIALOGUE,
    }

    # attributes - describe their state
    # methods - describe their behavior
    # constructor - builds a person from their unique attributes

    def __init__(
        self,
        name,
        age,
        appearance,
        personality,
        origin_position,
        qty_of_talking=.5,
        extr_to_intr=0.0,
    ):
        """Create a new person with traits used in the game."""
        self.name = name
        self.age = age
        self.appearance = appearance
        self.personality = personality
        self.origin_position = origin_position
        self.qty_of_talking = qty_of_talking
        self.extr_to_intr = extr_to_intr
        
    def is_old(self):
        """Return True if this person is considered old."""
        return self.age >= 35
    

    def speak(self, group):
        """Output dialogue for the person based on a group label."""
        rand_dialogue_choice = random.choice(Person.DEFAULT_DIALOGUE)
        group_dialogue_chance = random.randint(1,100)
        # selecting based on groups
        # each one randomly chooses either "typed" dialogue or default
        # each rolls for 1,100.

        if group_dialogue_chance <= 50:
            dialogue_choices = Person.DIALOGUE_OPTIONS.get(group.upper())
            if dialogue_choices is None:
                print("I'm not sure what to say...")
            else:
                random_group_dialogue = random.choice(dialogue_choices)
                print(random_group_dialogue)
        else:
            print(rand_dialogue_choice)
            
    def __repr__(self):
        return f'{self.name.title()}'