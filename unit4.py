# by Xander Eagle
# October 11, 2019
# this program simulates a blackjack game
import random


def card():
    """
    randomizes the card
    :return: a number between 1 and 10
    """
    return random.randint(1, 10)


def dealer():
    """
    simulates the dealers hand with 2 cards
    :return: the dealers total hand
    """
    dealer_card_1 = card()
    dealer_card_2 = card()
    print("The dealer drew a", dealer_card_1, "and a", dealer_card_2)
    dealer_total = dealer_card_1 + dealer_card_2
    print("The dealer's total is", dealer_total)
    return dealer_total


def who_wins(dealer_total, user_total):
    """
        uses if statements to tell the user who wins
        :return: the dealers total hand
        """
    if dealer_total > user_total:
        print("The dealer wins! Good try.")
    elif dealer_total < user_total:
        print("You win!")
    elif dealer_total == user_total:
        print("You tied the dealer. Wow that is pretty rare.")


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
        print("You drew a", user_card_3)
        print("Your new total is", user_total)
    if user_total > 21:
        print("You lose!")
    else:
        dealer_total = dealer()
        who_wins(dealer_total, user_total)


main()
