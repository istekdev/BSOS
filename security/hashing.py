from hashlib import sha256
import system
import json
import os

with open("config.json", "r") as r:
  config = json.load(r)
static = ((config["socials"]["developer"]).encode("utf-8") + (config["socials"]["github"]).encode("utf-8") + str(config["socials"]["created"]).encode("utf-8") + str(config["config"]["version"]).encode("utf-8") + str(config["config"]["colors"]).encode("utf-8") + (config["dynamic"]["user"]).encode("utf-8") + bytes.fromhex(config["dynamic"]["nonce"]) + str(config["apps"]["bank"]["balance"]).encode("utf-8"))

def start():
  if config["dynamic"]["nonce"] == None:
    nonce = os.urandom(10)
    config["dynamic"]["nonce"] = nonce.hex()
  config["configHash"] = sha256(sha256(static).digest()).hexdigest()
  with open("./config.json", "w") as w:
    json.dump(config, w, indent=4)

def verify():
  verified = False
  if config["configHash"] == sha256(sha256(static).digest()).hexdigest():
    verified = True
  return verified
