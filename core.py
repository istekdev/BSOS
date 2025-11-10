from apps import gambling, cryptomining, bank, settings, randomness, calculator
from security import aes, hashing
from termcolor import colored
import system
import json
import time

with open("config.json", "r") as r:
  config = json.load(r)

psw = ""

def home(option):
  if option.upper() == "colors":
    

def register(option):
  if option.lower() == "colors":
    psw = input(colored("Create a New Password: ", "white", attrs=["bold"]))
    system.clear()
    psw2 = input(colored("Confirm your Password: ", "white", attrs=["bold"]))
    if psw == psw2:
      system.clear()
      print(colored("Welcome to BSOS", "green", attrs=["bold"]))
      time.sleep(1)
      system.clear()
      home("colors")
    else:
      print(colored("Error - Password Is Incorrect", "red", attrs=["bold"]))
      time.sleep(3)
      system.clear()
      register("colors")
  elif option.lower == "regular":
    psw = input("Create a New Password: ")
    system.clear()
    psw2 = input("Confirm your Password: ")
    if psw == psw2:
      system.clear()
      print("Welcome to BSOS")
      time.sleep(1)
      system.clear()
      home("regular")
    else:
      print("Error - Password Is Incorrect")
      time.sleep(3)
      system.clear()
      register("regular")

def login(option):
  if option.lower() == "colors":
    print(colored(f"Login to BSOS as {config["dynamic"]["user"]}\n\n", "white", attrs=["bold"]))
    psw = input(colored("Enter your Password: ", "white", attrs=["bold"]))
    aes.d()
    if config["dynamic"]["status"] == "OK":
      print(colored("Welcome to BSOS!", "green", attrs=["bold"]))
      time.sleep(2)
      system.clear()
      home("colors)
    else:
      print(colored("Error - Incorrect Password", "red", attrs=["bold"]))
      time.sleep(3)
      system.clear()
      login()
  elif option.lower() == "regular":
    print(f"Login to BSOS as {config["dynamic"]["user"]}\n\n")
    psw = input("Enter your Password: ")
    aes.d()
    if config["dynamic"]["status"] == "OK":
      print("Welcome to BSOS!")
      time.sleep(2)
      system.clear()
      home("regular")
    else:
      print("Error - Incorrect Password")
      time.sleep(3)
      system.clear()
      login()

def logout(option):
  if option.lower() == "colors":
    print(colored("Logging Out...", "yellow", attrs=["bold"]))
    aes.e()
    print(colored("Logged Out!", "green", attrs=["bold"]))
    time.sleep(2)
    return
  elif option.lower() == "regular":
    print("Logging Out...")
    aes.e()
    print("Logged Out!")
    time.sleep(2)
    return
