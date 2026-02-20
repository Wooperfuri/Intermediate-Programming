# Eligibility Checker Program

age = int(input("Enter your age: "))
has_id = False 

if age >= 18:
    has_id_input = input("Do you have a valid ID? (yes/no): ").lower()
    
    if has_id_input == "yes":
        has_id = True

if age < 18:
    print("Not eligible.")
elif age >= 60 and has_id:
    print("Eligible for senior discount.")
elif age >= 18 and has_id:
    print("Eligible!")
else:
    print("Not eligible. Valid ID required.")
