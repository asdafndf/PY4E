# %%
class ValueOutOfRangeError(Exception):
    pass


def computepay(score):
    if score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score: "))
    if score < 0.0 or score > 1.0:
        raise ValueOutOfRangeError

except ValueError:
    print("Not a valid score")

except ValueOutOfRangeError:
    print("Not a valid score")
    
else:
    print(computepay(score))


