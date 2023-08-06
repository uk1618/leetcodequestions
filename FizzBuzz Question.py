n = int(input())
myList = []
i = 1
while i < n + 1:

    if i % 3 == 0 and i % 5 == 0:
        myList.append("FizzBuzz")
    elif i % 5 == 0:
        myList.append("Buzz")
    elif i % 3 == 0:
        myList.append("Fizz")
    else:
        myList.append(str(i))
    i = i + 1

print(myList)