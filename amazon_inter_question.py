# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?

def unique_letter(string: str):
    if not string:
        raise ValueError
    string = string.lower()
    for c in string: # O(n)
        if string.count(c) == 1: # O(n)
            return c
    return ""
    # O(n) * O(n) = O(n^2)
print(unique_letter('jjdfgerd'))

def unique_letter_optimal(string: str):
    if not string:
        raise ValueError
    string = string.lower()
    d = {}
    for c in string:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for k, v in d.items():
        if v == 1:
            return k
    return ""
print(unique_letter_optimal('jjhgdrdh'))
