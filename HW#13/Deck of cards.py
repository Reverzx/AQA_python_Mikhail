import random


class Card:
    number_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King",
                   "Ace"]
    mast_list = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, number_list, mast_list):
        self.number_list = number_list
        self.mast_list = mast_list


class CardsDeck:

    def __init__(self):
        self.deck = []
        self.number_list = Card.number_list
        self.mast_list = Card.mast_list
        for i in self.number_list:
            for j in self.mast_list:
                self.deck.append(f'{i} of {j}')

    def shuffle(self):
        random.shuffle(self.deck)


deck = CardsDeck()
deck.shuffle()
while True:
    try:
        card_number = int(input('Выберите карту из колоды в 52 карт:'))
        if 1 <= card_number <= 52:
            break
        print("Ошибка: Введите число от 1 до 52.")
    except ValueError:
        print("Ошибка: Введите число!")

print(f'You card is: {deck.deck[card_number - 1]}')
