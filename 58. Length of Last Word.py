words = str(input("Enter your sentence:")).strip().split()
if not words:
    print("0")
else:
    last_word = words[-1]
    cleaned_word = ""
    for char in last_word:
        if char.isalpha():
            cleaned_word += char
    print(len(cleaned_word))
'''print(len(words[-1]))'''