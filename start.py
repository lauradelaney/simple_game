def main():
    game_loop()


rooms = {


    # 'template': {
    #     'name': '',
    #     'desc': '',
    #     'north': '',
    #     'south': '',
    #     'east': '',
    #     'west': '',
    #     'search': '',
    #     'search_desc': '',
    # },

    'bathroom': {
        'name': 'bathroom',
        'desc': 'a room that smells truly damp. There is a slightly ajar door to the SOUTH.',
        'south': 'bedroom',     
    },

    'bedroom': {
        'name': 'bedroom',
        'desc': 'You enter a space that seems to have lived a thousand lives. None of them have been cleaners though... There is a door NORTH, and one WEST.',
        'search': 'Glasses',
        'search_desc': 'You find a pair of glasses scattered across the floor.',   
        'north': 'bathroom',
        'west': 'living room'
    },

    'living room': {
        'name': 'living room',
        'desc': 'You enter a messy room with a couch and TV. There is a door to the EAST, one to the SOUTH (with a lock on it), and an open doorframe to the WEST.',
        'south': 'hallway',
        'east': 'bathroom',
        'west': 'kitchen',
    },

}

current_room = rooms['bathroom']
directions = ['north','south','east','west','search']
inventory = []

def game_loop():
    while True:
        global current_room
        print(
            f"You are in {current_room['desc']}"
        )
        print(
            f"This is the {current_room['name']}"
        )
        

        #TODO: refactor this so the logic isn't so messy.
        userInput =  ''
        while userInput not in directions or userInput == 'search':
            userInput = input('> ').lower().strip()
            if userInput in directions:
                if userInput in current_room and userInput != 'search':
                    current_room = rooms[current_room[userInput]]

                elif userInput == 'search' and 'search' not in current_room:
                    print("Nothing to search for.")
                    continue

                elif userInput == 'search' and 'search' in current_room:
                    global inventory
                    if current_room['search'] not in inventory:
                        inventory.append(current_room['search'])
                        print(f"You dig around and find {current_room['search_desc']}")
                    else:
                        print("Nothing else to find in current room.")


                else:
                    print("Can't go that way.")
                    ...
                    


if __name__ == "__main__":
   main()
