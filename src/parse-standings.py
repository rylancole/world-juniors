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

    n = len(st)
    for i, p in enumerate(st):
      STANDINGS_md.write(f"| {i+1} | {p[1]} |  {p[0]} |\n")
      if p[1] in overall_points.keys():
        overall_points[p[1]] += n - i
      else:
        overall_points[p[1]] = n - i

  README_md = open('../README.md', 'w')

  README_md.write(f"| Rank | User | Points |\n")
  README_md.write(f"| :--- | ---- | -----: |\n")

  for i, user in enumerate(overall_points):
    points = overall_points[user]
    README_md.write(f"| {i} | {user} | {points} |\n")

if __name__ == "__main__":
  main()