# create function 
# odd and even number form list 

# input = 
# number_list = [1,2,3,4,5,6,7]

# output = [[1,3,5,7][2,4,6]]

def odd_even_fun(a):
    odd_list = []
    even_list = []
    for i in a:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)    
    output_list = [odd_list,even_list]
    return output_list
number = [1,2,3,4,5,6,7]
print(odd_even_fun(number))