from termcolor import colored
from security import hashing
import system
import random
import json
import time

rouletteTitle = """
Roulette

[N] - Number
[C] - Color
[X] - Exit"""

menuTitle = """
Welcome To BSOS Gambling

[R] - Roulette
[X] - Exit"""

def roulette():
  redNums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
  blackNums = [2, 4, 6, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
  currentColor = ""
  currentNumber = random.randint(1, 36)
  yourSelection = ""
  
  with open("./config.json", "r") as r:
    ver = json.load(r)
  if ver["config"]["colors"] == True:
    print(system.coloring(rouletteTitle + "\n\n", "white"))
    option = input(system.coloring(">> ", "white"))
    if option.upper() in ["N", "[N]"]:
      yourSelection = input(system.coloring(">> ", "white"))
      if yourSelection.isdigit() and if yourSelection <= 36:
        pass
      else:
        print(system.coloring("Error - Must Be A Valid Number Between 1 and 36", "red"))
        time.sleep(1)
        system.clear()
        roulette()
      for c in range(5, 0, -1):
        print(system.coloring(f"Rolling - Results In: {c}", "white"))
        time.sleep(1)
        system.clear()
      print(system.coloring(f"Your Number: {str(yourSelection)}", "white"))
      if currentNumber in blackNums:
        print(system.coloring(f"Rolled Number: {str(currentNumber)}", "black"))
      elif currentNumber in redNums:
        print(system.coloring(f"Rolled Number: {str(currentNumber)}", "red"))
      if yourSelectionn == currentNumber:
        preBalance = ver["apps"]["bank"]["balance"]
        print(system.coloring(f"You Just Won ${(preBalance * 2)}!", "green"))
        preBalance = preBalance * 2
        with open("./config.json", "w") as w:
          json.dump(preBalance, w, indent=4)
        hashing.start()
        time.sleep(1)
        systemc.clear()
        roulette()
    elif option.upper() in ["C", "[C]"]:
      print(system.coloring("Pick a Color, Either Black or Red.", "white"))
      yourSelection = input(system.coloring(">> ", "white"))
      if yourSelectionu.upper() == "BLACK":
        pass
      elif yourSelection.upper() == "RED":
        pass
      else:
        print(system.coloring("Error - Choose A Valid Color", "red"))
        time.sleep(1)
        system.clear()
        roulette()
      if currentNumber in blackNums:
        currentColor = "BLACK"
      elif currentNumber in redNums:
        currentColor = "RED"
      for c in range(5, 0, -1):
        print(system.coloring(f"Rolling Color - Results In {c}", "white"))
        time.sleep(1)
        system.clear()
      print(system.coloring(f"Your Color: {yourSelection}", "white"))
      if currentNumber in blackNums:
        print(system.coloring("Black Was Rolled", "black"))
      elif currentNumber in redNums:
        print(system.coloring("Red Was Rolled", "red"))
      if yourSelection.upper() == currentColor:
        preBalance = ver["apps"]["bank"]["balance"]
        print(system.coloring(f"You Just Won ${(preBalance * 2)}", "green"))
        preBalance = preBalance * 2
        with open("./config.json", "w") as w:
          json.dump(preBalance, w, indent=4)
        hashing.start()
        time.sleep(1)
        system.clear()
        roulette()
    elif option.upper() in ["X", "[X]"]:
      system.clear()
      system.home()
  else:
    print(rouletteTitle + "\n\n")
    option = input(">> ")
    if option.upper() in ["N", "[N]"]:
      yourSelection = input(">> ")
      if yourSelection.isdigit() and if yourSelection <= 36:
        pass
      else:
        print("Error - Must Be A Valid Number Between 1 and 36")
        time.sleep(1)
        system.clear()
        roulette()
      for c in range(5, 0, -1):
        print(f"Rolling - Results In: {c}")
        time.sleep(1)
        system.clear()
      print(f"Your Number: {str(yourSelection)}")
      if currentNumber in blackNums:
        print(f"Rolled Number: {str(currentNumber)}")
      elif currentNumber in redNums:
        print(f"Rolled Number: {str(currentNumber)}")
      if yourSelectionn == currentNumber:
        preBalance = ver["apps"]["bank"]["balance"]
        print(f"You Just Won ${(preBalance * 2)}!")
        preBalance = preBalance * 2
        with open("./config.json", "w") as w:
          json.dump(preBalance, w, indent=4)
        hashing.start()
        time.sleep(1)
        system.clear()
        roulette()
    elif option.upper() in ["C", "[C]"]:
      print("Pick a Color, Either Black or Red.")
      yourSelection = input(">> ")
      if yourSelectionu.upper() == "BLACK":
        pass
      elif yourSelection.upper() == "RED":
        pass
      else:
        print("Error - Choose A Valid Color")
        time.sleep(1)
        system.clear()
        roulette()
      if currentNumber in blackNums:
        currentColor = "BLACK"
      elif currentNumber in redNums:
        currentColor = "RED"
      for c in range(5, 0, -1):
        print(f"Rolling Color - Results In {c}")
        time.sleep(1)
        system.clear()
      print(f"Your Color: {yourSelection}")
      if currentNumber in blackNums:
        print("Black Was Rolled", "black")
      elif currentNumber in redNums:
        print("Red Was Rolled")
      if yourSelection.upper() == currentColor:
        preBalance = ver["apps"]["bank"]["balance"]
        print(f"You Just Won ${(preBalance * 2)}")
        preBalance = preBalance * 2
        with open("./config.json", "w") as w:
          json.dump(preBalance, w, indent=4)
        hashing.start()
        time.sleep(1)
        system.clear()
        roulette()
    elif option.upper() in ["X", "[X]"]:
      system.clear()
      menu()

def menu():
  with open("./config.json", "r") as r:
    config = json.load(r)
  if config["config"]["colors"] == True:
    print(menuTitle + "\n\n")
    input = input(system.coloring(">> ", "white"))
    if input.upper() in ["R", "[R]"]:
      roulette()
    elif input.upper() in ["X", "[X]"]:
      system.clear()
      system.home()
    else:
      print(system.coloring("Error - Function Does Not Exist", "red"))
      time.sleep(1)
      system.clear()
      menu()
  else:
    print(menuTitle + "\n\n")
    input = input(">> ")
    if input.upper() in ["R", "[R]"]:
      roulette()
    elif input.upper() in ["X", "[X]"]:
      system.clear()
      system.home()
    else:
      print("Error - Function Does Not Exist")
      time.sleep(1)
      system.clear()
      menu()
