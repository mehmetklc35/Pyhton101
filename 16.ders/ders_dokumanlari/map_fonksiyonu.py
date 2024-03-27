# def double(x):
#     return x * 2

# liste = [1,2,3,4,5]
# print(list(map(double,liste)))

# def thirdpow(x):
#     return x ** 3

# liste = [1,2,3,4,5]
# print(list(map(thirdpow,liste)))

# liste = [1,2,3,4,5]
# print(list(map(lambda x: x**2,liste)))

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12]

print(list(map(lambda x,y,z: x*y*z,liste1,liste2,liste3)))