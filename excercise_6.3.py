# %%
def count(string, letter):
    occurance = 0
    for char in string:
        if char == letter:
            occurance += 1
    return occurance

count("banana", "a")


