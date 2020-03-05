age = 18
driver_licence = True

drive_test = int(input('test if you can drive! Enter your age: '))
# - You can vote and drive

if drive_test <= age:
    print('you can not drive or vote yet I am sorry!')
elif drive_test >= age:
    print('Congratulations you can drive and vote!')



drink_age = 18
your_age = int(input('Please enter your age: '))

if your_age >= drink_age:
    print('You can drink! go grab a beer! ')
elif your_age >= 16:
    print('maybe you uncle might have your back')
else:
    print('you are too young go back to school!')
# - you can't legally drink but your mates/uncles might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'