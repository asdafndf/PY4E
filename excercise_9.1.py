# %%
txt_handle = open("excercise_9.1_raw.txt")

word_dict = {}

for line in txt_handle:
    words = line.split()
    for word in words:
        word_dict[word] = "random_value"

print(word_dict)


