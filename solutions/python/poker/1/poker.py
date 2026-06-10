from collections import Counter as c
def best_hands(hands):
    def _score(hand):
        straight_flush = 8
        four_of_a_kind = 7
        full_house = 6
        flush = 5
        straight = 4
        three_of_a_kind = 3
        two_pair = 2
        one_pair = 1
        high_card = 0

        ranks, suits, counts, is_flush, is_straight = _classify(hand)
        if set(ranks) == {2, 3, 4, 5, 14}:
            ranks = [1,2,3,4,5]
            counts = c(ranks)
            
        sorted_ranks = sorted(ranks, key=lambda r: (counts[r], r), reverse=True)
        if is_flush and is_straight:
            hand_rank = straight_flush
        elif is_flush:
            hand_rank = flush
        elif is_straight:
            hand_rank = straight
        elif 4 in counts.values():
            hand_rank = four_of_a_kind
        elif 3 in counts.values():
            if 2 in counts.values():
                hand_rank = full_house
            else:
                hand_rank = three_of_a_kind
        elif 2 in counts.values():
            if len(counts) == 3:
                hand_rank = two_pair
            else:
                hand_rank = one_pair
        else:
            hand_rank = high_card
    
        return hand_rank, tuple(sorted_ranks)
    
    def _parse(hand):
        RANKS = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
         '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        result = []
        for hnd in hand.split(' '):
            result.append((RANKS[hnd[:-1]], hnd[-1]))
        return result

    def _classify(hand):
        cards = _parse(hand)
        ranks = sorted([item[0] for item in cards])
        suits = [item[1] for item in cards]
        counts = c(ranks)
        is_flush = len(set(suits)) == 1
        is_straight = ((max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5) 
               or set(ranks) == {2, 3, 4, 5, 14})
        return ranks, suits, counts, is_flush, is_straight

    scores = {hand: _score(hand) for hand in hands}
    best = max(scores.values())
    return [hand for hand, score in scores.items() if score == best]