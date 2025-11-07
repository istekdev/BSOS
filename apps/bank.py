from twermcolor import colored
import system
import json
import time

def withColor():
  print(colored("BSOS Bank", "white", attrs=["bold"]))
  print("")
  print(colored("[B] - View Balance", "white", attrs=["bold"]))
  input = input(colored(">> ", "white", attrs=["bold"]))
  if input.upper() in ["B", "[B]"]:
    with open("config.json", "r") as r:
      view = json.load(r)
    print(colored(f"Current Balance: ${str(view["apps"]["bank"]["balance"])}", "white", attrs=["bold"]))
    print("")
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
  else:
    print(colored("Error - Function Dosen't Exist", "red", attrs=["bold"]))
    time.sleep(1)
    system.clear()
    withColor()

def nonColor():
  print("BSOS Bank")
  print("")
  print("[B] - View Balance")
  input = input(">> ")
  if input.upper() in ["B", "[B]"]:
    with open("config.json", "r") as r:
      view = json.load(r)
    print(f"Current Balance: ${str(view["apps"]["bank"]["balance"])}")
    print("")
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
  with open("./config.json", "r") as r:
    config = json.load(r)

  if config["config"]["colors"] == True:
    print(colored("Verifying...", "yellow", attrs=["bold"]))
  else:
    print("Verifying...")

  if config["apps"]["bank"]["balance"] == 0:
    config["apps"]["bank"]["balance"] == 1000
    with open("config.json", "w") as w:
      json.dump(config, w, indent=4)
    if config["config"]["colors"] == True:
      print(colored("Welcome! You Have Been Given $1,000", "white", attrs=["bold"]))
    else:
      print("Welcome! You Have Been Given $1,000")

  if config["config"]["colors"] == True:
    withColor()
  else:
    nonColor()
