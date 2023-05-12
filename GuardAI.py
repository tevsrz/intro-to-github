choice = input('Does the guard see the player (y/n)? ')
if choice == 'n':
    see_player = False
    print('The guard waits')
else:
    dist_from_player = int(input('How far away is the player? '))
    if dist_from_player <= 1:
            print('The guard attacks')
    elif 2<= dist_from_player <=4:
            print('The guard advances')
    elif dist_from_player >=5:
            print('The guard waits.')



    
    
