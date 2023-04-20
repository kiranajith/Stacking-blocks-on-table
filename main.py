from rwa3 import RWA3
from inputs import prompt_user


if __name__ == "__main__":
    clr =[]
    input = prompt_user()
    for ch in input:
        if ch =='r':
            clr.append('red')
        if ch =='g':
            clr.append('green')
        if ch =='b':
            clr.append('blue')
    bottom = clr[0]
    middle = clr[1]
    top = clr[2]        
    arm = RWA3(bottom,middle,top)
    initial_bottom, initial_middle, initial_top = arm.config()
    if clr == arm.config():
        print('Final configuration already reached...exit')
        exit()


    print('---- initial Configuration ----\n')
    arm.print_configuration()
    
    arm.move(initial_bottom, initial_middle, initial_top)

    print('\n---- final configuration ----\n')
    arm.print_configuration()


