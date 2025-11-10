from termcolor import colored
import system
import json
import time

bankTitle = """
Welcome to BSOS Bank

[B] - View Balance"""

def withColor():
  print(colored(bankTitle + "\n\n", "white", attrs=["bold"]))
  input = input(colored(">> ", "white", attrs=["bold"]))
  if input.upper() in ["B", "[B]"]:
    with open("./config.json", "r") as r:
      view = json.load(r)
    print(colored(f"Current Balance: ${str(view["apps"]["bank"]["balance"])}\n\n", "white", attrs=["bold"]))
    print(colored("[X] - Exit", "white", attrs=["bold"]))
    option = input(colored(">> ", "white", attrs=["bold"]))
    if option.upper() in ["X", "[X]"]:
      system.clear()
      withColor()
    else:
      print(colored("Error - Function Dosen't Exist", "red", attrs=["bold"]))
      time.sleep(1)
      system.clear()
      withColor()
  elif input.upper() in ["X", "[X]"]:
    system.clear()
    core.home()
  else:
    print(colored("Error - Function Dosen't Exist", "red", attrs=["bold"]))
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
      core.home()
    else:
      print("Error - Function Dosen't Exist")
      time.sleep(1)
      system.clear()
      nonColor()
  else:
    print("Error - Function Dosen't Exist")
    time.sleep(1)
    system.clear()
    nonColor()

def verify():
  with open("././config.json", "r") as r:
    config = json.load(r)

  if config["config"]["colors"] == True:
    print(colored("Verifying...", "yellow", attrs=["bold"]))
  else:
    print("Verifying...")

  if config["apps"]["bank"]["balance"] == 0:
    config["apps"]["bank"]["balance"] == 1000
    with open("./config.json", "w") as w:
      json.dump(config, w, indent=4)
    if config["config"]["colors"] == True:
      print(colored("Welcome! You Have Been Given $1,000", "white", attrs=["bold"]))
    else:
      print("Welcome! You Have Been Given $1,000")

  if config["config"]["colors"] == True:
    withColor()
  else:
    nonColor()
