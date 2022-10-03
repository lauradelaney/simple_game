def main():
    game_loop()


rooms = {
    'bathroom': {
        'name': 'bathroom',
        'desc': 'a room that smells truly damp',
        'north': 'hallway',
    }
}

current_room = rooms['bathroom']
directions = ['north','south','east','west']

def game_loop():
    while True:
        global current_room
        print(
            f"You are in {current_room['desc']}"
        )
        print(
            f"This is the {current_room['name']}"
        )
        
        userInput =  ''
        while userInput not in directions:
            userInput = input('> ').lower().strip()
            if userInput in directions:
                if userInput in current_room:
                    current_room = rooms[current_room[userInput]]
                    print(current_room)
                    break
                else:
                    continue

game_loop()

#if __name__ == "__main__":
#   main()
