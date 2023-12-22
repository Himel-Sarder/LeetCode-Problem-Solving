
def missing_num(n):
    l = len(n)
    all_num = set(range(1, l+1))
    missing = list(all_num - set(n))
    return missing
num = [4, 3, 2, 7, 8, 3] #missing => 1 , 5 , 6
result = missing_num(num)
print(result)

num2 = [4,3, 6, 9,10]
result2 = missing_num(num2) #
print(result2)