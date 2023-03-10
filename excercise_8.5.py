# %%
count = 0
mailbox_handle = open("mailbox.txt")
for line in mailbox_handle:
    if line.startswith("From "):
        line = line.split()
        print(line[1])
        count += 1
print(f"There were {count} lines in the file with From as the first word")


