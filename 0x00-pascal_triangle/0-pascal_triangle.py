#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    containerArray = []
    pascalArray = [1]
    containerArray.append(pascalArray.copy())
    if n == 1:
        return [[1]]
    pascalArray.append(1)
    containerArray.append(pascalArray.copy())
    triangle = [] 
    for number in range(0,n-2):
        originalArray = [1,1]
        for index in range(0,len(pascalArray) - 1):
            sum = pascalArray[index] + pascalArray[index + 1]
            originalArray.insert(index+1, sum)
            triangle = originalArray.copy()
        pascalArray =  triangle.copy()
        containerArray.append(pascalArray)
       
    return containerArray    

print(pascal_triangle(5))
