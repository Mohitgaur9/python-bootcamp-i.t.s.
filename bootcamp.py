# Print name
print("MOHIT GAUR")
name = "MOHIT GAUR"
group = "g1"
course = "MCA"
print(name, group, course)

# Type Casting and Salary
salary = float("12345")
print(type(salary))
print(salary)

# Find the current age using input()
print("Enter your birth year:")
bornYear = int(input())
print("Enter the current year:")
currentYear = int(input())
age = currentYear - bornYear
print("Your age is:", age)

# Currency Converter
# Convert rupees to dollars
print("Convert rupees to dollars")
rupeeAmount = float(input("Enter the amount in Rs.: "))
rsToDollar = rupeeAmount / 84
print(f"{rupeeAmount} Rs. converts to ${rsToDollar:.2f}")

# Convert dollars to rupees
print("Convert dollars to rupees")
dollarAmount = float(input("Enter the amount in $: "))
dollarsToRs = dollarAmount * 84
print(f"${dollarAmount} converts to {dollarsToRs:.2f} Rs.")

# Check if you are eligible to vote
userAge = int(input("Enter your age: "))
if userAge >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Check job eligibility
userAge = int(input("Enter your age: "))
userGender = input("Enter your gender (male/female): ").lower()
if userAge > 17 and userGender == "female":
    print("You are eligible for a job")
elif userAge > 17 and userGender == "male":
    print("You are eligible for a private job")
else:
    print("You are not eligible for any job")

# Find the greatest among three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a > c:
    print(a, "- A is greater")
elif b > a and b > c:
    print(b, "- B is greater")
else:
    print(c, "- C is greater")

# Example of using a tuple
mytuple = ("Aman", "Pardeep", "Aytul", "Adrash")
for x in mytuple:
    print(x)

# Example of using a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Print a specific key value from the dictionary
print(thisdict["brand"])

# Print the type of the dictionary
print(type(thisdict))

# Use of OOP in Python
class Mohit:
    def __init__(self):
        self.age = 20
        print("I am from UTTAR PRADESH")

mohit = Mohit()
print(mohit.age)

# Program to calculate age using a class
class AgeCalc:
    def __init__(self):
        self.currentYear = int(input("Enter the current year: "))
        self.birthYear = int(input("Enter the year of birth: "))
        self.age = self.currentYear - self.birthYear

age_instance = AgeCalc()
print("Your age is:", age_instance.age) 

