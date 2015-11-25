#!/usr/bin/python

import sys
import time
import random

# Interval of possible values
min_val = 1
max_val = 10

# Default number of rounds
num_rounds = 5

# Time between each round (seconds)
sleep_time = 1

# Function for printing out well formated columns
def print_cols(cols, width):
    print "".join(str(col).ljust(width) for col in cols)

if __name__ == "__main__":

    # Check arguments
    if(len(sys.argv) < 2):
        raise ValueError("Invalid arguments!\n Usage: dcid Player1 Player2 ... Player N")

    # Read players
    players = sys.argv[1:]
    scores  = [0] * len(players)

    # Gets largest name (for formatting purpuses)
    max_width = max(len(name) for name in players) + 2 # padding

    # Print header line
    print_cols(["Round"] + players, max_width)

    # For each round
    for r in range(num_rounds):

        for p in range(len(players)):
            scores[p] += random.randint(min_val, max_val)

        print_cols([r+1] + scores, max_width)

        time.sleep(sleep_time)

    # Print out result
    placement = 1
    print "Results:"
    for (i,s) in sorted(enumerate(scores), key=lambda x: -x[1]):
        print "%d. %s %d" % (placement, players[i].ljust(max_width), s)
        placement += 1
