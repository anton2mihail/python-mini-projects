def addOne(values):
    for i in range(len(values)):
        if values[i]%2 != 0:
            values[i] = values[i] +1
    print(values)

def main():
    addOne([1,4,6,8,9,0,3,5,7])
    addOne([4, 4, 5, 5, 13, 10, 13, 15, 17])
    addOne([11, 46, 67, 87, 97, 0, 37, 57, 77])
    addOne([1, 4, 6, 8, 9, 0, 3, 5, 7])



main()