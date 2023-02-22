value_map = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


class Card:
    def __init__(self, card_value):
        self.value = value_map.get(card_value[0])
        self.symbol = card_value[1]


class Hand:
    def __init__(self, hand_value):
        self.cards = sorted([Card(card_value) for card_value in hand_value.split()], key=lambda x: x.value)
        self.rate = None
        self.equal_compare = None
        straight = self.is_straight()
        if straight:
            self.rate = 5
        flush = self.is_flush()
        if flush:
            self.rate = 6
        if straight and flush:
            if self.cards[-1].value == 14:
                self.rate = 10
                self.equal_compare = None
            else:
                self.rate = 9
                self.equal_compare = (self.cards[-1].value,)
        if self.rate:
            return
        if self.is_full_house():
            self.rate = 7
            return
        if self.is_four_of_a_kind():
            self.rate = 8
            return
        if self.is_three_of_a_kind():
            self.rate = 4
            return
        if self.is_two_pairs():
            self.rate = 3
            return
        if self.is_one_pair():
            self.rate = 2
            return
        self.rate = 1
        self.equal_compare = tuple(sorted([card.value for card in self.cards], reverse=True))

    def is_straight(self):
        for i in range(1, 5):
            if self.cards[i].value != self.cards[i - 1].value + 1:
                return False
        self.equal_compare = (self.cards[-1].value,)
        return True

    def is_flush(self):
        flush = all(card.symbol == self.cards[0].symbol for card in self.cards[1:])
        if flush:
            self.equal_compare = tuple(reversed([card.value for card in self.cards]))
        return flush

    def is_full_house(self):
        if self.cards[0].value == self.cards[1].value and self.cards[2].value == self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[-1].value, self.cards[0].value)
            return True
        if self.cards[0].value == self.cards[1].value == self.cards[2].value and self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[0].value, self.cards[-1].value)
            return True
        return False

    def is_four_of_a_kind(self):
        if self.cards[0].value == self.cards[1].value == self.cards[2].value == self.cards[3].value:
            self.equal_compare = (self.cards[0].value, self.cards[-1].value)
            return True
        if self.cards[1].value == self.cards[2].value == self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[-1].value, self.cards[0].value)
            return True
        return False

    def is_three_of_a_kind(self):
        if self.cards[0].value == self.cards[1].value == self.cards[2].value:
            self.equal_compare = (self.cards[0].value, self.cards[-1].value, self.cards[-2].value)
            return True
        if self.cards[1].value == self.cards[2].value == self.cards[3].value:
            self.equal_compare = (self.cards[1].value, self.cards[-1].value, self.cards[0].value)
            return True
        if self.cards[2].value == self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[2].value, self.cards[1].value, self.cards[0].value)
            return True
        return False

    def is_two_pairs(self):
        if self.cards[0].value == self.cards[1].value and self.cards[2].value == self.cards[3].value:
            self.equal_compare = (self.cards[2].value, self.cards[0].value, self.cards[-1].value)
            return True
        if self.cards[0].value == self.cards[1].value and self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[3].value, self.cards[0].value, self.cards[2].value)
            return True
        if self.cards[1].value == self.cards[2].value and self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[-1].value, self.cards[1].value, self.cards[0].value)
            return True

    def is_one_pair(self):
        if self.cards[0].value == self.cards[1].value:
            self.equal_compare = (self.cards[0].value, self.cards[4].value, self.cards[3].value, self.cards[2].value)
            return True
        if self.cards[1].value == self.cards[2].value:
            self.equal_compare = (self.cards[1].value, self.cards[4].value, self.cards[3].value, self.cards[0].value)
            return True
        if self.cards[2].value == self.cards[3].value:
            self.equal_compare = (self.cards[2].value, self.cards[4].value, self.cards[1].value, self.cards[0].value)
            return True
        if self.cards[3].value == self.cards[4].value:
            self.equal_compare = (self.cards[3].value, self.cards[2].value, self.cards[1].value, self.cards[0].value)
            return True


def player1_wins(player1_hand, player2_hand):
    if player1_hand.rate > player2_hand.rate:
        return True
    if player1_hand.rate < player2_hand.rate:
        return False
    for i, player1_card_value in enumerate(player1_hand.equal_compare):
        player2_card_value = player2_hand.equal_compare[i]
        if player1_card_value == player2_card_value:
            continue
        return player1_card_value > player2_card_value


count = 0
with open("54.txt", "r") as file:
    for game in file.readlines():
        game = game.strip()
        if player1_wins(Hand(game[:14]), Hand(game[15:])):
            count += 1
print(count)
