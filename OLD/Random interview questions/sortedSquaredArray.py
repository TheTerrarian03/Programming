def returnSortedSquaredarray(array):
    orArray = []
    for item in array:
        orArray.append(item * item)
    orArray.sort()
    return(orArray)


unOrArray = [-7, -8, -9, -7, -6, -5, -4, -1, 5, 3, 8, 6, 7]
print(returnSortedSquaredarray(unOrArray))
