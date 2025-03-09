import random


class Card:
    number_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                   "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    mast_list = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, number_list, mast_list):
        self.number_list = number_list
        self.mast_list = mast_list

    def __repr__(self):
        return f"{self.number_list} of {self.mast_list}" if self.mast_list != "None" \
            else self.number_list


class CardsDeck:

    def __init__(self):
        self.cards = [Card(number, mast) for mast in Card.mast_list for number in Card.number_list]
        self.cards.append(Card("Joker", "None"))
        self.cards.append(Card("Joker", "None"))

    def shuffle(self):
        random.shuffle(self.cards)


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

print(f'You card is: {deck.cards[card_number]}')
