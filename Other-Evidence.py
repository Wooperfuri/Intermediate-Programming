# movie_ticket_system.py

# ===== Part A: User Inputs =====
day = input("Day type (weekday/weekend): ").lower()
customer = input("Customer type (regular/student/senior): ").lower()
time = int(input("Movie time (9–22 in 24hr format): "))
tickets = int(input("Number of tickets: "))

# ===== Part D: Validate Inputs =====
if time < 9 or time > 22:
    print("Invalid time. Cinema operates from 9 to 22 only.")
    exit()

if tickets <= 0:
    print("Ticket count must be positive.")
    exit()

# ===== Part B: Base Pricing =====
if day == "weekday":
    base_price = 200
elif day == "weekend":
    base_price = 300
else:
    print("Invalid day type.")
    exit()

subtotal = base_price * tickets
discount = 0

# ===== Part C: Discounts (Nested Conditionals) =====

# Customer discount
if customer == "student":
    discount += subtotal * 0.20
elif customer == "senior":
    discount += subtotal * 0.30

# Matinee discount (before 12pm)
if time < 12:
    discount += subtotal * 0.10

# Group discount
if tickets >= 5:
    discount += subtotal * 0.05

# ===== Part E: Receipt =====
final_total = subtotal - discount

print("\n----- ITEMIZED RECEIPT -----")
print("Base price per ticket: ₱", base_price)
print("Number of tickets:", tickets)
print("Subtotal: ₱", subtotal)
print("Total discounts: ₱", round(discount, 2))
print("Final Total: ₱", round(final_total, 2))
