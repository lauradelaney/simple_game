def main():
    game_loop()


rooms = {
    'bathroom': {
        'name': 'bathroom',
        'desc': 'a room that smells truly damp. There is a slightly ajar door to the SOUTH.',
        'south': 'bedroom',
        'search': 'Glasses',
        'search_desc': 'You find a pair of glasses scattered across the floor.'        
    },

    'bedroom': {
        'name': 'bedroom',
        'desc': '',
        'north': 'bathroom',
        'west': 'hallway'
    }

}

current_room = rooms['bathroom']
directions = ['north','south','east','west','search']
inventory = []

def game_loop():
    #want to fix this so only the input gets repeated and not this whole section.
    while True:
        global current_room
        print(
            f"You are in {current_room['desc']}"
        )
        print(
            f"This is the {current_room['name']}"
        )
        

        #need to refactor this so the logic isn't so messy.
        userInput =  ''
        while userInput not in directions:
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
                    print("Can't go that way.")
                    ...
                    


if __name__ == "__main__":
   main()
