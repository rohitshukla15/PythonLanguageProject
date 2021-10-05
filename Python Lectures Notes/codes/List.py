fruits = ["apple", "banana", "cherry", "guava"]
print(fruits)
print(type(fruits))
print(fruits[2])
print(fruits[-2])
print(fruits[0:])
if "banana" in fruits:
    print("Exist!")
fruits[0] = "sev"
fruits[2] ="deshi"
print(fruits)
newfruits=["aam", "jamun", "amrood"]
print(fruits[0:2])
fruits[0:2] = newfruits
fruits.insert(-1, "watemenon")
fruits.append("kuchhnhi")
fruits.extend(newfruits)
fruits.remove("kuchhnhi")
fruits.pop(0)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)