from collections import deque, defaultdict

in_players = 439
in_last_marble = 7130700

MULTIPLE_TRIGGER = 23
CC_BACKUP = 7

scores = defaultdict(int)
marbles = deque([0])
current_player = 0

for marble_val in range(1, in_last_marble + 1):
    if marble_val % MULTIPLE_TRIGGER == 0:
        marbles.rotate(7)
        scores[current_player] += marble_val + marbles.pop()
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(marble_val)
    # end if

    current_player = (current_player + 1) % in_players
# end for

max_score = max(scores.values())
print(max_score)
