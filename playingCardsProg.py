# Mario DeCristofaro
# lab 10


import random

# program just creates a deck of cards

class Card:
    def __init__(self, card_num):
        self.faceDown = True
        self.card_num = card_num
        if self.card_num >= 0 and self.card_num < 13:
            self.suit = "Spades"
            if card_num == 0:
                self.rank = "Ace"
                self.value = 11
            elif card_num == 1:
                self.rank = "1"
                self.value = 1
            elif card_num == 2:
                self.rank = "2"
                self.value = 2
            elif card_num == 3:
                self.rank = "3"
                self.value = 3
            elif card_num == 4:
                self.rank = "4"
                self.value = 4
            elif card_num == 5:
                self.rank = "5"
                self.value = 5
            elif card_num == 6:
                self.rank = "6"
                self.value = 6
            elif card_num == 7:
                self.rank = "7"
                self.value = 7
            elif card_num == 8:
                self.rank = "8"
                self.value = 8
            elif card_num == 9:
                self.rank = "9"
                self.value = 9
            elif card_num == 10:
                self.rank = "10"
                self.value = 10
            elif card_num == 11:
                self.rank = "Queen"
                self.value = 10
            elif card_num == 12:
                self.rank = "Jack"
                self.value = 10
            elif card_num == 13:
                self.rank = "King"
                self.value = 10
        elif card_num == self.card_num >= 13 and self.card_num < 26:
            self.suit = "Hearts"
            reset_num = card_num - 13
            if reset_num == 0:
                self.rank = "Ace"
                self.value = 11
            elif reset_num == 1:
                self.rank = "1"
                self.value = 1
            elif reset_num == 2:
                self.rank = "2"
                self.value = 2
            elif reset_num == 3:
                self.rank = "3"
                self.value = 3
            elif reset_num == 4:
                self.rank = "4"
                self.value = 4
            elif reset_num == 5:
                self.rank = "5"
                self.value = 5
            elif reset_num == 6:
                self.rank = "6"
                self.value = 6
            elif reset_num == 7:
                self.rank = "7"
                self.value = 7
            elif reset_num == 8:
                self.rank = "8"
                self.value = 8
            elif reset_num == 9:
                self.rank = "9"
                self.value = 9
            elif reset_num == 10:
                self.rank = "10"
                self.value = 10
            elif reset_num == 11:
                self.rank = "Queen"
                self.value = 10
            elif reset_num == 12:
                self.rank = "Jack"
                self.value = 10
            elif reset_num == 13:
                self.rank = "King"
                self.value = 10
        elif self.card_num >= 26 and self.card_num < 39:
            self.suit = "Clubs"
            reset_num = card_num - 26
            if reset_num == 0:
                self.rank = "Ace"
                self.value = 11
            elif reset_num == 1:
                self.rank = "1"
                self.value = 1
            elif reset_num == 2:
                self.rank = "2"
                self.value = 2
            elif reset_num == 3:
                self.rank = "3"
                self.value = 3
            elif reset_num == 4:
                self.rank = "4"
                self.value = 4
            elif reset_num == 5:
                self.rank = "5"
                self.value = 5
            elif reset_num == 6:
                self.rank = "6"
                self.value = 6
            elif reset_num == 7:
                self.rank = "7"
                self.value = 7
            elif reset_num == 8:
                self.rank = "8"
                self.value = 8
            elif reset_num == 9:
                self.rank = "9"
                self.value = 9
            elif reset_num == 10:
                self.rank = "10"
                self.value = 10
            elif reset_num == 11:
                self.rank = "Queen"
                self.value = 10
            elif reset_num == 12:
                self.rank = "Jack"
                self.value = 10
            elif reset_num == 13:
                self.rank = "King"
                self.value = 10
        elif self.card_num >= 39 and self.card_num <= 51:
            self.suit = "Diamonds"
            reset_num = card_num - 39
            if reset_num == 0:
                self.rank = "Ace"
                self.value = 11
            elif reset_num == 1:
                self.rank = "1"
                self.value = 1
            elif reset_num == 2:
                self.rank = "2"
                self.value = 2
            elif reset_num == 3:
                self.rank = "3"
                self.value = 3
            elif reset_num == 4:
                self.rank = "4"
                self.value = 4
            elif reset_num == 5:
                self.rank = "5"
                self.value = 5
            elif reset_num == 6:
                self.rank = "6"
                self.value = 6
            elif reset_num == 7:
                self.rank = "7"
                self.value = 7
            elif reset_num == 8:
                self.rank = "8"
                self.value = 8
            elif reset_num == 9:
                self.rank = "9"
                self.value = 9
            elif reset_num == 10:
                self.rank = "10"
                self.value = 10
            elif reset_num == 11:
                self.rank = "Queen"
                self.value = 10
            elif reset_num == 12:
                self.rank = "Jack"
                self.value = 10
            elif reset_num == 13:
                self.rank = "King"
                self.value = 10

    def __str__(self):
        if self.faceDown is True:
            return "FaceDown"
        elif self.faceDown is False:
            return self.rank + " " + "of" + " " + self.suit

    def face_down(self):
        self.faceDown = True

    def face_up(self):
        self.faceDown = False

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

if __name__ == "__main__":
    # Lets make a deck of cards
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        # flip over each card
        my_card.face_up()
        # print each card as we add them
        print(my_card)
        # print a random card from the deck
    print(random.choice(deck))
    # card number 37 is the queen of clubs
    card = Card(37)
    print(card)
    # Queen of Clubs
    print(card.get_value())
    # 10
    print(card.get_suit())
    # Clubs
    print(card.get_rank())
    # Queen
    card.face_down()
    print(card)
    # <facedown>
    card.face_up()
    print(card)
    # Queen of CLubs


# create chip bank Class
class ChipBank:
    # create initialize method and pass in parameter
    def __init__(self,value):
        # create balance variable
        self.balance = value
    # create a withdraw method, pass in amount as int
    def withdraw(self,amount):
        # use if statement for greater amount than balance in account
        if amount > self.balance:
            # create local variable for max amount that can be taken
            amount_taken = self.balance
            # set new balance to 0
            self.balance = 0
            # return max amount user can withdraw
            return amount_taken
        # for normal withdrawal
        else:
            #create new balance
            self.balance = self.balance - amount
            # return amount taken
            return amount

    # create deposit method
    def deposit(self,amount):
        # create new balance
        self.balance = self.balance + amount
    # create get_balance method
    def get_balance(self):
        return self.balance
    # create string method
    def __str__(self):
        # create variable set to balance
        chip_val = self.balance
        # use int division to get number of chips for each color
        self.black_chip = chip_val // 100
        # set new value to each chip
        chip_val %= 100
        self.green_chip = chip_val // 25
        chip_val %= 25
        self.red_chip = chip_val // 5
        chip_val %= 5
        self.blue_chip = chip_val // 1
        chip_val %= 1
        # return required str
        # set chip numbers to strings to concatenate
        return str(self.black_chip) + " " + "Black Chip(s)," + " " + \
            str(self.green_chip) + " " + "Green Chip(s)," + " " + \
            str(self.red_chip) + " " + "Red Chip(s)," + " " + \
            str(self.blue_chip) + " " + "Blue Chip(s)" + " " + \
            "Totaling" + " " + "$" + str(self.balance)
# Test code for ChipBank
cs = ChipBank(149)
print(cs)
cs.deposit(7)
print(cs.get_balance())
print(cs)
print(cs.withdraw(84))
print(cs)
cs.deposit(120)
print(cs)
print(cs.withdraw(300))