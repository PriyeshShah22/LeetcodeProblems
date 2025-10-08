import random
print("WELCOME TO HANGMAN:-")
print("Select a genre")
genres = {
    1: "Movie",
    2: "Physics",
    3: "Chemistry",
    4: "Maths",
    5: "Games",
    6: "Food",
    7: "Players",
    8: "Youtubers",
    9: "Series"
}
for index, genre in enumerate(genres.values()):
    print(f"{index + 1}. {genre}")

selection = int(input("Enter the number of your choice: ")) - 1
difficulty = input("Enter your choice of Difficulty(easy,medium,hard): ").capitalize()
if 0 <= selection < len(genres):
    genre_name = list(genres.values())[selection]
    print(f"You selected: {genre_name}, Difficulty: {difficulty}")
else:
    print("Invalid selection. Please try again.")
    exit()

word_list = {
    "Movie": {
        "Easy": ["Interstellar", "Avengers", "Aashiqui", "Hera Pheri", "Golmaal", "Conjuring", "Incredibles", "KGF", "Stree", "Avatar", "Pushpa"],
        "Medium": ["PK", "The Nun", "The Evil Dead", "RRR", "Chhichhore", "Lights Out", "Singham", "IT", "Oppenheimer"],
        "Hard": ["Fifty Shades of Grey", "Sex and city", "Lage Raho Munna Bhai", "Zindagi Na Milegi Dobara", "Uri", "Gully Boy", "Sholay"]
    },
    "Physics":{
        "Easy": ["Capacitor", "Resistor", "Electricity", "Magnetism", "Optics", "Tension", "Molecule", "Friction", "Proton", "Free Fall"],
        "Medium": ["Bernoullis", "Wavelength", "Thermodynamics", "Amplitude", "Inertia", "Reflection", "Refraction"],
        "Hard": ["Impedance", "Cohesive", "Coulomb", "Archimedes", "Interference", "Relativity", "Viscosity", "Entropy", "Buoyancy", "Quantum Mechanics", "Escape Velocity"]
    },
    "Maths": {
        "Easy": ["Addition", "Subtraction", "Multiplication", "Division", "Fraction", "Decimal", "Percentage", "Geometry"],
        "Medium": ["Algebra", "Trigonometry", "Calculus", "Statistics", "Probability", "Logarithms", "Matrices", "Vectors"],
        "Hard": ["Category Theory", "Algebraic Geometry", "Differential Equation", "Functional Analysis", "Complex Numbers", "Numerical Analysis", "Stochastic Processes", "Optimization Theory"]
    },
    "Chemistry": {
        "Easy": ["Atom", "Molecule", "Element", "Compound", "Mixture", "Solution", "Acid", "Base", "Salt", "Periodic Table"],
        "Medium": ["Chemical Reaction", "Stoichiometry", "Bond", "Ion", "Isotope", "Organic Chemistry", "Inorganic Chemistry", "Biochemistry"],
        "Hard": ["Polymer", "Catalyst", "Thermodynamics", "Kinetics", "Spectroscopy", "Chromatography", "Electrochemistry", "Quantum Chemistry"]
    },
    "Games": {
        "Easy": ["Tic-Tac-Toe", "Hangman", "Guess the Number", "Rock Paper Scissors", "Last of us", "God of War", "Uncharted", "Fall Guys", "Minesweeper", "Valorant"],
        "Medium": ["Sudoku", "Chess", "Scrabble", "Ludo", "Carrom", "Far Cry", "Gta ", "Mortal Kombat", "Chained Together", "Battlefield"],
        "Hard": ["Go", "Bridge", "Poker", "Backgammon", "Asphalt", "Black Myth Wukoing", "Elden Ring", "Red Dead Redemption", "Hollow Night", "Shadow of The Tomb fighter", "Horizon Zero Dawn"]
    },
    "Food": {
        "Easy": ["Pizza", "Burger", "Pasta", "Sushi", "Tacos", "Fried Rice", "French Fries", "Ice Cream", "Chocolate", "Apple Pie"],
        "Medium": ["Curry", "Ramen", "Spaghetti", "Steak", "Salad", "Soup", "Smoothie", "Sandwich", "Burrito", "Quesadilla"],
        "Hard": ["Pho", "Dim Sum", "Biryani", "Sambar", "Dosa", "Falafel", "Shawarma", "Dumplings", "Frankie", "Samosa", "Hummus"]
    },
    "Players": {
        "Easy": ["Messi", "Ronaldo", "Neymar", "Mbappe", "Salah", "Kane", "Lewandowski", "Haaland", "Benzema", "De Bruyne"],
        "Medium": ["Iniesta", "Xavi", "Modric", "Pogba", "Griezmann", "Suarez", "Aguero", "Van Dijk", "Ramos", "Neuer"],
        "Hard": ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Jacques Kallis", "Shane Warne", "Wasim Akram", "Waqar Younis", "Imran Khan", "Brian Lara", "Viv Richards"]
    },
    "Youtubers": {
        "Easy": ["PewDiePie", "MrBeast", "Dude Perfect", "Logan Paul", "Jake Paul", "Ryan Kaji", "Blippi", "Rhett & Link", "Mark Rober", "David Dobrik"],
        "Medium": ["Jacksepticeye", "Valkyrae", "Ninja", "Pokimane", "Shroud", "Asmongold", "xQc", "Sodapoppin", "Corpse Husband", "Sykkuno"],
        "Hard": ["Mr. Beast Gaming", "Ludwig", "xQcOW", "Trainwreckstv", "DrLupo", "Summit1G", "TimTheTatman", "Disguised Toast", "Hasanabi", "MoistCr1tikal"]
    },
    "Series": {
        "Easy": ["Friends", "The Office", "The Big Bang Theory", "Game of Thrones", "Stranger Things", "Breaking Bad", "The Mandalorian", "The Crown", "Bridgerton", "The Witcher"],
        "Medium": ["Dark", "Peaky Blinders", "Chernobyl", "The Boys", "Ozark", "Mindhunter", "The Queen's Gambit", "The Sopranos", "Mad Men", "Westworld"],
        "Hard": ["Mr Robot", "The Leftovers", "True Detective", "Lost", "Twin Peaks", "Watchmen", "The Wire", "Breaking Bad", "The Sopranos", "Mad Men"]
    }
}
selected_word = random.choice(word_list[genre_name][difficulty])
# print(f"{selected_word}")
word_to_guess = selected_word.lower()
guessed_word = ['_' if char!= ' ' else ' ' for char in word_to_guess]
guessed_letter = []


