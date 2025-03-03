import random

def card_dealer():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculating_results(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(score_user, dealer_score):
    if score_user == dealer_score:
        return "its a draw"
    elif dealer_score == 0:
        return "you lost dealer has a BlackJack ,better luck next time"
    elif score_user == 0:
        return "congratulation you win "
    elif dealer_score > 21:
        return "congratulation you win"
    elif score_user > 21 :
        return "you lost better luck next time"
    elif score_user > dealer_score:
        return "congratulation you win"
    else:
        return "you lost better luck next time"

def play_game():
    user_cards = []
    computer_cards = []
    dealers_score = -1
    user_score = -1
    game_over = False

    for x in range(2):
        user_cards.append(card_dealer())
        computer_cards.append(card_dealer())


    while not game_over :
        user_score = calculating_results(user_cards)
        dealers_score = calculating_results(computer_cards)
        print(f"you card is {user_cards},currect score {(user_score)}")
        print(f"dealers card is {computer_cards[0]}")

        if user_score == 0 or dealers_score == 0 or user_score > 21:
                game_over = True

        else:
            stand = input('Do you want to get another card, type y to get another or s to pass : ')
            if stand == "y":
                user_cards.append(card_dealer())
            else:
                game_over = True


    while dealers_score != 0 and dealers_score < 17:
        computer_cards.append(card_dealer())
        dealers_score = calculating_results(computer_cards)

    print(f"your final hand:{user_cards},your score is: {user_score}")
    print(f"dealers final hand:{computer_cards},dealers score is: {dealers_score}")
    print(compare(user_score,dealers_score))

while input("do you want to play BlackJack type yes or no : ") == "yes":
    print("\n" * 20)
    play_game()




