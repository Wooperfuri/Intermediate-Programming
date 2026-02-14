# Eligibility Checker Program

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

# Stop program if underage
if age <= 17:
    print("Oops invalid age.")
    exit()

# Ask ID only if age is valid
has_id_input = input("Do you have a valid ID? (yes/no): ").lower()
has_id = True if has_id_input == "yes" else False

# Eligibility check
if age >= 60 and has_id:
    print("Eligible! You also qualify for senior discount.")
elif age >= 18 and has_id:
    print("Eligible!")
else:
    print("Not eligible.")
