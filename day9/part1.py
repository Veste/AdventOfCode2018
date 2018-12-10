#in_players = 439
#in_last_marble = 71307
in_players = 1
in_last_marble = 200

MULTIPLE_TRIGGER = 23
CC_BACKUP = 7

marbles = [0]
cmi = 0 # current marble index
current_player = 0
scores = {x: 0 for x in range(in_players)}

for marble_val in range(1, in_last_marble + 1):
    if (marble_val % MULTIPLE_TRIGGER) != 0:
        next_mi = (cmi + 1) % len(marbles)
        insert_mi = next_mi + 1
        # Python insert actually handles index == len gracefully, so we don't need to check
        marbles.insert(insert_mi, marble_val)
        cmi = insert_mi
        print("      ", end="")
    else:
        backup_mi = (cmi - CC_BACKUP) % len(marbles)
        added_score = marble_val + marbles.pop(backup_mi)
        scores[current_player] += added_score
        print("{:5d}".format(added_score), end=" ")
        cmi = backup_mi
    # end if

    print("[{:4d}] ".format(marble_val), end="")
    for marble in marbles:
        if marble == marbles[cmi]:
            print('(' + "{:d}".format(marble) + ')', end="")
        else:
            print(" {:d} ".format(marble), end="")
        # end if
    # end for
    print()

    current_player = (current_player + 1) % in_players
# end for

print(scores)
print()
winning_score = max(zip(scores.values(), scores.keys()), key=lambda x: x[0])
print("Winning score is ({}, {})".format(winning_score[0], winning_score[1] + 1))

