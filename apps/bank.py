from twermcolor import colored
import system
import json
import time

# Tomorrow

with open("./config.json", "r") as r:
  config = json.load(r)

if config["config"]["colors"] == True:
  withColor()
else:
  nonColor()
