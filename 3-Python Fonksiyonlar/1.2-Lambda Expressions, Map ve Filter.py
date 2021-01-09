def square(num): return num ** 2

numbers = [1,3,7,12]
result = list(map(square, numbers))
print(result)

# for item in map(square, numbers):
#   print(item)

"********************************"
# square = lambda num: num ** 2
# result = list(map(square, numbers))

numbers = [3,5,8,16]
result = list(map(lambda num: num ** 2, numbers))
print(result)


"********************************"

def check_even(num): return num%2 == 0

numbers = [4,5,3,1,10]

result = list(filter(check_even, numbers))
print(result)