import core
import json
import os

global config
with open("config.json", "r") as r:
  config = json.load(r)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def home():
  core.menu()
