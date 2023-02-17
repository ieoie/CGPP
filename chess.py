#!/usr/bin/python3
from bs4 import BeautifulSoup
import datetime, os.path, re, requests

## Hacky script to d/l PGNs from ChessGames's
## Greatest of All Time pages. Saves each PGN into
## file based on decade

base_url = "https://www.chessgames.com";
decades = [
  "1000", # all time
  "1400", # prior to 1800
  "1800", # 1800-1899
  "1900", # 1900-1909
  "1910", # 1910-1919
  "1920", # 1920-1929
  "1930", # 1930-1939
  "1940", # 1940-1949
  "1950", # 1950-1959
  "1960", # 1960-1969
  "1970", # 1970-1979
  "1980", # 1980-1989
  "1990", # 1990-1999
  "2000", # 2000-2009
  "2010", # 2010-2019
  "2020"  # 2020-2029
]

def scrape_page(soup, decade):
  print("Scraping " + decade);
  for gid in soup.find_all("a", href=re.compile(r"gid")):
    gid_url = base_url + gid["href"]
    scrape_pgn(gid_url, decade);

def scrape_pgn(gid_url, decade):
  print("Scraping PGN");
  req2 = requests.get(gid_url);
  soup2 = BeautifulSoup(req2.content, "lxml")
  for pgn in soup2.find_all("div", id=re.compile(r"olga-data")):
    result = pgn["pgn"]
  with open(decade + ".pgn", "a") as file:
    print("Writing to file");
    file.write(result + "\n\n")

for decade in decades:
  print("Making Soup with " + decade);
  req = requests.get(base_url + "/perl/goat.pl?decade=" + decade);
  soup = BeautifulSoup(req.content, "lxml")
  scrape_page(soup, decade);
