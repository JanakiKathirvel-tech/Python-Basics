import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

f = open("demotxt.txt", "r")
print(f)