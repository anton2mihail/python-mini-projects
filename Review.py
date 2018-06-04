def addOne(low, high):
    sum = 0
    for i in range(low, high+1):
        if i%2 != 0:
            sum = sum + i
    return sum

def main():
    print(addOne(1,5))
    print(addOne(1, 8))
    print(addOne(9, 16))
    print(addOne(1,2).isalpha())
    print(isinstance(23.0002,int))


main()