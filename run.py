from os import system

with open("command.txt","r",encoding="utf-8") as file:
  data = file.read()
  os.system(data)
