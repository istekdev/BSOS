from termcolor import colored
import system
import json
import time

bankTitle = """
Welcome to BSOS Bank

[B] - View Balance"""

def withColor():
  print(system.coloring(bankTitle + "\n\n", "white"))
  input = input(system.coloring(">> ", "white"))
  if input.upper() in ["B", "[B]"]:
    with open("./config.json", "r") as r:
      view = json.load(r)
    print(system.coloring(f"Current Balance: ${str(view["apps"]["bank"]["balance"])}\n\n", "white"))
    print(system.coloring("[X] - Exit", "white"))
    option = input(system.coloring(">> ", "white"))
    if option.upper() in ["X", "[X]"]:
      system.clear()
      withColor()
    else:
      print(system.coloring("Error - Function Dosen't Exist", "red"))
      time.sleep(1)
      system.clear()
      withColor()
  elif input.upper() in ["X", "[X]"]:
    system.clear()
    system.home()
  else:
    print(system.coloring("Error - Function Dosen't Exist", "red"))
    time.sleep(1)
    system.clear()
    withColor()

def nonColor():
  print(bankTitle + "\n\n")
  input = input(">> ")
  if input.upper() in ["B", "[B]"]:
    with open("./config.json", "r") as r:
      view = json.load(r)
    print(f"Current Balance: ${str(view["apps"]["bank"]["balance"])}\n\n")
    print("[X] - Exit")
    option = input(">> ")
    if option.upper() in ["X", "[X]"]:
      system.clear()
      withColor()
    else:
      print("Error - Function Dosen't Exist")
      time.sleep(1)
      system.clear()
      withColor()
  else:
    print("Error - Function Dosen't Exist")
    time.sleep(1)
    system.clear()
    withColor()

def verify():
  with open("././config.json", "r") as r:
    config = json.load(r)

  if config["config"]["colors"] == True:
    print(system.coloring("Verifying...", "yellow"))
  else:
    print("Verifying...")

  if config["apps"]["bank"]["balance"] == 0:
    config["apps"]["bank"]["balance"] == 1000
    with open("./config.json", "w") as w:
      json.dump(config, w, indent=4)
    if config["config"]["colors"] == True:
      print(system.coloring("Welcome! You Have Been Given $1,000", "white"))
    else:
      print("Welcome! You Have Been Given $1,000")

  if config["config"]["colors"] == True:
    withColor()
  else:
    nonColor()
