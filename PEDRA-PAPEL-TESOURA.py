import random

def get_choices():
    player_choice = input("Faça uma escolha (pedra, papel, tesoura): ")
    options = ["pedra", "papel", "tesoura"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"Você escolheu {player}, contra {computer}")
    if player == computer:
        return "Empatou!!!" 
    elif player == "pedra":
        if computer == "tesoura":
            return "Pedra quebra tesoura, Você ganhou!"
        else:
            return "Papel cobre pedra, Você perdeu!"
    elif player == "papel":
        if computer == "pedra":
            return "Papel cobre pedra, Você ganhou!"
        else:
            return "Tesoura corta papel, Você perdeu!"
    elif player == "tesoura":
        if computer == "papel":
            return "Tesoura corta papel, Você ganhou!"
        else:
            return "Pedra quebra tesoura, Você perdeu!"
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)