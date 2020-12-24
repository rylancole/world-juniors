import requests
from bs4 import BeautifulSoup

def main():
  response = requests.get("https://www.eliteprospects.com/ajax/team.player-stats?teamId=1618&season=2020-2021&position=")
  html = response.content
  
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.find_all('a')
  print(links)

if __name__ == "__main__":
  main()