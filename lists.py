fruits=["banana","orange","pawpaw","apple","mango"]
print(fruits[0]) #listing or calling them out

fruits.append("pineapple")  # adds to end
print(fruits)

fruits.insert(1, "watermelon")  # inserts at index 1
print(fruits)

fruits.remove("mango")  # removes by value
print(fruits)

print(len(fruits))  #length of list

for fruit in fruits:
    print(fruit)




