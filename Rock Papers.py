import random
while(1!=0):
    def is_win(player,opponent):
        if ((player=='r' and opponent=='s') or (player=='s' and opponent=='p') \
        or (player=='p' and opponent=='r')):
        return True

    def play():
        Poss = ['s', 'p', 'r']
        C_choice = random.choice(Poss)
        P_choice = input("Rock(R),Siscors(S) or Paper(P):").lower()
        print(f"Your choice is {P_choice} and Computer's is {C_choice}")
        if P_choice == C_choice:
            return 'Draw'
        if is_win(P_choice,C_choice):
            return 'You Win'
        return'Computer Wins'
    
    print(play())
