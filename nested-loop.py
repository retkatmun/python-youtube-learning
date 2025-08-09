	
'''
for x in range(5):
   for y in range(3):
       print(f"{x},{y}")


#iterable
for x in "python":
    print(x)

count = 0
for number in range(1, 11,):
    if number % 2 == 0:
        count += 1
        print(number)
'''

import random

students = []
count = 1

while count <= 1000:
    student = {
        "id": count,
        "name": f"Student{count}",
        "score": random.randint(0, 100)  
    }
    students.append(student)
    count += 1


for s in students:
    print(s)

# Total students
print(f"\nTotal students generated: {len(students)}")

'''
# Check ticket eligibility and discounts
if age >= 60:
    print("You are eligible to buy a ticket.")
    print("You get a **Senior Discount**.")
elif age >= 18:
    print("You can buy a regular movie ticket.")
elif age >= 12:
    print("You can buy a **Teen Ticket**.")
else:
    print("You can buy a **Kid Ticket**.")

'''
