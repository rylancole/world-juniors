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

  md_file = open('../STANDINGS.md', 'w')

  for category in standings:
    st = standings[category]
    st.sort()
    st.reverse()

    md_file.write(f"## {category}\n")
    md_file.write(f"| User | {category} |\n")
    md_file.write(f"| :--- |  --------: |\n")

    for p in st:
      md_file.write(f"| {p[1]} |  {p[0]} |\n")

if __name__ == "__main__":
  main()