import json

def main():
  with open('../json/draft-picks.json', 'r') as json_file:
    draft_data = json.loads(json_file.read())

  with open('../json/ep-player-data.json', 'r') as json_file:
    player_data = json.loads(json_file.read())

  team_data = {}

  for user in draft_data:
    for player in draft_data[user]:
      team = player_data[player]['team']
      if team in team_data.keys():
        team_data[team].append(player)
      else:
        team_data[team] = [player]
  
  print(json.dumps(team_data, indent=4))


if __name__ == "__main__":
  main()