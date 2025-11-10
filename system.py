import core
import os

psw = core.password

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def home():
  core.menu()
