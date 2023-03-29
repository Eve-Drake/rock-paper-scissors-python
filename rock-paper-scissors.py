import random

def play(): 
    playAgain = True
    while(playAgain):
        choiceList = ['r' , 'p', 's']    
        computerChoice = random.choice(choiceList)
        print(computerChoice)
        userChoice = input('Rock - r, Paper - p, Scissors - s!...')
        if(userChoice == computerChoice):
            print(f' I also chose {computerChoice}. We tied!')
        
        if(userChoice == 'r'):
            if(computerChoice == 's'):
                print(f'You win. I chose {computerChoice}')
            elif(computerChoice == 'p'):
                print(f'I win. I chose {computerChoice}')

        if(userChoice == 'p'):
            if(computerChoice == 's'):
                print(f'I win. I chose {computerChoice}')
            elif(computerChoice == 'r'):
                print(f'You win. I chose {computerChoice}')


        if(userChoice == 's'):
                if(computerChoice == 'r'):
                    print(f'You win. I chose {computerChoice}')
                elif(computerChoice == 'p'):
                    print(f'I win. I chose {computerChoice}')
        playChoice = input('Do you want to play again? y or n')
        if(playChoice == 'n'):
            playAgain(False)

play()