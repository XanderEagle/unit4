import random


def card():
    return random.randint(1, 10)


def main():
    user_card_1 = card()
    user_card_2 = card()
    print("You drew a", user_card_1, "and a", user_card_2)
    user_total = user_card_1 + user_card_2
    print("Your total is", user_total)
    another_card = input("Would you like another card?")
    if another_card == "yes":
        user_card_3 = card()
        user_total += user_card_3
    print(user_total)

def dealer():
    dealer_card_1 = card()
    dealer_card_2 = card()


main()
