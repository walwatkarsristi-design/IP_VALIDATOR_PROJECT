password=input("Enter your password:")

length=len(password)
print("password length is:",length)
if(length<8):
    print("Weak password")
else:
    print("Strong password")
has_upper=False
has_lower=False
has_digit=False
has_symbol=False
for char in password:
  if char.isupper():
    has_upper=True
  if char.islower():
    has_lower=True
  if char.isdigit():
     has_digit=True
  if char.isalnum():
     has_symbol=True
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digit:", has_digit)
print("symbol:", has_symbol)
score=0
if length >= 8:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_symbol:
    score += 1
    if score <= 2:
     print("Password Strength: Weak")

elif score <= 4:
    print("Password Strength: Medium")

else:
    print("Password Strength: Strong")
