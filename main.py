from random import choice


def deal_card():
    deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return [choice(deck)]


def score(hand):
    tot_points = 0
    aces_count = 0
    # counting regular cards
    for card in hand:
        if card in ['J', 'Q', 'K']:
            points_to_add = 10
        elif card == 'A':
            points_to_add = 0
            aces_count += 1
        else:
            points_to_add = int(card)

        tot_points += points_to_add

    # Counting aces
    for i in range(aces_count):
        if (tot_points + 10) > 21:
            tot_points += 1
        else:
            tot_points += 10

    return tot_points


def continue_game(hand_player, hand_dealer):
    return score(hand_player) >= 21 or score(hand_dealer) >= 21


if __name__ == '__main__':
    hand_player = []
    hand_dealer = []

    hand_player += deal_card()
    # while continue_game(hand_player, hand_dealer)
