name = input("Enter your name : ")
print(f"Welcome {name} to the Ultimate Quiz Game ")

age = int(input("Enter your age : "))
print(f"Welcome {name} at {age} years old to the Ultimate Quiz Game!")

score = 0

print(" Category: GEOGRAPHY")
print(" Question 1: What is the most poplulated city of Kenya? ")
print("A) Mombasa")
print("B) Kisumu")
print("C) Nairobi")
print("D) Nakuru")
ans1 = input("Your answer (A, B, C, or D): ")
if ans1 == "C":
 print("Correct! Congartulations")
 score += 1
else:
 print("Wrong! The answer was C)Nairobi")

 print("  Category: SCIENCE ")
print("Question 2: What is the chemical symbol for Oxygen?")
print("A) O2")
print("B) OX")
print("C) OG")
print("D) O")
ans2 = input("Your answer : ")
if ans2 == "D":
        print("Correct! Congratulations!")
        score += 1
else:
        print(" Wrong! The answer was D) O")

print("Category: FINANCE")
print("Question 3:What does GDP stand for? ")
print("A) Gross Domestic Product")
print("B) General Debt Percentage")
print("C) Global Distribution Plan")
print("D) Government Deficit Projection")
ans3 = input("Your answer: ")
if ans3 == "A" :
 print("Correct!Congratulations!")
 score += 1
else:
 print("Wrong! The answer was A)")

print("Category: POLITICAL")
print("Question 4: How many permanentmembers does the UN Security Council have?")
print("A) 3")
print("B) 4")
print("C) 5")
print("D) 6")
ans4 = input("Your answer : ")
if ans2 == "C":
 print("Correct!Congratulations!")
 score += 1
else:
 print(" Wrong! The answer was C) 5")

print("Category: COMMON KNOWLEDGE ")
print("Question 5: How many months of the year have 28 days?")
print("A) Only February")
print("B) 6 months")
print("C) 2 months")
print("D) All 12 of them")
ans5 = input("Your answer : ")
if ans5 == "D":
 print(" Correct! All 12 months have *at least* 28 days. February is just the only one with ONLY 28 days!")
 score += 1
else:
 print(" Gotcha! The correct answer is D. All 12 months have at least 28 days!")


print(f"RESULTS FOR {name}")
print(f"TOTAL SCORE: {score}/5")
    