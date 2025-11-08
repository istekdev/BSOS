from hashlib import sha256
import json

def start():
  nonce = None
  with open("./config.json", "r") as r:
    config = json.load(r)
  if config["dynamic"]["nonce"] == None:
    nonce = "None".encode("utf-8")
  else:
    nonce = bytes.fromhex(config["dynamic"]["nonce"])
    
  static = ((config["socials"]["developer"]).encode("utf-8") + (config["socials"]["github"]).encode("utf-8") + str(config["socials"]["created"]).encode("utf-8") + str(config["config"]["colors"]).encode("utf-8") + nonce + str(config["apps"]["bank"]["balance"]).encode("utf-8"))
  config["configHash"] = sha256(sha256(static).digest()).hexdigest()
  with open("./config.json", "w") as w:
    json.dump(config, w, indent=4)
