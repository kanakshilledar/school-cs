# 1 Menu based program to
#     * Find Factorial of Number
#     * Check for prime number


# factorial function using recursion
def factorial(n):
    if (n == 1):
        return n
    else:
        return n * factorial(n - 1)

# optimised method to check whether the number is prime
# instead of looking up to n it just looks for factors
# <= sqrt(n)
def prime(n): # returns boolean values
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    
    if (n % 2 == 0 or n % 3 == 0):
        return False
    
    i = 5
    while (i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# driver Program 
while True:
    print('''
    \tFactorial Of Number (!)
    \tCheck whether number is prime (~)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "!"):
        n = int(input('Enter any number: '))
        print(factorial(n))
    if (choice == "~"):
        n = int(input('Enter any number: '))
        print(prime(n))
    if (choice == "."):
        break
    if (choice != '.' and choice != '!' and choice != '~'):
        print('Try again!')



# 2 Menu based program for 
#     * Fibonacci Series
#     * sum of series x / 1 + x / 2 + ... + x / n

# fibonacci numbers function
def fibonacci(n):
    fibSeries = [0, 1]
    for i  in range(2, n):
        fibSeries.append(fibSeries[i - 1] + fibSeries[i - 2])    
    # return list of fibonacci seqence upto n
    return fibSeries

# sum series function
def sumSeries(n, x):
    sum = 0
    for i in range(1, n):
        sum += x / i
    # return sum of the series
    return sum

# driver Program 
while True:
    print('''
    \tFibonacci Series up to n (!)
    \tSum of the series x / 1 + x / 2 + ... + x / n (~)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "!"):
        n = int(input('Enter any number: '))
        print(fibonacci(n))
    if (choice == "~"):
        n = int(input('Enter any number: '))
        x = int(input('Enter value for x: '))
        print(sumSeries(n, x))
    if (choice == "."):
        break
    if (choice != '.' and choice != '!' and choice != '~'):
        print('Try again!')



# 3 Menu based program for
#     * interchange elements of list
#     * reverse digits of number

# function to interchange elements
def interchangeElements(l):
    length = len(l)
    for i in range(0, length - 2):
        if (i % 2 == 0):
            l[i], l[i + 2] = l[i + 2], l[i]
        else:
            l[i], l[i + 2] = l[i + 2], l[i]

    return l

# function to reverse the elements
def reverse(n):
    return n[::-1]

# driver Program 
while True:
    print('''
    \tInterchange alternate elements of list (!)
    \tReverse number of digits (~)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "!"):
        l = eval(input('Enter a list: '))
        print(interchangeElements(l))
    if (choice == "~"):
        n = input('Enter any number: ')
        print(reverse(n))
    if (choice == "."):
        break
    if (choice != '.' and choice != '!' and choice != '~'):
        print('Try again!')



# 4 Program to make a calculator
#     * Add
#     * Product
#     * Divide
#         * Integer Division
#         * Float
#         * Remainder

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def integerDivide(x, y):
    return x // y

def floatDivide(x, y):
    return x / y

def remainder(x, y):
    return x % y

# driver Program 
while True:
    print('''
    \tAdd (+)
    \tMultiply (*)
    \tDivide
    \t\tInteger(//)
    \t\tFloat(/)
    \t\tRemainder(%)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "+"):
        # enter values of a and b
        a = int(input('$ '))
        b = int(input('$ '))
        print(add(a, b))
    if (choice == "*"):
        # enter values of a and b
        a = int(input('$ '))
        b = int(input('$ '))
        print(multiply(a, b))
    if (choice == '//'):
        # enter values of a and b
        a = int(input('$ '))
        b = int(input('$ '))
        print(integerDivide(a, b))
    if (choice == '/'):
        # enter values of a and b
        a = int(input('$ '))
        b = int(input('$ '))
        print(floatDivide(a, b))
    if (choice == '%'):
        # enter values of a and b
        a = int(input('$ '))
        b = int(input('$ '))
        print(remainder(a, b))
    if (choice == "."):
        break
    if (choice != '+' and choice != '*' and choice != '//' and choice != '/' and choice != '%'):
        print('Try again!')



# 5 Menu Based Program to calculate
#     * Power
#     * Square
#     * Sum of digits

def power(x, y):
    return x ** y
def square(x):
    return x ** 2
def sumDigits(x):
    sum = 0
    for digit in str(x):
        sum += int(digit)
    return sum

# driver Program 
while True:
    print('''
    \tPower (^)
    \tSquare (**)
    \tSum of Digits (+)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "^"):
        a = int(input('$ '))
        b = int(input('$ '))
        print(power(a, b))
    if (choice == "**"):
        n = input('$ ')
        print(square(n))
    if (choice == '+'):
        n = int(input('$ '))
        print(sumDigits(x))
    if (choice == "."):
        break
    if (choice != '+' and choice != '^' and choice != '**'):
        print('Try again!')



# 6. Program with the following function characteristics
#     * Cube of number with default value 2 (no return).
#     * Checks whether the two input characters are equal (return T/F)

def cube(x = 2):
    print(x ** 3)

def characters(a, b):
    if (a == b):
        return True
    else:
        return False

# cube calculator
n = int(input('$ '))
cube(n)
# character checker
x = input('$ ')
y = input('$ ')
print(characters(x, y))



# 7. Menu Based Phone Dictionary
#     * Create Phone Dictionary
#     * Edit Phone Dictionary
#         * Phone Number
#         * Display
#     * Display all Data

numbers = {}
while True:
    print('''
    * Create Phone Dictionary (c)
    * Edit Phone Dictionary (e)
        ** Phone Number (p)
        ** Display (d)
    * Display all data (i)
    * Exit (x)
    ''')

    choice = input('Enter your choice: ')

    # creating directory
    if (choice == 'c'):
        # name and number input
        name = input('$ ')
        phone = input('$ ')
        numbers[name] = phone
    # editing phone dict
    if (choice == 'e'):        
        task = input('Enter task: ')
        # edit number
        if (task == 'p'):
            name = input('$ ')
            changeNumber = input('$ ')
            numbers[name] = changeNumber
        # edit display
        if (task == 'd'):
            name = input('$ ')
            changeName = input('$ ')
            numbers[changeName] = numbers[name]
            del numbers[name]
    # display all data
    if (choice == 'i'):
        for x in numbers.keys():
            print('Name: ', x, '\tNumber: ', numbers[x])
    if (choice == 'x'):
        break



# 8. Dictionary with keys as month names and values as number of days
#     * Ask the user to enter month name and print no of days
#     * Print out all of the keys in alphabetical order
#     * Print all the months in alphabetical order

year = {'January' : 31, 'February' : 28, 'March' : 31, 'April' : 30, 
    'May' : 31, 'June' : 30, 'July' : 31, 'August' : 31, 'September' : 30,
    'October' : 31, 'November' : '30', 'December' : 31}


# input month name
month = input('Enter month name: ')
print('>>> ', year[month])

# print all keys
months = year.keys()
# converting dict_keys() to list()
months = list(months)
# sorting months
months.sort()
print(months)

# printing months with 31 days
print('Months having 31 days!')
for month in year:
    if (year[month] == 31):
        print(month, end = ' ')

print()



# 9. Menu based program for 
#     * Sorting elements with bubble sort
#     * Factorial of a number in function

def factorial(n):
    if (n == 1):
        return n
    else:
        return n * factorial(n - 1)

def bSort(l):
    length = len(l)

    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if (l[j] > l[j + 1]):
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


# driver Program 
while True:
    print('''
    \tFactorial Of Number (!)
    \tBubble Sort Implementation (~)
    \tExit (.)''')

    choice = input('Enter your choice: ')

    if (choice == "!"):
        n = int(input('Enter any number: '))
        print(factorial(n))
    if (choice == "~"):
        l = eval(input('Enter list of elements: '))
        print(bSort(l))
    if (choice == "."):
        break
    if (choice != '.' and choice != '!' and choice != '~'):
        print('Try again!')



# 10. Menu based program to display working of any five functions of
    # * Math Library
    # * String Library
    # * Statistics Library

import math
import string
import statistics

def mathLibrary():
    print('Floor of 5.19')
    x = 5.19
    print('>>> ', math.floor(x))
    print('Ceil of 5.19')
    print('>>> ', math.ceil(x))
    print('Degree to Raidan')
    print('>>> ', math.radians(x))
    y = 11
    print('Radian to Degree')
    print('>>> ', math.degrees(y))
    print('Sin(x)')
    print('>>> ', math.sin(x))

def stringLibrary():
    print('ascii_letters')
    print('>>> ', string.ascii_letters)
    print('ascii_lowercase')
    print('>>> ', string.ascii_lowercase)
    print('ascii_uppercase')
    print('>>> ', string.ascii_uppercase)
    print('digits')
    print('>>> ', string.digits)
    print('hexDigits')
    print('>>> ', string.hexdigits)
    
def statisticsLibrary():
    print('Mean')
    l = [1, 2, 3, 4, 5, 6, 10]
    print('>>> ', statistics.mean(l))
    print('Mode')
    print('>>> ', statistics.mode(l))
    print('Median')
    print('>>> ', statistics.median(l))
    print('Standard Deviation')
    print('>>> ', statistics.stdev(l))
    print('Variance')
    print('>>> ', statistics.variance(l))

# driver Program 
while True:
    print('''
    \tMath Library (!)
    \tStatistics Library (~)
    \tString Library (?)
    \tExit (.)''')

    choice = input('Enter your choice: ')
    # display math
    if (choice == "!"):
        mathLibrary()
    # display statistics
    if (choice == "~"):
        statisticsLibrary()
    # display string
    if (choice == "?"):
        stringLibrary()
    # exit 
    if (choice == "."):
        break
    
    if (choice != '?' and choice != '!' and choice != '~'):
        print('Try again!')



# 11. Menu based program to
#     * Input list
#     * Display contents
#     * Replace all numbers divisible with 10 to 0

l = []
# driver Program 
while True:
    print('''
    \tEnter into List (!)
    \tDisplay List (~)
    \tReplace all numbers with 10 to 0 (?)
    \tExit (.)''')

    choice = input('Enter your choice: ')
    
    # input into List
    if (choice == "!"):
        l = eval(input('$ '))
    # Display List
    if (choice == "~"):
        print(l)
    # Replace number divisible 10 by 0
    if (choice == "?"):
        for i in range(len(l)):
            if (l[i] % 10 == 0):
                l[i] = 0
    # exit 
    if (choice == "."):
        break
    
    if (choice != '?' and choice != '!' and choice != '~'):
        print('Try again!')



# 12. Menu Based 
#     * Swap elements at the even location with elements at odd
#     * search for a given element in the list
#     * find the larges and smallest number in list.

# swapping odd elements with even
def swapper(l):
    op = l[:]
    evenIndex, oddIndex = 0, 1
    for value in l:
        if value % 2 == 0:
            op[evenIndex] = value
            evenIndex += 2
        else:
            op[oddIndex] = value
            oddIndex += 2

    return op

# recursive binary search approach
def bSearch(l, low, high, x):
    if (high >= low):
        mid = (low + high) // 2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            return bSearch(l, low, mid - 1, x)
        else:
            return bSearch(l, mid + 1, high, x)
    else:
        # returns -1 is no matching element is found
        return -1


# driver Program 
# enter elements into list
l = eval(input('$ '))
while True:
    print('''
    \tSwap Elements (!)
    \tSearch Element (~)
    \tLargest and Smallest Number (?)
    \tExit (.)''')

    choice = input('Enter your choice: ')
    
    # swap element
    if (choice == "!"):
        print('>>> ', swapper(l))
    # search element
    if (choice == "~"):
        x = int(input('$ '))
        print('>>> ', bSearch(l, 0, len(l) - 1, x))
    # smallest and largest element
    if (choice == "?"):
        print('>>> ', max(l), '\t', min(l))
    # exit 
    if (choice == "."):
        break
    
    if (choice != '?' and choice != '!' and choice != '~'):
        print('Try again!')
