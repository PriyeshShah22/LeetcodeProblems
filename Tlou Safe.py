import random

safe_code = str(random.randint(10000000, 99999999))
attempts = 0

while attempts < 6:
  guess = input("Enter your 8-digit guess: ")

  if len(guess) != 8:
    print("Invalid input. Please enter an 8-digit number.")
    continue

  feedback = ""
  for i in range(8):
    if guess[i] == safe_code[i]:
      feedback += "O"  # Correct digit
    elif guess[i] in safe_code:
      feedback += "X"  # Digit present but in wrong position
    else:
      feedback += "-"  # Digit not present
  print(feedback)

  if feedback == "OOOOOOOO":
    print("You cracked the safe!")
    exit()

  attempts += 1
print("You failed to crack the safe.")