"""
Demo some reading of student_letter.txt

Modify your Run-Edit Configuration to point to the project folder, not src!
"""

letter = open("data/student_letter.txt", "rt") # Hard coded file path; danger!
print(letter)

# Phase 1 - practice with tell, read, and
print(" tell start=",letter.tell())

text = letter.read()
print(type(text))
print(len(text))
print(text)
print(" tell end=",letter.tell())

# If you open, you better close
letter.close()

#  Phase 2 Uncomment
letter = open("data/student_letter.txt","rt")
print(" tell start=",letter.tell())
letter.seek(len(text)//2)
print(" tell seek =",letter.tell())
text2 = letter.readlines()
print(" tell end=",letter.tell())
letter.close()

print(type(text2))
print(len(text2))
print(text2)

for index, string in enumerate(text2):
    print("{} : {} ".format(index, string.strip()))
