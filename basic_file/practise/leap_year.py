year=int(input("Enter Any year:"))

if year%4==0 and year%100==0 and year%400==0:
    print(year,", this is leap year")

else:
    print(year," is not leapyear")