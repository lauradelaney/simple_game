def main():
    intro()

head_pounding = True
overdose = False
inventory = []
room_count = 0

def roomcount():
    global room_count
    room_count += 1

def intro():
    directions = ['south','east','west']
    print("""You wake up in a cold semi spherical contraption. A tub. That's what it's called.
The mostly smooth white veneer of, well, not porceline.
Your head is pounding as you clamber your way out of the tub with the grace of an ostrich.
There is a door directly in SOUTH of you, a medicine cabinet to your EAST, and a nearly identical door on your WEST.""")

    pill_count  = 0
    userInput = ''
    while userInput not in directions or userInput == 'east':
        userInput = input('> ').lower().strip()
        if userInput == 'south':
            print("You approach the dark brown door, and grasp the brassing handle.")
            roomcount()
            bedroom()
        
        elif userInput == 'west':
            print("You approach the dark brown door, and grasp the brassing handle.")
            roomcount()
            livingroom()

        elif userInput == 'east':
            global head_pounding
            head_pounding = False
            print("You see a grizzy figure in the mirror. Your own reflection. It took you a minute to recognize yourself...")
            print("Reaching past the discheveled monument of human existance, you open the cabinet.")
            print("Inside you find a bottle, simply marked with tape and sharpie, 'pain KILLERS'")
            print("Against your better judgement, you open the bottle and take two oval shaped pills.")
            pill_count +=1
            global inventory
            inventory.append('pills')
            
            if pill_count > 4:
                print("You are beginning to lose your balance, as the amphetimine high takes control.")
            if pill_count > 6:
                print("You passout on to the floor. A warm and familiar darkness sets in.")
                global overdose
                overdose = True
                if 'pills' in inventory:
                    inventory.remove('pills')
                bathroom()
            pass 

def bathroom():
    directions = ['south','west']
    if 'glasses' in inventory:
        print("A subtle smell of muskiness enters your nose. The chipped and broken tiles now catch your eye.")
        print("The tub... you can barely stand to look at it.")
        print("There is a door to the SOUTH, and a door to the WEST.")
    elif 'glasses' not in inventory:
        print("A subtle smell of muskiness enters your nose.")
        print("There is a door to the SOUTH, and a door to the WEST.")

    userInput = ''
    while userInput not in directions:
        userInput = input('> ').lower().strip()
        if userInput == 'south':
            roomcount()
            bedroom()
        if userInput == 'west':
            roomcount()
            livingroom()



def bedroom():
    directions = ['dig','west','north','south']
    print("""
You enter a space that feels like it has seen a thousand lifetimes.
None of those lifetimes have been cleaners, though...
But through the mess you can tell, at one point, this was a nice, enjoyable space.
You can DIG through your own filth, possibly find something useful. Now that you think about it, your vision is blurrier than you remember.
You can also see a door to your NORTH, and one WEST of you.
""")
    userInput = ''
    while userInput not in directions or userInput == 'dig':
        userInput = input('> ').lower().strip()
        if userInput == 'north':
            roomcount()
            bathroom()

        elif userInput == 'dig':
            print("You search the room. Not finding much besides your ex's old hoodie, a fork that you do not recognize, and a pair of glasses.")
            print("You put on the glasses. It is uncertain if these are yours. Your vision remains blurry, but in a different way.")
            print("Now that you can, somewhat, see, the painting on the SOUTH wall stands out to you.")
            global inventory
            if 'glasses' not in inventory:
                inventory.append('glasses')
                continue
            continue

        elif userInput == 'west':
            roomcount()
            livingroom()

        elif userInput == 'south':
            print('Moving the bookshelf off the wall, a door appears.')
            roomcount()
            secretroom()


def livingroom():
    directions =  ['north east', 'south east', 'south', 'west']
    print("A dark, depressing, scene unfolds in front of you.")
    print("Garbage. You are a garbage human being.")
    print("There is a door to your NORTH EAST, another to your SOUTH EAST, one directly SOUTH, and one to the WEST of you.")
    userInput = ''
    while userInput not in directions or userInput == 'south':
        userInput = input('> ').lower().strip()

        if userInput == 'north east':
            bathroom()
        
        elif userInput == 'south east':
            bedroom()

        elif userInput == 'south':
            if room_count < 3:
                print('You grab the handle and feel a sharp pain shoot through your forehead.')
                print('You stumble back, nearly tripping over the... is that a coffee table under all of that clutter?')
                print('Maybe you should check more rooms you think to yourself. The outside world seems scary.')
                continue
            elif  room_count > 3:
                hallway()
            

        elif userInput == 'west':
            kitchen()


livingroom()
#main()

if __name__ == "__main__":
    main