# create function 
# find how much number of list inside list

# Example 
# input
# list = [1,2,[1,2],[5,6,4],[9,6,9]]

def count_list_linside_list(a):
    count = 0
    for i in a:
        if type(i) == list:
            count += 1
    return count

number = [1,2,[1,2],[5,6,4],[9,6,9]]
print(count_list_linside_list(number))
