__author__ = 'kdoddipalle'
n = int(raw_input("Enter any number for FizzBuzz style printing of numbers here: "))
for i in range(1, n):
    if (i % 3) == 0 and (i % 5) == 0:
        print 'FizzBuzz'
        if i >= n:
            break
    elif (i % 3) == 0:
            print 'Fizz'
    elif (i % 5) == 0:
            print 'Buzz'
    if (i % 3) != 0 and (i % 5) != 0:
        print i

else:
    print 'End of Fizz Buzz program'


