fruits = {"kela", "sev", "papeeta"}
print(fruits)

num ={1, 2, 3, 4, 5, 10, 9, 7, 7}
print(num)

print(len(fruits,))
print(len(num))

print(type(fruits))

for p in fruits:
    print(p)


print("papeeta" in fruits)

fruits.add("bihi")

print(fruits)


newFruits = {"jamun", "bair"}

fruits.update(newFruits)
print(fruits)

fruits.update(num)
print(fruits)

for p in fruits:
    print(fruits)

fruits.remove(10)
print(fruits)

fruits.discard("papeeta")
print(fruits)

del num
print(fruits)


fruits.clear()
print(fruits)