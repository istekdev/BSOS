from termcolor import colored
from eth_utils import keccak
import requests
import system
import random
import base58
import json
import time
import os

with open("config.json", "r") as r:
  config = json.load(r)

randomTitle = """
Welcome to BSOS Randomness

[W] - Random Word Generator
[I] - Random Integer Generator
[E] - True Entropy Generator
[P] - Password Generator
[X] - Exit"""

def randWord():
  randomWord = "https://random-word-api.herokuapp.com/word"
  try:
    connection = requests.get(randomWord).json()
  except Exception as ex:
    return False
  return connection[0]

def randomInt(val):
  return random.randint(0, val)

def trueEntropy(size):
  entropy = os.urandom(size)
  return str(int.from_bytes(entropy, "big"))

def passwordGen(security):
  password = ""
  if security.upper() == "LITTLE":
    password = randWord() + randWord() + randWord() + str(random.randint(1, 1000))
  elif security.upper() == "MOD":
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    while len(password) < random.randint(15, 20):
      password += alphabet[random.randint(0, 61)]
  elif security.upper() == "HIGH":
      password = base58.b58encode(keccak(os.urandom(32))).decode()
  return password

def menu():
  if config["config"]["colors"] == True:
    print(colored(randomTitle + "\n\n", "white", attrs=["bold"]))
    input = input(colored(">> ", "white", attrs=["bold"]))
    if input.upper() in ["X", "[X]"]:
      system.clear()
      return
    elif input.upper() in ["P", "[P]"]:
      system.clear()
      print(colored("[LITTLE] - Little Security\n\n[MOD] - Moderate Security\n\n[HIGH] - High Security\n\n[X] - Exit\n\n", "white", attrs=["bold"]))
      option = input(colored(">> ", "white", attrs=["bold"]))
      if option.upper() in ["X", "[X]"]:
        system.clear()
        menu()
      elif option.upper() in ["LITTLE", "[LITTLE]"]:
        while True:
          system.clear()
          print(colored("Your Unsecure Password Is: " + passwordGen("LITTLE") + "\n\n", "white", attrs=["bold"]))
          cont = input(colored("Continue (y/n): ", "white", attrs=["bold"]))
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      elif option.upper() in ["MOD", "[MOD]"]:
        while True:
          system.clear()
          print(colored("Your Moderately Secure Password Is: " + passwordGen("MOD") + "\n\n", "white", attrs=["bold"]))
          cont = input(colored("Continue (y/n): ", "white", attrs=["bold"]))
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      elif option.upper() in ["HIGH", "[HIGH]"]:
        while True:
          system.clear()
          print(colored("Your Very Secure Password Is: " + passwordGen("HIGH") + "\n\n", "white", attrs=["bold"]))
          cont = input(colored("Continue (y/n): ", "white", attrs=["bold"]))
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      else:
        print(colored("Error - Function Does Not Exist", "red", attrs=["bold"]))
        time.sleep(3)
        system.clear()
        menu()
  else:
    print(randomTitle + "\n\n")
    input = input(">> ")
    if input.upper() in ["X", "[X]"]:
      system.clear()
      return
    elif input.upper() in ["P", "[P]"]:
      system.clear()
      print("[LITTLE] - Little Security\n\n[MOD] - Moderate Security\n\n[HIGH] - High Security\n\n[X] - Exit\n\n")
      option = input(">> ")
      if option.upper() in ["X", "[X]"]:
        system.clear()
        menu()
      elif option.upper() in ["LITTLE", "[LITTLE]"]:
        while True:
          system.clear()
          print("Your Unsecure Password Is: " + passwordGen("LITTLE") + "\n\n")
          cont = input("Continue (y/n): ")
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      elif option.upper() in ["MOD", "[MOD]"]:
        while True:
          system.clear()
          print("Your Moderately Secure Password Is: " + passwordGen("MOD") + "\n\n")
          cont = input("Continue (y/n): ")
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      elif option.upper() in ["HIGH", "[HIGH]"]:
        while True:
          system.clear()
          print("Your Very Secure Password Is: " + passwordGen("HIGH") + "\n\n")
          cont = input("Continue (y/n): ")
          if cont.upper() != "Y":
            system.clear()
            menu()
            break
      else:
        print("Error - Function Does Not Exist")
        time.sleep(3)
        system.clear()
        menu()
