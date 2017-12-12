def two_times(numberlist):
    result = []
    for number in numberlist:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)