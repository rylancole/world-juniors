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
      team = player_data[pick]['team']

      if pos == "G":
        player_map[pos].append(f"| [{pick}]({href}) | {pos} | {team} | | | | | | |\n")
      else:
        player_map[pos].append(f"| [{pick}]({href}) | {pos} | {team} | | | | | | |\n")

    md_file.write(f"## {user}\n")
    md_file.write(f"| Player | Pos | Team | G | A | SOG | PIM | +\- | TPM |\n")
    md_file.write(f"| :----- | --- |  --- | - | - | --- | --- | --- | --: |\n")

    
    skaters = player_map["F"]
    skaters.extend(player_map["D"])

    for sk in skaters:
      md_file.write(sk)

    md_file.write(f"\n| Player | Pos | Team | S% | GAA |\n")
    md_file.write(f"| :----- | --- |  --- | -- | --: |\n")

    goalies = player_map["G"]
    for g in goalies:
      md_file.write(g)

if __name__ == "__main__":
  main()