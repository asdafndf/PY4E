# %%
file_handle = open("mailbox-short.txt")

email_counter = {}

for line in file_handle:
    if line.startswith("From "):
        line = line.split()
        day = line[2]
        email_counter[day] = email_counter.get(day, 0) + 1

print(email_counter)


