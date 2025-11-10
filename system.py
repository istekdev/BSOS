import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def colors(message, color, type):
  if type.lower() == "input":
    return input(colored(message, color, attrs=["bold"]))
  elif type.lower() == "print":
    return print(colored(message, color, attrs=["bold"]))
  else:
    return None
