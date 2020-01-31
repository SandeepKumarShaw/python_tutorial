# Exception handling 
# Try and except
# Else and finally keyword in Exception handling

#ex1
while True:
    try:

        number1 = int(input("enter any number :-"))
        number2 = int(input("enter any number :-"))
        #break

    except ValueError:    
        print("Enter only number")

    except:
        print("unknown error")

    else:
        print(number1 + number2)
        break

    finally:
        print("program run successfully")    

#print(number1 + number2)

#ex2
try:
    number1 = int(input("enter any number :-"))
    number2 = int(input("enter any number :-"))
    #break

except ValueError as err:    
    #print("Enter only number")
    print(err)

# Custome Exception

class NameisTooLongError(ValueError):
    pass
name = int(input("enter your name :-"))
if len(name) > 7:
    raise ValueError("Your name is too long:")

