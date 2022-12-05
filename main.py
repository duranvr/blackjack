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
        if (tot_points + 11) > 21:
            tot_points += 1
        else:
            tot_points += 11

    return tot_points


def calc_winner(hand_player, hand_dealer):
    score_player = score(hand_player)
    score_dealer = score(hand_dealer)

    if score_player > 21:
        winner = 'dealer'
    elif score_dealer > 21:
        winner = 'player'
    elif score_player < score_dealer:
        winner = 'dealer'
    elif score_player > score_dealer:
        winner = 'player'
    else:
        winner = 'draw'

    return winner


def get_player_decision():
    decision_number = int(input('1: hit, 2: hold'))
    if decision_number == 1:
        return 'hit'
    else:
        return 'hold'


def get_dealer_hits(hand_player, hand_dealer):
    score_player = score(hand_player)
    score_dealer = score(hand_dealer)

    dealer_hits = True
    if score_player > 21:
        dealer_hits = False
    elif score_dealer > score_player:
        dealer_hits = False
    elif score_dealer == 21:
        dealer_hits = False

    return dealer_hits


def run():
    hand_player = deal_card() + deal_card()
    hand_dealer = deal_card() + deal_card()

    print(f'Dealer Hand: [XXX, {hand_dealer[1:]}')
    current_player_decision = 'hit'
    while current_player_decision == 'hit' and score(hand_player) < 21:
        print(f'Player Hand: {hand_player}')
        current_player_decision = get_player_decision()
        if current_player_decision == 'hit':
            hand_player += deal_card()

    while get_dealer_hits(hand_player, hand_dealer):
        hand_dealer += deal_card()

    print(f'Final Player Hand: {hand_player}')
    print(f'Player Score: {score(hand_player)}')
    print(f'Final Dealer Hand: {hand_dealer}')
    print(f'Dealer Score: {score(hand_dealer)}')
    print(f'Winner is: {calc_winner(hand_player, hand_dealer)}')

if __name__ == '__main__':
    run()

