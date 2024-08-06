# Différentes maps
MAP_FILES = {
    1: 'assets/Map/Village_map.tmx',
    2: 'assets/Map/Labyrinthe_map.tmx',
    3: 'assets/Map/Harbor2_map.tmx'
}

# Object et configurations
OBJECTS = {
    1: [
        {'x': 670, 'y': 670, 'image_path': 'media/coin.png', 'level': 1, 'can_be_collected': True},
        {'x': 1255, 'y': 162, 'image_path': 'media/coin.png', 'level': 1, 'can_be_collected': True},
        {'x': 2184, 'y': 151, 'image_path': 'media/coin.png', 'level': 1, 'can_be_collected': True},
        {'x': 308, 'y': 1743, 'image_path': 'media/coin.png', 'level': 1, 'can_be_collected': True},
        {'x': 1557, 'y': 1842, 'image_path': 'media/coin.png', 'level': 1, 'can_be_collected': True},
    ],
    2: [
         {'x': 1440, 'y': 155, 'image_path': 'media/portal.png', 'level': 2, 'can_be_collected': True},
    ],
    3: [
        {'x': 1300, 'y': 138, 'image_path': 'media/Ship_full.png', 'level': 3, 'can_be_collected': True},
        {'x': 569, 'y': 963, 'image_path': 'media/coin.png', 'level': 3, 'can_be_collected': True},
        {'x': 241, 'y': 413, 'image_path': 'media/coin.png', 'level': 3, 'can_be_collected': True},
        {'x': 938, 'y': 414, 'image_path': 'media/coin.png', 'level': 3, 'can_be_collected': True},
        {'x': 1243, 'y': 1492, 'image_path': 'media/coin.png', 'level': 3, 'can_be_collected': True},
        {'x': 493, 'y': 1791, 'image_path': 'media/coin.png', 'level': 3, 'can_be_collected': True},
    ],
}

# Level messages
LEVEL_MESSAGES = {
    1: {
        1: "Collect the 5 coins to advance to the next level",
        2: "You've collected all the coins, now you can go to the cave to change levels"
    },
    2: {
        1: "Find the exit of the maze to proceed to the next level",
    },
    3: {
        1: "Collect 5 coins to pay for the boat",
        2: "You've collected all the coins, now you need to find the boat to finish the game"
    },
}

TARGETS = {
    1: {
        'coins': 5,
    },
    2: {
        'coins': 1,
    },
    3: {
        'coins': 5,
    },
}