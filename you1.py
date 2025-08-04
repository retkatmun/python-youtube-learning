
'''
data types
textual data
'''

'''
message = "hello world"
new_message = message.replace("hello","welcome")
print(new_message)
print(message.upper())
print(message.count('l'))
print(message.find('world'))

bobby = "bobby's world"
print(bobby)
#to check len of text

len_text = 'hello world'
print(len(len_text))


#slicing

slicing = 'hello world'
print(slicing[1])
print(slicing[5:11])

greeting = 'hello'
name = 'scholar'

message1 = f'{greeting},{name}. welcome!'
#message1 = '{}, {}. welcome!'.format(name,greeting)
print(message1)
'''

#if statement conditionals
'''
language = "rust"

if language == "python":
    print("condition is python")
elif language == "java":
    print("condition is java")
elif language == "javascript":
    print("conditon is javascript")
else:
    print("No match")

user = "admin"
loged_in = True 

if not user == "admin"  or not loged_in == True:
   print("succesfull")
else:
    print("Try again")

a = [1,2,3]
b = [1,2,3]
print(id(a))
'''


#for loop while lopp
'''
nums = [1, 2, 3, 4, 5]

for num in nums:
   if num == 3:
      print("Found!")
      continue
   print("num")
'''
'''
for num in nums:
   for letter in "abc":
        print(num, letter)

for number in range(5):
  print("Attemp", number + 1 , (number + 1) * ".")


for number in range(1, 10, 3):
    print("attemp", number, number, * ".")
'''
for i in range(1, 11):
    print(i)


'''
x = 0

while x < 10:
   if x == 5:
      break
   print(x)
   x += 1
'''


