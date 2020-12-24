import json

def main():
  with open('rosters.json', 'r') as json_file:
    data = json.loads(json_file.read())

  md_file = open('rosters.md', 'w')

  md_file.write("# Fantasy Rosters\n")

  for user in data:
    roster = data[user]

    md_file.write(f"## {user}\n")
    for pick in roster:
      md_file.write(f"- {pick}\n")

if __name__ == "__main__":
  main()