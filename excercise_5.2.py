# %%
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        float_num = float(num)
    except ValueError:
         print("Invalid input")
    else:
        if largest == None or float_num > largest:
            largest = float_num
        if smallest == None or float_num < smallest:
            smallest = float_num

if largest:
    print(f"Maximum is {int(largest)}")
if smallest:
    print(f"Minimum is {int(smallest)}")
else:
    print(f"Can not display largest and smallest value")


