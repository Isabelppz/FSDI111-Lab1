def separator():
    print("-" * 30)

def print_menu():
    print('\n'* 5)
    #is there a way to clear the console??
    separator()
    print('Welcome to PyCalc')
    separator()

    print('[1]- Add')
    print('[2]- Substract')
    print('[3]- Multiply')
    print('[4]- Divide')

    print('[x]- Close')

    separator()

def sum(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    # //print('user input:'+ opc)
    if(opc == 'x'):
        break # break = finish loop

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == '1'):
        res = sum(num1, num2)
        print("Result: "+ str(res) )

    elif(opc == '2'):
        #res = substract(num1, num2)
        print ("Result: " + str(substract(num1,num2)))

    input("Press enter to continue...")

print("Byte byte!")
    
""" elif(opc =='2'):
    print("result: ")+ str(substract(num1,num2)) """
 
 # on division, show an error 
 #switch ()