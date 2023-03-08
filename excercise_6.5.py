# %%
string = 'X-DSPAM-Confidence:0.8475'
colon_position = string.find(":")
number = float(string[colon_position + 1:])
print(number)


