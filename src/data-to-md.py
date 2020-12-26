import json
import re

def validatePick(pick):
  KEYS = [
    "href",
    "team",
    "pos"
  ]

  for k in KEYS:
    if k not in pick.keys():
      print(f"\n### ERROR: Missing {k}")
      print()
      print(json.dumps(pick, indent=4))
      return False

  return True

def main():
  with open('../json/draft-picks.json', 'r') as json_file:
    draft_data = json.loads(json_file.read())

  with open('../json/ep-player-data.json', 'r') as json_file:
    player_data = json.loads(json_file.read())

  md_file = open('../ROSTERS.md', 'w')

  md_file.write("# Fantasy Rosters\n")

  ranking_data = {}

  for user in draft_data:
    roster = draft_data[user]
    player_map = {
      "F": [],
      "D": [],
      "G": []
    }

    g_total = 0
    a_total = 0
    pim_total = 0
    pm_total = 0

    gaa_list = []
    svp_list = []

    for pick in roster:

      if validatePick(player_data[pick]):

        href = player_data[pick]['href']
        pos = player_data[pick]['pos']
        team = player_data[pick]['team']

        if pos == "G":
          gaa = player_data[pick]['gaa']
          svp = player_data[pick]['svp']

          if re.match('[\d\.]+', gaa): gaa_list.append(float(gaa)) 
          if re.match('[\d\.]+', svp): svp_list.append(float(svp)) 

          player_map[pos].append(f"| [{pick}]({href}) | {pos} | {team} | {svp} | {gaa} |\n")
        else:
          g = player_data[pick]['g']
          a = player_data[pick]['a']
          pim = player_data[pick]['pim']
          pm = player_data[pick]['pm']

          if re.match('\d+', g): g_total += int(g)
          if re.match('\d+', a): a_total += int(a)
          if re.match('\d+', pim): pim_total += int(pim)
          if re.match('\-?\d+', pm): pm_total += int(pm)

          player_map[pos].append(f"| [{pick}]({href}) | {pos} | {team} | {g} | {a} | | {pim} | {pm} | |\n")

    ranking_data[user] = {
      "Goals": g_total,
      "Assists": a_total,
      "Penalties in Minutes": pim_total,
      "Plus / Minus": pm_total,
      "Save Percentage": max(svp_list) if svp_list else '-',
      "Goals Against Average": min(gaa_list) if svp_list else '-'
    }

    md_file.write(f"## {user}\n")
    md_file.write(f"| Player | Pos | Team | G | A | SOG | PIM | +/- | TPM |\n")
    md_file.write(f"| :----- | --- |  --- | - | - | --- | --- | --- | --: |\n")

    
    skaters = player_map["F"]
    skaters.extend(player_map["D"])

    for sk in skaters:      
      md_file.write(sk)

    md_file.write(f"| **Totals** | | | {g_total} | {a_total} | | {pim_total} | {pm_total} | |\n")

    md_file.write(f"\n| Player | Pos | Team | S% | GAA |\n")
    md_file.write(f"| :----- | --- |  --- | -- | --: |\n")

    goalies = player_map["G"]
    for g in goalies:
      md_file.write(g)

  with open('../json/standings.json', 'w') as json_file:
    json_file.write(json.dumps(ranking_data, indent=4))


if __name__ == "__main__":
  main()