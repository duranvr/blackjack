import pandas as pd

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

def single_run():
    hand_player = deal_card() + deal_card()
    hand_dealer = deal_card() + deal_card()

    data_dict = {
        'dealer_score': score(hand_dealer[1]),
        'player_score': score(hand_player)
    }

    current_player_decision = 'hit'
    n_hits = 0
    while current_player_decision == 'hit' and score(hand_player) < 21:
        current_player_decision = choice(['hit', 'hit', 'hit', 'hold'])
        if current_player_decision == 'hit':
            hand_player += deal_card()
        n_hits += 1

    data_dict['n_hits'] = n_hits

    while get_dealer_hits(hand_player, hand_dealer):
        hand_dealer += deal_card()

    data_dict['success'] = 1 if calc_winner(hand_player, hand_dealer) == 'player' else 0
    return data_dict

if __name__ == '__main__':
    all_results_raw = pd.DataFrame([single_run() for _ in range(int(1e7))])
    all_results = all_results_raw.groupby(['dealer_score', 'player_score', 'n_hits']).agg(
        count=('success', 'count'),
        winner_prop=('success', 'mean'),
    )
    all_results = all_results.reset_index()