import requests
from bs4 import BeautifulSoup
import re
import json

def getSoup(url):
  response = requests.get(url)
  html = response.content
  
  return BeautifulSoup(html, 'html.parser')

def handleTd(obj, td):
  cl = td.get('class')

  if cl == ['player']:
    a_list = td.find_all('a')
    for a in a_list:
      match = re.match('(.*)\s\((.*)\)', a.text)
      if match:
        name, pos = match.groups()
        if pos != "D": pos = 'F'
        obj["name"] = name
        obj["pos"] = pos
      else:
        obj["name"] = a.text
        obj["pos"] = "G"
      obj["href"] = a.get('href')

  elif cl == ['team']:
    a_list = td.find_all('a')
    for a in a_list:
      match = re.match(' (.*) U20', a.text)
      if match:
        obj["team"] = match.group(1)

def getPlayersFromSoup(players, soup):
  tr_list = soup.find_all('tr')

  for tr in tr_list:
    td_list = tr.find_all('td')

    player_obj = {}

    for td in td_list:
      handleTd(player_obj, td)

    if player_obj and "name" in player_obj.keys():
      players[player_obj["name"]] = player_obj

def main():
  players = {}

  for i in range(1, 4):
    soup = getSoup("https://www.eliteprospects.com/league/wjc-20/stats/2020-2021?page="+str(i))
    getPlayersFromSoup(players, soup)

  with open('./ep-player-data.json', 'w') as json_file:
    json_file.write(json.dumps(players, indent=4))

if __name__ == "__main__":
  main()