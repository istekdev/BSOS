import system
import json
import time

calcTitle = """
Welcome to BSOS Calculator

[L] - Leave"""

optionTitle = """
[C] - Continue
[L] - Leave"""

def nonColor():
  print(calcTitle + "\n\n")
  calc = input(">> ")
  if calc.upper() in ["L", "[L]"]:
    system.clear()
    system.home()
  try:
    output = eval(calc)
    print(output)
    time.sleep(1)
    print("\n\n" + optionTitle)
    option = input(">> ")
    if option.upper() in ["L", "[L]"]::
      system.clear()
      system.home()
    elif option.upper() in ["C", "[C]"]::
      system.clear()
      nonColor()
  except Exception as ex:
    print(f"Error - {ex}")

def withColor():
  print(system.coloring(calcTitle + "\n\n", "white"))
  calc = input(system.coloring(">> ", "white"))
  if calc.upper() in ["L", "[L]"]:
    system.clear()
    system.home()
  try:
    output = eval(calc)
    print(system.coloring(output, "white"))
    time.sleep(1)
    print(system.coloring("\n\n" + optionTitle, "green"))
    option = input(system.coloring(">> ", "white"))
    if option.upper() in ["L", "[L]"]:
      system.clear()
      system.home()
    elif option.upper() in ["C", "[C]"]:
      system.clear()
      nonColor()
  except Exception as ex:
    print(system.coloring(f"Error - {ex}", "red"))
  
def verify():
  with open("./config.json", "r") as r:
    config = json.load(r)

  if config["config"]["colors"] == True:
    withColor()
  else:
    nonColor()
