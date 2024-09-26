import random


def shuffle_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{value} of {suit}" for suit in suits for value in values]
    random.shuffle(deck)
    return deck


def magic_card_trick():
    deck = shuffle_deck()
    print("Welcome to the Magic Card Trick!")
    print("I have shuffled a deck of cards.")

    print("\nPick a card from the shuffled deck, but don't tell me what it is.")
    input("Press Enter when you have your card in mind...")

    guessed_card = random.choice(deck)
    print(f"Is your card the {guessed_card}?")
    response = input("Was I correct? (yes/no): ").strip().lower()

    if response == 'yes':
        print("I knew it! Magic never fails!")
    else:
        print("Oops! Looks like the magic got tricky this time. Let's try again!")


if __name__ == "__main__":
    magic_card_trick()
