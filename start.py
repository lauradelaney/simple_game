def main():
    bathroom()

head_pounding = True

def bathroom():
    directions = ['front','left','right']
    print("""You wake up in a cold semi spherical contraption. A tub. That's what it's called.
    The mostly smooth white veneer of, well, not porceline.
    Your head is pounding as you clamber your way out of the tub with the grace of an ostrich.
    There is a door directly in FRONT of you, a medicine cabinet on your LEFT, and a nearly identical door on your RIGHT.""")

    userInput = ''
    while userInput not in directions:
        userInput = input('> ')
    
    



main()

if __name__ == "__main__":
    main