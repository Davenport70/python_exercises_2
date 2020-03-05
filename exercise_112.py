# Write a bizz and zzuu game ##project

# as a user I should be able prompted for a number, as the program will
# print all the number up to and inclusing said number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will
# calculate appropriately until you use the key word: 'penpinapplespen'

number = ''

# number list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#              16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
#              30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
while True:
    print("If you want to exit input: pineapplespen")
    number = int(input('Pick your favorite number: '))
    for number in range(number):
        if number % 3 == 0 and number % 5 == 0:
            print('bizzzzuu')
        elif number % 3 == 0:
            print('bizz')
        elif number % 5 == 0:
            print('zzuu')
        else:
            print(number)










# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu