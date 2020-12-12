from random import shuffle, randint, choice


class Card:
    def __init__(self, couleur: str, valeur: str):
        self.suit = couleur
        self.v = valeur

    def __str__(self):
        return f"{self.suit}{self.v}"


class DeckCards:
    def __init__(self):
        self.deck = []
        for suit in ["S", "H", "C", "D"]:
            for i in ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K"]:
                self.deck.append(Card(suit, i))

    def shuffle_cards(self):
        shuffle(self.deck)

    def get_card_from_index(self, index):
        return self.deck[index]

    def __str__(self):
        msg = ""
        counter = 0
        for card in self.deck:
            counter += 1
            msg += str(card)
            msg += "\n" if counter % 13 == 0 else " "
        return msg

    def draw_card(self):
        return self.deck.pop()


def good(hand):
    suits = []
    for item in hand:
        suits.append(item.suit)
    return suits.count("H") > 0


if __name__ == "__main__":
    cas_favorables = 0
    n = 100000

    for _ in range(n):
        deck = DeckCards()
        deck.shuffle_cards()
        a, b, c, d, e = randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31)

        hand = [deck.get_card_from_index(i) for i in [a, b, c, d, e]]
        if good(hand):
            cas_favorables += 1

    print((cas_favorables / n) * 100, "%", sep="")

"""
deck = DeckCards()
print(deck)
print("*"*26)
deck.shuffle_cards()
print(deck)
print("*"*26)

for _ in range(10):
    print(f"Carte tirêe : {deck.draw_card()}")

print("*"*26)
print(deck)
"""
