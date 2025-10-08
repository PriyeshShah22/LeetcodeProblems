test_cases = int(input())


def processed_words(message):
    corrected_words = []
    for word in message:
        if word.startswith("*"):
            corrected_words.pop()
            corrected_words.append(word[1:])
        else:
             corrected_words.append(word)
    return corrected_words


for _ in range(test_cases):
    number = int(input())
    message = []
    for _ in range(number):
        message.append(input())
    correct_message = processed_words(message)
    for word in correct_message:
        print(word)