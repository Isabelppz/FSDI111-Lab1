
print("Hello world")

#data types
name="Isabel"
last="P. Perez"
age=34
found=False
average=2.34

print (name)
print (average)
print (found)

#operations
print(21 + 21)
print(100 - 50)
print(12 * 321)
print(100 / 10)
print(10 % 3) #%=modulus operator(gives the residue)

print(name + name)
print(age + age)
print(name + str(age))

def separator():
    print('______________________')
    print('inside')

print('outside')

separator()

if(age < 90):
    print("You are still young")
elif(age == 90):
    print("You are on the border line")
else:
    print ("Sorry bud you are getting old")