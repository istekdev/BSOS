from termcolor import colored
from security import hashing
import system
import json
import time

with open("./config.json", "r") as r:
  config = json.load(r)

settingsTitle = """
Welcome to BSOS Settings

Display:
---
[COLORS] - Toggle Text Colors"""
      
def menu():
  if config["config"]["colors"] == True:
    print(colored(settingsTitle + "\n\n", "white", attrs=["bold"]))
    input = input(colored(">> ", "white", attrs=["bold"]))
    if input.upper() in ["COLORS", "[COLORS]"]:
      system.clear()
      print(colored("Text Colors:\n\n[OFF] - Turn Off Text Colors\n\n[X] - Exit", "red", attrs=["bold"]))
      option = input(colored(">> ", "white", attrs=["bold"]))
      if option.upper() in ["OFF", "[OFF]"]:
        config["config"]["colors"] = False
        with open("./config.json", "w") as w:
          json.dump(config, w, indent=4)
      print(colored("Saved Settings!", "green", attrs=["bold"]))
      hashing.start()
      system.clear()
      menu()
      elif option.upper() in ["X", "[X]"]:
        system.clear()
        menu()
      else:
        print(colored("Error - Function Does Not Exist", "red", attrs=["bold"]))
        time.sleep(3)
        system.clear()
        menu()
  else:
    print(settingsTitle + "\n\n")
    input = input(">> ")
    if input.upper() in ["COLORS", "[COLORS]"]:
      system.clear()
      print("Text Colors:\n\n[ON] - Turn On Text Colors\n\n[X] - Exit\n\n")
      option = input(">> ")
      if option.upper() in ["ON", "[ON]"]:
        config["config"]["colors"] = True
        with open("./config.json", "w") as w:
          json.dump(config, w, indent=4)
      elif option.upper() in ["X", "[X]"]:
        system.clear()
        menu()
      else:
        print("Error - Function Does Not Exist")
        time.sleep(3)
        system.clear()
        menu()
      print("Saved Settings!")
      hashing.start()
      system.clear()
      menu()
    else:
      print("Error - Function Does Not Exist")
      time.sleep(3)
      system.clear()
      menu()
