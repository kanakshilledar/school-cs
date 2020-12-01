# # 1 Menu based program to
# #     * Find Factorial of Number
# #     * Check for prime number


# # factorial function using recursion
# def factorial(n):
#     if (n == 1):
#         return n
#     else:
#         return n * factorial(n - 1)

# # optimised method to check whether the number is prime
# # instead of looking up to n it just looks for factors
# # <= sqrt(n)
# def prime(n): # returns boolean values
#     if (n <= 1):
#         return False
#     if (n <= 3):
#         return True
    
#     if (n % 2 == 0 or n % 3 == 0):
#         return False
    
#     i = 5
#     while (i * i <= n):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # driver Program 
# while True:
#     print('''
#     \tFactorial Of Number (!)
#     \tCheck whether number is prime (~)
#     \tExit (.)''')

#     choice = input('Enter your choice: ')

#     if (choice == "!"):
#         n = int(input('Enter any number: '))
#         print(factorial(n))
#     if (choice == "~"):
#         n = int(input('Enter any number: '))
#         print(prime(n))
#     if (choice == "."):
#         break
#     if (choice != '.' and choice != '!' and choice != '~'):
#         print('Try again!')



# # 2 Menu based program for 
# #     * Fibonacci Series
# #     * sum of series x / 1 + x / 2 + ... + x / n

# # fibonacci numbers function
# def fibonacci(n):
#     fibSeries = [0, 1]
#     for i  in range(2, n):
#         fibSeries.append(fibSeries[i - 1] + fibSeries[i - 2])    
#     # return list of fibonacci seqence upto n
#     return fibSeries

# # sum series function
# def sumSeries(n, x):
#     sum = 0
#     for i in range(1, n):
#         sum += x / i
#     # return sum of the series
#     return sum

# # driver Program 
# while True:
#     print('''
#     \tFibonacci Series up to n (!)
#     \tSum of the series x / 1 + x / 2 + ... + x / n (~)
#     \tExit (.)''')

#     choice = input('Enter your choice: ')

#     if (choice == "!"):
#         n = int(input('Enter any number: '))
#         print(fibonacci(n))
#     if (choice == "~"):
#         n = int(input('Enter any number: '))
#         x = int(input('Enter value for x: '))
#         print(sumSeries(n, x))
#     if (choice == "."):
#         break
#     if (choice != '.' and choice != '!' and choice != '~'):
#         print('Try again!')



# # 3 Menu based program for
# #     * interchange elements of list
# #     * reverse digits of number

# # function to interchange elements
# def interchangeElements(l):
#     length = len(l)
#     for i in range(0, length - 2):
#         if (i % 2 == 0):
#             l[i], l[i + 2] = l[i + 2], l[i]
#         else:
#             l[i], l[i + 2] = l[i + 2], l[i]

#     return l

# # function to reverse the elements
# def reverse(n):
#     return n[::-1]

# # driver Program 
# while True:
#     print('''
#     \tInterchange alternate elements of list (!)
#     \tReverse number of digits (~)
#     \tExit (.)''')

#     choice = input('Enter your choice: ')

#     if (choice == "!"):
#         l = eval(input('Enter a list: '))
#         print(interchangeElements(l))
#     if (choice == "~"):
#         n = input('Enter any number: ')
#         print(reverse(n))
#     if (choice == "."):
#         break
#     if (choice != '.' and choice != '!' and choice != '~'):
#         print('Try again!')



# # 4 Program to make a calculator
# #     * Add
# #     * Product
# #     * Divide
# #         * Integer Division
# #         * Float
# #         * Remainder

# def add(x, y):
#     return x + y

# def multiply(x, y):
#     return x * y

# def integerDivide(x, y):
#     return x // y

# def floatDivide(x, y):
#     return x / y

# def remainder(x, y):
#     return x % y

# # driver Program 
# while True:
#     print('''
#     \tAdd (+)
#     \tMultiply (*)
#     \tDivide
#     \t\tInteger(//)
#     \t\tFloat(/)
#     \t\tRemainder(%)
#     \tExit (.)''')

#     choice = input('Enter your choice: ')

#     if (choice == "+"):
#         # enter values of a and b
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(add(a, b))
#     if (choice == "*"):
#         # enter values of a and b
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(multiply(a, b))
#     if (choice == '//'):
#         # enter values of a and b
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(integerDivide(a, b))
#     if (choice == '/'):
#         # enter values of a and b
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(floatDivide(a, b))
#     if (choice == '%'):
#         # enter values of a and b
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(remainder(a, b))
#     if (choice == "."):
#         break
#     if (choice != '+' and choice != '*' and choice != '//' and choice != '/' and choice != '%'):
#         print('Try again!')



# # 5 Menu Based Program to calculate
# #     * Power
# #     * Square
# #     * Sum of digits

# def power(x, y):
#     return x ** y
# def square(x):
#     return x ** 2
# def sumDigits(x):
#     sum = 0
#     for digit in str(x):
#         sum += int(digit)
#     return sum

# # driver Program 
# while True:
#     print('''
#     \tPower (^)
#     \tSquare (**)
#     \tSum of Digits (+)
#     \tExit (.)''')

#     choice = input('Enter your choice: ')

#     if (choice == "^"):
#         a = int(input('$ '))
#         b = int(input('$ '))
#         print(power(a, b))
#     if (choice == "**"):
#         n = input('$ ')
#         print(square(n))
#     if (choice == '+'):
#         n = int(input('$ '))
#         print(sumDigits(x))
#     if (choice == "."):
#         break
#     if (choice != '+' and choice != '^' and choice != '**'):
#         print('Try again!')