roman_number = input("Enter the Roman numer:").upper()

numbers = {
     'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000
 }
integer = 0

for i in range(len(roman_number)):
        number1 = roman_number[i]
        number2 = roman_number[i + 1] if i+1 < (len(roman_number)) else None

        if number2 and numbers[number1] < numbers[number2]:
            integer -= numbers[number1]
        else:
            integer += numbers[number1]

print(integer)