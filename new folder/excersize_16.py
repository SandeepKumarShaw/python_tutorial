
user = {}
name = input("Enter your Name :-")
last_name = input("Enter your last name :-")
age = int(input("Enter your age :-"))
fav_movie = input("enter your fab movie separated by comma").split(",")
user["name"] = name
user["last_name"] = last_name
user["age"] = age
user["fav_movie"] = fav_movie

print(user)
for i,j in user.items():
    print(f"the key is {i} and value is {j}")