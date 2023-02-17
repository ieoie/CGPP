# CGPP: ChessGames PGN Project

A python script to scrape PGN files of "Notable Chess Games" from the ChessGames.com website. Requires the Beautiful Soup library.

## How it works

1. An array defines the valid ```decade``` query strings available on the site
2. Loads page at ```https://www.chessgames.com/perl/goat.pl?decade=VARIABLE```, where ```VARIABLE``` is the first value in the array
3. Scrapes the PGN data and appends it to a file for each decade, e.g. 1930.pgn
4. Loads a new page using the next value in the array

## Usage

Make the script executable and run at the command line.
