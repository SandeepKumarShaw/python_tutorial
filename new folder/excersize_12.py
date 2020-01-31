def reverese_order(a):
    value = []
    for i in a:
        value.append(i[::-1])
    return value    


num = ["hhvccv","vcvcbc","hsvhvx"]
print(reverese_order(num))