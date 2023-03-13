# %%
file_handle = open("mailbox-short.txt")

email_counter = {}

for line in file_handle:
    if line.startswith("From "):
        at_index = line.find("@")
        space_index = line.find(" ", at_index)
        domain = line[at_index+1:space_index]
        email_counter[domain] = email_counter.get(domain, 0) + 1

print(email_counter)


