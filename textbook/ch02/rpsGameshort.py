import random

def play_rock_paper_scissors():
    print('ROCK, PAPER, SCISSORS')
    wins = 0
    losses = 0
    ties = 0

    while True:
        print(f"{wins} wins, {losses} Losses, {ties} Ties")
        print('Enter your move: (1) PAPER (2) SCISSORS or (q)uit')
        player_move = input()
        
        if player_move == 'q':
            break
        if player_move not in ['1', '2']:
            print('Type 1, 2, or q.')
            continue
        
        player_move = int(player_move)
        computer_move = random.randint(1, 2)

        if player_move == computer_move:
            print('It is a tie!')
            ties += 1
        elif player_move % 3 == computer_move % 3 + 1:
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1

play_rock_paper_scissors()
