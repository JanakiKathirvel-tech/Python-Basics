#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

#All these objects have a iter() method which is used to get an iterator:

mytuple = ({"apple","banana","orange"})
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))