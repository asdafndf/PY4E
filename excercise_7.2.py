# %%
file_name = input("Enter a file name: ")
try:
    file_handle = open(file_name)

except FileNotFoundError:
    print("File not found")

else:
    total = 0
    count = 0
    for line in file_handle:
        if line.startswith("X-DSPAM-Confidence:"):
            colon_position = line.find(":")
            number = float(line[colon_position+1:])
            total += number
            count += 1
    if count:
        print(f"Average spam confidence: {total/count}")


