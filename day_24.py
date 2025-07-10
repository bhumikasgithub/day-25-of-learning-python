#1
def equal(a, b, c):
    # Step 1: Check if all three are equal
    if a == b == c:
        return 3
    # Step 2: Check if any two are equal
    elif a == b or b == c or a == c:
        return 2
    # Step 3: All are different
    else:
        return 0
print(equal(3, 4, 3))  # Output: 2
print(equal(1, 1, 1))  # Output: 3
print(equal(3, 4, 1))  # Output: 0

#2
def dict_to_list(d):
    # Step 1: Convert dictionary to list of (key, value) tuples
    items = list(d.items())
    
    # Step 2: Sort the list of tuples by the key (i.e., the first element in each tuple)
    sorted_items = sorted(items)
    
    # Step 3: Return the sorted list
    return sorted_items
print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}))  
# ➞ [('B', 2), ('C', 3), ('D', 1)]

print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}))
# ➞ [('dislikes', 3), ('followers', 10), ('likes', 2)]

#3
def mapping(letters):
    result = {}  # Step 1: Create an empty dictionary to store the result

    for letter in letters:  # Step 2: Loop through each lowercase letter
        result[letter] = letter.upper()  # Step 3: Add (lower, upper) pair to the dictionary

    return result  # Step 4: Return the final dictionary
print(mapping(["p", "s"]))         # ➞ {"p": "P", "s": "S"}
print(mapping(["a", "b", "c"]))    # ➞ {"a": "A", "b": "B", "c": "C"}
print(mapping(["a", "v", "y", "z"]))# ➞ {"a": "A", "v": "V", "y": "Y", "z": "Z"}

#4
def vow_replace(txt, vowel):
    vowels = "aeiou"       # Step 1: List of all vowels
    result = ""            # Step 2: Create an empty string to store the result

    for char in txt:       # Step 3: Go through each character in the input text
        if char in vowels:     # Step 4: If the character is a vowel
            result += vowel        # Replace with the given vowel
        else:
            result += char         # Otherwise, keep the character unchanged

    return result           # Step 5: Return the final result string
print(vow_replace("apples and bananas", "u"))
# Output: "upplus und bununus"

print(vow_replace("cheese casserole", "o"))
# Output: "chooso cossorolo"

print(vow_replace("stuffed jalapeno poppers", "e"))
# Output: "steffed jelepene peppers"
