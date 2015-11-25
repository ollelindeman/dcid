#!/usr/bin/python

import sys
import getopt
import time
import random

# Function for printing out well formated columns
def print_cols(cols, width):
    print "".join(str(col).ljust(width) for col in cols)

def print_help():
    print 'dcid.py [options] <names of players>'
    print 'OPTIONS:'
    print '\t-t\tTime between each round (default: 1).'
    print '\t-s\tScore range each round (min:max, default: 1:10).'
    print '\t-n\tNumber of rounds (default: 5).'
    print '\t-h\tHelp, writes this text.'
    print 'EXAMPLES:'
    print '\tDefault game with four players:\n'
    print '\t\tdicd.py Olle Nisse Jocke Kalle\n'
    print '\tSame game, but with custom time and scores:\n'
    print '\t\tdcid.py -t 5 -s 0:100 Olle Nisse Jocke Kalle\n'

def main(argv):

    # Interval of possible values
    min_val = 1
    max_val = 10

    # Default number of rounds
    num_rounds = 5

    # Time between each round (seconds)
    sleep_time = 1

    # Parse input arguments
    try:
        opts, args = getopt.getopt(argv,"ht:s:n:")
    except getopt.GetoptError:
        print "Invalid arguments!"
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-t':
            sleep_time = int(arg)
        elif opt == '-n':
            num_rounds = int(arg)
        elif opt == "-s":
            min_val, max_val = (int(s) for s in arg.split(":"))

    # Read players
    players = args
    scores  = [0] * len(players)

    # Gets largest name (for formatting purpuses)
    max_width = max(len(name) for name in players) + 2 # padding

    # Print header line
    print_cols(["Round"] + players, max_width)

    # For each round
    for r in range(num_rounds):
        time.sleep(sleep_time)
        for p in range(len(players)):
            scores[p] += random.randint(min_val, max_val)

        print_cols([r+1] + scores, max_width)

    # Print out result
    placement = 1
    print "Results:"
    for (i,s) in sorted(enumerate(scores), key=lambda x: -x[1]):
        print "%d. %s %d" % (placement, players[i].ljust(max_width), s)
        placement += 1

if __name__ == "__main__":
    main(sys.argv[1:])
