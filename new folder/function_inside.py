def greater(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
def new_greater(a,b,c):
    biggernumber = greater(a,b)
    return greater(biggernumber,c)

print("Greatest Number is :-" + str(new_greater(10,5,20)))