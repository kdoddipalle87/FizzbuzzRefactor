__author__ = 'kdoddipalle'
def checkeven(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
def fizzbuzz(n):
    print "I am a function. My name is {}".format(fizzbuzz.__name__)
    for i in range(1, n):
        if (checkeven(i, 3) & checkeven(i, 5)):
            print 'FizzBuzz'
            continue
        if i >= n:
            break
        elif checkeven(i, 3) == True:
            print 'Fizz'
        elif checkeven(i, 5) == True:
            print 'Buzz'
        if (i % 3) != 0 and (i % 5) != 0:
            print i
if __name__ == "__main__":
    fizzbuzz(31)

