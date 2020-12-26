import json 

def main():
  with open('../json/standings.json', 'r') as json_file:
    ranking_data = json.loads(json_file.read())

  standings = {}

  for user in ranking_data:
    scores = ranking_data[user]
    for category in scores:
      score = scores[category]
      if score != '-':
        if category in standings.keys():
          standings[category].append((score, user))
        else:
          standings[category] = [(score, user)]

  STANDINGS_md = open('../STANDINGS.md', 'w')

  overall_points = {}

  for category in standings:
    st = standings[category]
    st.sort()
    if category != "Goals Against Average": st.reverse()

    STANDINGS_md.write(f"## {category}\n")
    STANDINGS_md.write(f"| Rank | User | {category} |\n")
    STANDINGS_md.write(f"| :--- | ---- | ---------: |\n")

    for i, p in enumerate(st):
      STANDINGS_md.write(f"| {i+1} | [{p[1]}](https://github.com/rylancole/world-juniors/blob/master/ROSTERS.md#{p[1]}) |  {p[0]} |\n")

  README_md = open('../README.md', 'w')

  README_md.write(f"| Rank | User | [G](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#goals) | [A](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#assists) | [PIM](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#penalties-in-minutes) | [+/-](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#plus--minus) | [S%](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#save-percentage) | [GAA](https://github.com/rylancole/world-juniors/blob/master/STANDINGS.md#goals-against-average) |\n")
  README_md.write(f"| :--- | ---- | ---- | ---- | ---- | ---- | ---- | -----: |\n")

  for i, user in enumerate(ranking_data):
    README_md.write(f"| {i+1} | {user} | ")
    for p in ranking_data[user]:
      README_md.write(f"{ranking_data[user][p]} | ")
    README_md.write(f"\n")

  

if __name__ == "__main__":
  main()