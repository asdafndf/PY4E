# %%
unique_words = []
romeo_handle = open("romeo.txt")
for line in romeo_handle:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
print(sorted(unique_words))


