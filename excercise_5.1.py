# %%
from statistics import mean

inputs = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        float_user_input = float(user_input)
    except ValueError:
         print("Invalid input")
    else:
        inputs.append(float_user_input)

total = sum(inputs)
length = len(inputs)

if length:
    average = mean(inputs)
else:
    average = "Can not calculate average"

print(f"{total} {length} {average}")


