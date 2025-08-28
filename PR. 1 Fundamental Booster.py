print("=== Personal Info Form ===")
print("This program collects a few details and shows their data types.")

# Collect
name_txt = input("Enter your name: ")
ageYears = int(input("Enter your age (in years): "))
heightMeter = float(input("Enter height (meters): "))
luckyNumber = int(input("Enter your favourite number: "))

# Types and memory
print("\n--- Summary ---")
print("name_txt =", name_txt, "| type ->", type(name_txt), "| id ->", id(name_txt))
print("ageYears =", ageYears, "| type ->", type(ageYears), "| id ->", id(ageYears))
print("heightMeter =", heightMeter, "| type ->", type(heightMeter), "| id ->", id(heightMeter))
print("luckyNumber =", luckyNumber, "| type ->", type(luckyNumber), "| id ->", id(luckyNumber))

# Arithmetic
birthGuess = 2025 - ageYears
print("\nBirth year guess:", birthGuess)
print("Note: birth year is calculated using", 2025, "-", ageYears)
print("\nThanks!")