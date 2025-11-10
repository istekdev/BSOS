from termcolor import colored
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
    return
  try:
    output = eval(calc)
    print(output)
    time.sleep(1)
    print("\n\n" + optionTitle)
    option = input(">> ")
    if option.upper() in ["L", "[L]"]::
      system.clear()
      return
    elif option.upper() in ["C", "[C]"]::
      system.clear()
      nonColor()
  except Exception as ex:
    print(f"Error - {ex}")

def withColor():
  print(colored(calcTitle + "\n\n", "white", attrs=["bold"]))
  calc = input(colored(">> ", "white", attrs=["bold"]))
  if calc.upper() in ["L", "[L]"]:
    system.clear()
    return
  try:
    output = eval(calc)
    print(colored(output, "white", attrs=["bold"]))
    time.sleep(1)
    print(colored("\n\n" + optionTitle, "green", attrs=["bold"]))
    option = input(colored(">> ", "white", attrs=["bold"]))
    if option.upper() in ["L", "[L]"]:
      system.clear()
      return
    elif option.upper() in ["C", "[C]"]:
      system.clear()
      nonColor()
  except Exception as ex:
    print(colored(f"Error - {ex}", "red", attrs=["bold"]))
  
def verify():
  with open("./config.json", "r") as r:
    config = json.load(r)

  if config["config"]["colors"] == True:
    withColor()
  else:
    nonColor()
