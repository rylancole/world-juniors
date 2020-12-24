import json

def main():
  with open('./draft-picks.json', 'r') as json_file:
    draft_data = json.loads(json_file.read())

  with open('./ep-player-data.json', 'r') as json_file:
    player_data = json.loads(json_file.read())

  md_file = open('./draft-picks.md', 'w')

  md_file.write("# Fantasy Rosters\n")

  for user in draft_data:
    roster = draft_data[user]
    player_map = {
      "F": [],
      "D": [],
      "G": []
    }

    for pick in roster:
      pos = player_data[pick]['pos']
      href = player_data[pick]['href']
      player_map[pos].append(f"- [{pick}]({href})\n")

    md_file.write(f"## {user}\n")

    for position in player_map:
      ls = player_map[position]
      
      md_file.write(f"### {position}\n")
      for p in ls:
        md_file.write(p)

if __name__ == "__main__":
  main()