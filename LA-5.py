# Grade Calculator Program

score = int(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a value between 0 and 100.")
else:
    if score >= 97:
        grade = "A+"
        message = "Outstanding!"
    elif score >= 93:
        grade = "A"
        message = "Excellent!"
    elif score >= 90:
        grade = "A-"
        message = "Great job!"
    elif score >= 87:
        grade = "B+"
        message = "Very Good!"
    elif score >= 83:
        grade = "B"
        message = "Good work!"
    elif score >= 80:
        grade = "B-"
        message = "Nice effort!"
    elif score >= 70:
        grade = "C"
        message = "Good!"
    elif score >= 60:
        grade = "D"
        message = "You passed."
    else:
        grade = "F"
        message = "Failed. Try again."

    print("Score:", score, "-> Grade:", grade, "-", message)
