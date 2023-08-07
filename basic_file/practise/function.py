# def sub_fnc(num2, num1):
#     return num1 - num2

# sub=sub_fnc(20,10)
# print(sub)

# def sum_fnc(*k):
#     return sum(k)

# sum_1 = sum_fnc(1, 2, 3)
# print(sum_1)


# sum_2 = sum_fnc(1, 2, 3, 4, 5, 6, 7, 8)
# print(sum_2)

def my_fun(n):
    if n==0:
        return 0
    
    else:
        return n +my_fun(n-1)
    
res=my_fun(5)
print(res)