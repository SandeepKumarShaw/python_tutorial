# define a function that takes a number(n)
# return a dictionary conttaining square of number from 1 to number

# Example 
# Square_finder(4)
# output
# {1:1,2:4,3:9,4:12}

def Square_finder(a):
    square_num = {}
    for i in range(1, a+1):
        square_num[i] = i**2
    return square_num

print(Square_finder(5))