# %%
file_name = input("Enter a file name: ")
try:
    file_handle = open(file_name)

except FileNotFoundError:
    if file_name == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print(f"File cannot be opened: {file_name}")

else:
    count = 0
    for line in file_handle:
        count += 1

    print(f"There were {count} subject lines in {file_name}")