def display_word(guessed_word):
    print(' '.join(guessed_word))
    return None


attempts = None
hints = None
if difficulty == "Easy":
    attempts = 7
    hints = 2
elif difficulty == "Medium":
    attempts = 5
    hints = 2
elif difficulty == "Hard":
    attempts = 6
    hints = 3
else:
    print("Invalid Difficulty level. Please try again.")
if attempts is not None:
    print(f"Attempts Allowed:{attempts}")
    display_word(guessed_word)
while attempts > 0:
    present = False
    guess = input("Guess a letter(for hint type 'hint'):").lower()
    if guess == 'hint':
        if hints > 0:
            hint_letter = random.choice([char for char in word_to_guess if char not in guessed_letter and char != ' '])
            print(f"Hint: The letter '{hint_letter}' is in the word!")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == hint_letter:
                    guessed_word[i] = hint_letter
            hints -= 1
            print(f"Hints left: {hints}")
        else:
            print("No hints left!")
        display_word(guessed_word)
        continue
    if guess in guessed_letter:
        print("You have already guessed that letter.")
    elif guess in word_to_guess:
        guessed_letter.append(guess)
        print(f"Good job! you have guessed correct letter.")
    for i in range(len(word_to_guess)):
        if guess in word_to_guess[i:]:
            idx = word_to_guess[i:].index(guess) + i        #idx= index
            guessed_word[idx] = guess
            present = True
        else:
            guessed_letter.append(guess)
            if not present:
                attempts -= 1
                print(f"Wrong guess! You have {attempts} attempts left.")
            break
    display_word(guessed_word)
    if '_' not in guessed_word:
        print("Congratulations! You won the game.")
        break
else:
    print(f"Sorry, you have run out of attempts. The word was:{selected_word}")