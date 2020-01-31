# List Unside List

list_inside_list =[[1,2,3],[4,5,6],[7,8,9]]
#print(list_inside_list[0][1])

for sub_list in list_inside_list:
    for i in sub_list:
        print(i)