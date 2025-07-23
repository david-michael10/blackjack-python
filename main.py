import art
logo = art.logo
import random

def deal_2_cards_user():
    for i in range(0,2):
        random_user_cards = random.choice(cards)
        user_cards.append(random_user_cards)
    user_sum = sum(user_cards)
    print(f"Your cards: {user_cards} | current score = {user_sum}")


def another_card_user():
    user_cards.append(random.choice(cards))

def another_card_pc():
    pc_cards.append(random.choice(cards))

def sum_user_cards():
    return sum(user_cards)

def sum_pc_cards():
    return sum(pc_cards)


def deal_2_cards_pc():
    for i in range(0, 2):
        random_pc_cards = random.choice(cards)
        pc_cards.append(random_pc_cards)
    pc_sum = sum(pc_cards)
    pc_first_card = pc_cards[0]
    print(f"Computer's first card: {pc_first_card}")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
pc_cards = []

def ace_1_or_11():
    for i in user_cards:
        if 11 in user_cards and sum_user_cards() > 21:
            user_cards.remove(11)
            user_cards.append(1)

    for i in pc_cards:
        if 11 in pc_cards and sum_pc_cards() > 21:
            pc_cards.remove(11)
            pc_cards.append(1)

choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()

if choice == "y":
    print("\n" * 50)
    print(logo)

    deal_2_cards_user()
    deal_2_cards_pc()
    print()

    new_card = True
    over = False
    while not over:
        while new_card:
            another_card_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            print()
            if another_card_choice == "y":
                another_card_user()
                if sum_user_cards() <= 21:
                    print(f"Your cards: {user_cards} | current score = {sum_user_cards()}")
                    print()

                    pc_first_card = pc_cards[0]
                    print(f"Computer's first card: {pc_first_card}")
                    print()

                ace_1_or_11()
                if sum_user_cards() > 21:
                    new_card = False
            else:
                new_card = False

        if sum_user_cards() > 21:
            over = True
            print("\n" * 20)
            print(f"Your Cards: {user_cards} | final score = {sum_user_cards()}")
            print(f"Computer cards: {pc_cards} | final score = {sum_pc_cards()}")
            print()
            print("You went over. You lose")
        else:
            pc_total_sum = sum(pc_cards)
            if pc_total_sum < sum_user_cards():
                while pc_total_sum < 17 and pc_total_sum < 21:
                    another_card_pc()
                    pc_total_sum = sum(pc_cards)

            ace_1_or_11()
            if sum_pc_cards() > 21:
                over = True
                print("\n" * 20)
                print(f"Your Cards: {user_cards} | final score = {sum_user_cards()}")
                print(f"Computer cards: {pc_cards} | final score = {sum_pc_cards()}")
                print()
                print("Opponent went over. You win")
            elif sum_pc_cards() > sum_user_cards():
                over = True
                print("\n" * 20)
                print(f"Your Cards: {user_cards} | final score = {sum_user_cards()}")
                print(f"Computer cards: {pc_cards} | final score = {sum_pc_cards()}")
                print()
                print("You lose")
            elif sum_user_cards() > sum_pc_cards():
                over = True
                print("\n" * 20)
                print(f"Your Cards: {user_cards} | final score = {sum_user_cards()}")
                print(f"Computer cards: {pc_cards} | final score = {sum_pc_cards()}")
                print()
                print("You win")
            else:
                over = True
                print("\n" * 20)
                print(f"Your Cards: {user_cards} | final score = {sum_user_cards()}")
                print(f"Computer cards: {pc_cards} | final score = {sum_pc_cards()}")
                print()
                print("Draw")