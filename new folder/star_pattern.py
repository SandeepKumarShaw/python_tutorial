# *     1
# **    2
# ***   3
# ****  4
# ***** 5
# ****** 6

n = 6
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end = "")
    print("\r")
