from termcolor import colored
from hashlib import sha256
import json
import core
import time
import os

def start():
  with open("config.json", "r") as r:
    config = json.load(r)
  if config["dynamic"]["nonce"] == None:
    with open("config.json", "w") as w:
      config["dynamic"]["nonce"] = hex(os.urandom(10))
      json.dump(config, w, indent=4)
  if config["dynamic"]["verifyHash"] == None:
    config["dynamic"]["verifyHash"] = sha256(sha256((core.user).encode("utf-8") + (core.pass).encode("utf-8") + bytes.fromhex(config["dynamic"]["nonce"])).digest()).hexdigest()
    with open("config.json", "w") as w:
      json.dump(config, w, indent=4)
  # Tomorrow
  
