# %%
try:
    float_hours = float(input("Enter Hours: "))
    float_rate = float(input("Enter Rate: "))

except:
    print("Error, please enter numeric input")

else:
    if float_hours > 40:
        pay = 40 * float_rate + (float_hours - 40) * float_rate * 1.5
    else:
        pay = float_hours * float_rate
    
    print(f"Pay: {pay}")


