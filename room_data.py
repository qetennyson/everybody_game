from room import Room

kitchen = Room('Kitchen',
    {
    'n': 'the sink and window and counter with knives',
    's': 'the entrance to the kitchen',
    'e': 'mysterious basement entrance',
    'w': 'mud room entrance',
    },
)

living_room = Room(
    'Living Room',
    {
    'n': 'window',
    's': 'couch',
    'e': 'TV playing the football game',
    'w': 'a GHOST (and some chairs)',
    },
)

basement = Room(
    'Basement',
    {
    'n': 'TV',
    's': 'small children with a nintendo',
    'e': 'random stuff on shelves',
    'w': 'couch',
    },
)