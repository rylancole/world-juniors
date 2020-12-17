import os
import json

def main():
  countries = [country[:-5] for country in os.listdir('./json')]
  
  for country in countries:
    print('\"'+country+'\",')

if __name__ == "__main__":
  main()