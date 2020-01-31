# define a function which will take list as a argument and this function
# will return a reversed list

# examples
# [10,11,12,13] ‐‐‐ > [13,12,11,10]
# ['car' ,'bike'] ‐‐‐> ['bike','car']
# you can use reverse method or string slicing [::-1]
# also try this with pop and append method


# def reverse_list(a):
#     a.reverse()
#     return a

# def string_slice(a):
#     return a[::-1]    

# number = [2,3,4,5,6]
# #print(reverse_list(number))
# print(string_slice(number))

# def Append_pop(a):
#     reverse_list = []
#     for i in range(len(a)):
#         pop_item = a.pop()
#         reverse_list.append(pop_item)
#     return reverse_list    

#  sss = ["dhdh","nbbn","jdgh"]   
#  print(Append_pop(sss))

def Append_pop_1(a):

    reverse_list = []
    for i in range(len(a)):

        pop_item = a.pop()
        reverse_list.append(pop_item)
    return reverse_list

name = ["mahendar","chetan","rahul"]
print(Append_pop_1(name))