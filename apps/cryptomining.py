from termcolor import colored
from hashlib import sha256
import system
import random
import json
import time
import os

difficulty = 1000 * 120
target = ((2**224) * ((2**32) - 1)) // difficulty
targetByted = target.to_bytes(32, "big")

menuTitle = """
Welcome To BSOS Crypto Mining

[S] - Start
[X] - Exit"""

def block():
  version = 1
  height = random.getrandbits(24)
  merkleRoot = sha256(os.urandom(2)).digest()
  Target = targetByted.hex()
  timestamp = str(round(time.time()))
  nonce = 0
  blockHash = sha256(sha256(version.to_bytes(4, "big") + height.to_bytes(3, "big") + merkleRoot + bytes.fromhex(Target) + timestamp.encode("utf-8") + nonce.to_bytes(32, "big")).digest()).hexdigest()
  return version, height, merkleRoot, Target, timestamp, nonce, blockHash

def mine():
  with open("config.json", "r") as r:
    config = json.load(r)
  max = (2**32) - 1
  nonce = 0
  while nonce < max:
    nonce += 1
    bHash = sha256(sha256(block()[0].to_bytes(4, "big") + block()[1].to_bytes(3, "big") + block()[2] + bytes.fromhex(block()[3]) + block()[4].encode("utf-8") + nonce.to_bytes(32, "big")).digest()).hexdigest()
    if config["config"]["colors"] == True:
      print(colored(f"Mining - Current Hash: {bHash}", "yellow", attrs=["bold"]))
    else:
      print(f"Mining - Current Hash: {bHash}")
      
    if int(bHash, 16) <= target:
      if config["config"]["colors"] == True:
        print(colored("Block Has Been Mined! You Earned $2,500!", "green", attrs=["bold"]))
      else:
        print("Block Has Been Mined! You Earned $2,500!")
        Balance = config["apps"]["bank"]["balance"] + 2500
      with open("config.json", "w") as w:
        json.dump(Balance, w, indent=4)
      time.sleep(1)
      break
      system.clear()
      system.home()

def menu():
  with open("config.json", "r") as r:
    ver = json.load(r)
  if ver["config"]["colors"] == True:
    print(colored(menuTitle + "\n\n", "white", attrs=["bold"]))
    input = input(colored(">> ", "white", attrs=["bold"]))
    if input.upper() in ["S", "[S]"]:
      system.clear()
      mine()
    elif input.upper() in ["X", "[X]"]:
      system.clear()
      system.home()
    else:
      print(colored("Error - Function Does Not Exist", "red", attrs=["bold"]))
      time.sleep(3)
      system.clear()
      system.home()
  else:
    print(menuTitle + "\n\n")
    input = input(">> ")
    if input.upper() in ["S", "[S]"]:
      system.clear()
      mine()
    elif input.upper() in ["X", "[X]"]:
      system.clear()
      system.home()
    else:
      print("Error - Function Does Not Exist")
      time.sleep(3)
      system.clear()
      system.home()
  
