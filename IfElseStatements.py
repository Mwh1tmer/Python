a = 1
b = 2
if a < b:
    print("a is less than b")
print("Not sure if a is less than b")

a = 2
b = 1
if a < b:
    print("a is less than b")
print("Not sure if a is less than b")

c = 2
d = 1
if c < d:
    print("c is less than d")
else:
    print("c is Not less than d")
    print("I don't think c is less than d")
print("outside the if block")

c = 1
d = 2
if c < d:
    print("c is less than d")
else:
    print("c is Not less than d")
    print("I don't think c is less than d")
print("outside the if block")

e = 8
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is Not less than f")
    
    
    g = 7
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")
        
   name = "Bob"
height_m = 2
weight_kg = 90

bmi = weight_kg / (height_m ** 2)
print("bmi:  ")
print(bmi)
if bmi < 25:
    print(name)
    print("is Not overweight")
else:
    print(name)
    print("is overweight")

    