"""Room definitions used by the game."""

from room import Room

kitchen = Room('Kitchen',
    {
    'n': 'the sink and window and counter with knives',
    's': 'the entrance to the kitchen',
    'e': 'mysterious basement entrance',
    'w': 'mud room entrance',
    },
    "A busy kitchen filled with aromas and other human beings."
)

living_room = Room(
    'Living Room',
    {
    'n': 'window',
    's': 'couch',
    'e': 'TV playing the football game',
    'w': 'a GHOST (and some chairs)',
    },
    "The most common and busy room inside the house, the living room.. whats that in the corner?"
)


basement = Room(
    'Basement',
    {
    'n': 'TV',
    's': 'small children with a nintendo',
    'e': 'random stuff on shelves',
    'w': 'couch',
    },
    "An eerie creak echoes as you step off the staircase, then childrens excited screams fill the room whilst they're all hudled around one kid in the center, video game music blasting from the nintendo clamped in the one kids hand. Looks like they're having fun."
)

bathroom = Room(
    'Bathroom',
    {
    'n': 'bathtub',
    's': 'towel rack',
    'e': 'bathmat, plunger, toilet',
    'w': 'sink, mirror, cabinets,',
    },
    "Despite normally known for filthy and foul-smelling, everything was seat up quite neatly and brand new. Perhaps someone tided the bathroom up before all the guest arrived. "
)

starter_bedroom = Room(
    'Bedroom',
    {
    'n': 'TV, TV stand',
    's': 'bed, nightstand, alarm clock',
    'e': 'posters, computer set up',
    'w': 'trash can, lamp',
    },
    "The lamp in the left side of the room emits a shine throughout the room, the familar nightstand, bed, and posters hanging on the wall greets you as you enter the room."
)



dining_room = Room(
    'dining room',
    {
    'n': 'table, adults talking at the table',
    's': 'fake plants',
    'e': 'picture frame, windows',
    'w': 'shelves',
    },
    "The first thing you take hold of as you walk into the dining room is the adults gathered at the table, and the picture frames scattered amongst the walls. The pictures that are set up are quite pretty too."
)
