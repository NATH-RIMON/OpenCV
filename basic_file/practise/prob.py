for i in range(1,51,1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

    else:
        print(i)

#Write a nested loop to print counting table from 1 to 10.

for i in range(1,11,1):
    for j in range(1,11,1):
        print( i,"X" ,j ,"=", i*j)

    print("\n")
        


