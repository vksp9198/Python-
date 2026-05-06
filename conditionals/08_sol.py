password_length = 12

if password_length < 6:
    password_strength = "Weak"
elif password_length <= 10:
    password_strength = "Medium"
else:
    password_strength = "Strong"
print("Your password strength is = ",password_strength) 