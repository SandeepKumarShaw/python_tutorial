# define a function that take list of string
# list containing reverse of every number

# Note - use LIST comprehension  
# using normal method

# example 
name = ["mumbai","delhi","kolkata"]
# def list_comprehension(name):
#     reverse_list = []
#     for i in name:
#         reverse_list.append(i[::-1])
#         return reverse_list

def by_list_comp(name):
    reverse_list = [i[::-1] for i in name]
    return reverse_list
print(by_list_comp(name))