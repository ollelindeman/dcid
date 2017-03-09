# dcid
A small program for deciding stuff by chance! Developed to solve the ever recurring problem of who should go and buy coffee for everyone. But the program can be used to cover a wide range of applications where you want to decide something by chance.

## Disclaimer
I would of course always help my friends and go willingly to buy them coffee, this is for the hypothetical situations which I'm sure arise elsewhere in the world.

## Basics
The "deciding process" is simply a game of _n_ number of rounds, where at each round every _player_ gets a score. The scores from each round are summed up and the final score ranks the players from first, the one with the highest score, to last, the one with the lowest score.

Here's an example of how to settle who should buy coffee between the players Olle, Martin and Philip:
```
$ python dcid.py Olle Martin Philip
Round   Olle    Martin  Philip
1       4       1       1
2       6       7       11
3       11      17      21
4       14      18      29
5       24      21      37
Results:
1. Philip   37
2. Olle     24
3. Martin   21
```
Now it's clear that Philip and Olle can stay in doors and wait comfortably for their coffees, while Martin have to walk the long long way to the coffee shop. You can of course make up your own rules, and the program basically just ranks players by their scores.

When the program runs, there is a default delay of 1 second between each round. This is there to add a thrilling component, so you can watch how one wins or loses. (I know, super fun right!?)

## Usage
```
python dcid.py [options] <names of players>
```
### Options
```
-t  Time between each round (default: 1).
-s  Score range each round (min:max, default: 1:10).
-n  Number of rounds (default: 5).
-h  Help, writes this text.
```
### Examples
Default game with four players:
```
$ python dcid.py Olle Nisse Jocke Kalle
```

Same game as above but with custom time, scores and rounds:
```
$ python dcid.py -t 5 -s 0:100 -n 3 Olle Nisse Jocke Kalle
```

## Installation
If you have python on your machine it's just to download the script and run it like the examples listed above.

### Hard core dcider
If you need this program daily it can be convinient to make it an executable and put it in your `/usr/local/bin`. This can be done by the following commands in the terminal (assuming you're on Linux/OS X):
```
$ cd [path-of-dcid.py]
$ cp dcid.py dcid
$ chmod a+x dcid
$ mv dcid /usr/local/bin/dcid
```
Now you can simply run the program from everwhere with just type `dcid` followed by the arguments!

