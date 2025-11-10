from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from hashlib import pbkdf2_hmac
import ephemeral
import hashing
import system
import json
import time
import os

with open("config.json", "r") as r:
  config = json.load(r)

salt = bytes.fromhex(config["dynamic"]["salt"])
nonce = bytes.fromhex(config["dynamic"]["nonce"])

def e():
  if hashing.verify() == True:
    if config["dynamic"]["salt"] == None:
      config["dynamic"]["salt"] = hex(os.urandom(16))
      with open("config.json", "w") as w:
        json.dump(config, w, indent=4)
      hashing.start()
      password = (ephemeral.password).encode("utf-8")
      aes = AESGCM(pbkdf2_hmac("sha256", password, salt, 200_000, dklen=32))
      config["apps"]["bank"]["balance"] = aes.encrypt(nonce, config["apps"]["bank"]["balance"], None)
      with open("config.json", "w") as w:
        json.dump(config, w, indent=4)
      ephemeral.wipe()
      aes = None
      return "LogOut", aes
    else:
      return False

def d():
  if hashing.verify() == True:
    password = (ephemeral.password).encode("utf-8")
    aes = AESGCM(pbkdf2_hmac("sha256", password, salt, 200_000, dklen=32))
    config["apps"]["bank"]["balance"] = aes.decrypt(nonce, config["apps"]["bank"]["balance"], None)
    with open("config.json", "w") as w:
      json.dump(config, w, indent=4)
    ephemeral.wipe()
    aes = None
    return True
  else:
    return False
