def main():
    intro()

head_pounding = True
overdose = False

def intro():
    directions = ['front','left','right']
    print("""You wake up in a cold semi spherical contraption. A tub. That's what it's called.
The mostly smooth white veneer of, well, not porceline.
Your head is pounding as you clamber your way out of the tub with the grace of an ostrich.
There is a door directly in FRONT of you, a medicine cabinet on your LEFT, and a nearly identical door on your RIGHT.""")

    pill_count  = 0
    userInput = ''
    while userInput not in directions or userInput == 'left':
        userInput = input('> ').lower()
        if userInput == 'front':
            print("You approach the dark brown door, and grasp the brassing handle.")
            bedroom()
        
        elif userInput == 'right':
            print("You approach the dark brown door, and grasp the brassing handle.")
            livingroom()

        #need to add pills to inventory, and set up inventory system
        elif userInput == 'left':
            global head_pounding
            head_pounding = False
            print("You see a grizzy figure in the mirror. Your own reflection. It took you a minute to recognize yourself...")
            print("Reaching past the discheveled monument of human existance, you open the cabinet.")
            print("Inside you find a bottle, simply marked with tape and sharpie, 'pain KILLERS'")
            print("Against your better judgement, you open the bottle and take two oval shaped pills.")
            pill_count +=1
            
            if pill_count > 4:
                print("You are beginning to lose your balance, as the amphetimine high takes control.")
            if pill_count > 6:
                print("You passout on to the floor. A warm and familiar darkness sets in.")
                global overdose
                overdose = True
                #alternative method, will add only options to go into the doors
                bathroom_overdose()
            pass 


        
def bedroom():
    directions = ['dig','left','behind']
    print("""
You enter a space that feels like it has seen a thousand lifetimes.
None of those lifetimes have been cleaners, though...
But through the mess you can tell, at one point, this was a nice, enjoyable space.
You can DIG through your own filth, possibly find something useful. Now that you think about it, your vision is blurrier than you remember.
You can also see a door to your LEFT, and you can re-enter the bathroom BEHIND you.
""")
    userInput = ''
    while userInput not in directions:
        userInput = input('> ').lower()
        if userInput == 'behind':
            pass

        if userInput == 'dig':
            print("You search the room. Not finding much besides your ex's old hoodie, a fork that you do not recognize, and a pair of glasses.")
            print("You put on the glasses. It is uncertain if these are yours. Your vision remains blurry, but in a different way.")


main()

if __name__ == "__main__":
    main