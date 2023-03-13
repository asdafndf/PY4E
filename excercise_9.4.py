# %%
file_handle = open("mailbox-short.txt")

email_counter = {}

for line in file_handle:
    if line.startswith("From "):
        line = line.split()
        sender = line[1]
        email_counter[sender] = email_counter.get(sender, 0) + 1
        
for key, value in email_counter.items():
    if value == max(email_counter.values()):
        print(key, value)


