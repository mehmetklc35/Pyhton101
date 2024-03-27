# all() ve any() fonksiyonları

# all()
# def hepsi(liste):
#     # True - False
#     # [True, True, True] ---> True
#     # [True, True, False] ---> False
#     # [True, False, True] ---> False
#     for i in liste:
#         if not i:
#             return False
#     return True

# liste = [True, True, True, True, True]
# print(hepsi([1,1,1,1,1,1,False]))

# print(hepsi(liste))

# any()
# def herhangi(liste):
#     # [False, False, False, True] --> True
#     # [False, False, False, False] --> False
#     for i in liste:
#         if i:
#             return True
#     return False

# liste = [False, False, False, True]
# print(herhangi(liste))

# print(herhangi([0,0,0,0,0,0]))

# liste = [True, True, True, True, True]

# print(all(liste))

# liste = [0,1,2,3,4,5]
# print(all(liste))

# liste = [False, False, False, False]
liste = [0,0,0,0,0]
print(any(liste))