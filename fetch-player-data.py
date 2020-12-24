import requests
from bs4 import BeautifulSoup
import re
import json

def getSoup(url):
  response = requests.get(url)
  html = response.content
  
  return BeautifulSoup(html, 'html.parser')

def getPlayersFromSoup(players, soup):
  td_list = soup.find_all('td')

  for td in td_list:
    if td.get("class") == ['player']:
      a_list = td.find_all('a')
      for a in a_list:
        match = re.match('(.*)\s\((.*)\)', a.text)
        if match:
          name, pos = match.groups()
          if pos != "D": pos = 'F'
          players[name] = {
            "pos": pos,
            "href": a.get('href')
          }
        else:
          players[a.text] = {
            "pos": "G",
            "href": a.get('href')
          }

  return players


def main():
  players = {}

  for i in range(1, 4):
    soup = getSoup("https://www.eliteprospects.com/league/wjc-20/stats/2020-2021?page="+str(i))
    getPlayersFromSoup(players, soup)

  with open('./ep-player-data.json', 'w') as json_file:
    json_file.write(json.dumps(players, indent=4))

if __name__ == "__main__":
  main()