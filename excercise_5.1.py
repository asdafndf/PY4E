# %%
total = 0
count = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        float_user_input = float(user_input)
    except ValueError:
         print("Invalid input")
    else:
        total += float_user_input
        count += 1

if count:
    average = total / count
else:
    average = "Can not calculate average"

print(total, count, average)


