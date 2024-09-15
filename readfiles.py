f = open("demotxt.txt", "r")
print(f.read())


# Read fist  characters
f = open("demotxt.txt", "r")
print(f.read(5))

# Read line
f = open("demotxt.txt", "r")
print(f.readline())

f = open("demotxt.txt", "r")
for x in f:
    print(x)
f.close()

