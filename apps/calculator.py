from termcolor import colored
import system
import json
import time

def nonColor():
  print("Calculator | Version 1.0.0")
  print("[L] To Leave App")
  print("")
  calc = input(">> ")
  if calc.upper() in ["L", "[L]"]:
    system.clear()
    system.return()
  try:
    output = eval(calc)
    print(output)
    time.sleep(1)
    print("")
    print("[C] - Continue")
    print("[L] - Leave")
    option = input(">> ")
    if option.upper() in ["L", "[L]"]::
      system.clear()
      system.return()
    elif option.upper() in ["C", "[C]"]::
      system.clear()
      nonColor()
  except Exception as ex:
    print(f"Error - {ex}")

def withColor():
  print(colored("Calculator | Version 1.0.0", "white", attrs=["bold"]))
  print(colored("[L] To Leave App", "red", attrs=["bold"]))
  print("")
  calc = input(colored(">> ", "white", attrs=["bold"]))
  if calc.upper() in ["L", "[L]"]:
    system.clear()
    system.return()
  try:
    output = eval(calc)
    print(colored(output, "white", attrs=["bold"]))
    time.sleep(1)
    print("")
    print(colored("[C] - Continue", "green", attrs=["bold"]))
    print(colored("[L] - Leave", "red", attrs=["bold"]))
    option = input(colored(">> ", "white", attrs=["bold"]))
    if option.upper() in ["L", "[L]"]:
      system.clear()
      system.return()
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
