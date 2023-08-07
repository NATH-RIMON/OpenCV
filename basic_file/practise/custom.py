def calculate_bonous(basic,type):
    if type=="full-time":
        return basic/4
    
    elif type=="trainee":
        return basic/2
    
    else:
        raise Exception ("Not Applicable")
    
try:
    val=calculate_bonous(100,"part")

except Exception as e:
    print(e)

finally :
    
    print("Bonous Added",val)
    print("val :",val)


