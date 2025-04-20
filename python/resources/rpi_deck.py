from rpi_card import Card, numbers, suits


class Deck:
    def __init__(self):
        self._cards = []
        self.populate()
        print(self._cards)

    def populate(self):
        self._cards = [Card(s, n) for s in suits for n in numbers]


deck = Deck()
