def singlenumber(array):
    result=0
    for i in array:
        result=result^i
    return result
array=list(map(int,input().split()))
print(singlenumber(array))
