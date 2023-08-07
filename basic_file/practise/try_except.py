print(15%16)

def calculate_division(num):
    try:
        c=3/0

    except IndexError as e:
        print(e,"test")

    except ZeroDivisionError as zde:
        print(zde,"ct")

    finally:
        print("completed")

calculate_division(0)


