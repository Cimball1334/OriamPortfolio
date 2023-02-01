# Excersize 0

# numarr = [int(x) for x in input().split()]
# print(sum(numarr),max(numarr))

#Excersize 1

def trimbyn(arr, n):
    return sorted(arr)[n:-n]

arr = []
x = int(input('Enter the number of entries? '))
for i in range(x):
    arr.append(int(input()))

y = int(input('How many elements would you like to remove? '))
if len(arr) < 2*y:
    print('Array Too Short')
else:
    print(trimbyn(arr,y),arr)


