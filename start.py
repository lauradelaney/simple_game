def main():
    bathroom()

head_pounding = True
overdose = False

def bathroom():
    directions = ['front','left','right']
    print("""You wake up in a cold semi spherical contraption. A tub. That's what it's called.
The mostly smooth white veneer of, well, not porceline.
Your head is pounding as you clamber your way out of the tub with the grace of an ostrich.
There is a door directly in FRONT of you, a medicine cabinet on your LEFT, and a nearly identical door on your RIGHT.""")

    pill_count  = 0
    userInput = ''
    while userInput not in directions or userInput == 'left':
        userInput = input('> ').lower()
        print(f'-------------DEV: {userInput}')
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




main()
print(f'-----------DEV: {head_pounding}')

if __name__ == "__main__":
    main