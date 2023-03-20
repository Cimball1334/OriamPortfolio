'''
Example 1
'''

def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

add_numbers(5, 4)

'''
Example 2
'''
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((2, 10, 5, -1, 7)))


'''
Example 3
'''
def reverse(itr):
  return itr[::-1]

str1 = 'reverse'
print(f"Original: {str1} \nReverse strig:{reverse(str1)}")

'''
Example 4
'''
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(test_prime(7))


'''
Example 5
'''
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('Hello, World!')


'''
Example 6
'''

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))


'''
Example 7
'''
def pascal_triangle(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1
pascal_triangle(6) 

'''
Example 8
'''

def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))


'''
Example 9
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n = 5
print(factorial(n))