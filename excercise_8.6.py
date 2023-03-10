# %%
numbers = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        float_num = float(num)
    except ValueError:
         print("Invalid input")
    else:
        numbers.append(float_num)

if numbers:
    print(f"Maximum is {max(numbers)}")
    print(f"Minimum is {min(numbers)}")
else:
    print(f"Can not display largest and smallest value")


