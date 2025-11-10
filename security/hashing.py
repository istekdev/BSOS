from hashlib import sha256
import system
import json
import os

static = ((config["socials"]["developer"]).encode("utf-8") + (config["socials"]["github"]).encode("utf-8") + str(config["socials"]["created"]).encode("utf-8") + str(config["config"]["version"]).encode("utf-8") + str(config["config"]["colors"]).encode("utf-8") + (config["dynamic"]["user"]).encode("utf-8") + bytes.fromhex(config["dynamic"]["nonce"]) + str(config["apps"]["bank"]["balance"]).encode("utf-8"))

def start():
  if system.config["dynamic"]["nonce"] == None:
    nonce = os.urandom(10)
    system.config["dynamic"]["nonce"] = nonce.hex()
  system.config["configHash"] = sha256(sha256(static).digest()).hexdigest()
  with open("./system.config.json", "w") as w:
    json.dump(system.config, w, indent=4)

def verify():
  verified = False
  if system.config["configHash"] == sha256(sha256(static).digest()).hexdigest():
    verified = True
  return verified
