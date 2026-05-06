"""
Use this file as a 'factory' to build our instances of Person
 and test some operations
"""
# pylint: disable-msg=C0103

from src.person import Person

hopper = Person("Grace", "M.", "Hopper")
print(hopper)
print(id(hopper))

# https://webpages.uncc.edu/mperez19/twolastnames.html
# https://diverseeducation.com/article/198351
# https://en.wikipedia.org/wiki/ISO/IEC_8859-1
person1 = Person("Manuel", "A.", "P\xE9rez", "Qui\xF1ones")
print(person1)

person2 = Person("Grace", "M.", "Hopper")
print("id2=", id(person2))
print(person1 == hopper)
print(person2 == hopper)
print(person2 is hopper)

hopper2 = Person("Dennis", "Lee", "Hopper")

ptrib = Person("Paul", "", "Trible")
print("PTrib", ptrib)

provost = Person("Dave", "", "Doughty")
print(provost)

dean = Person("Nicole", "R.", "Guajardo")
print(dean)

dept = Person("Toni", "", "Riedl")
print(dept)
print(type(dept))
print("is type Person? ", type(dept) == Person)
print("is instance of Person? ", isinstance(dept, Person))


stu1 = Person("Captain", "Chris", "Newport")
print(stu1)

people = [Person("Miguel", "", "P\xE9rez"), hopper, person1,
          Person("Dario", "", "P\xE9rez", "Flores"), hopper2,
          Person("N\xE9ster", "Luis", "P\xE9rez", "Luzardo"),
          person2, Person("Isaac", "Tatum", "Hopper"), Person("Thomas", "Edward", "Hopper"),
          Person("Chief", "Jim", "Hopper"),
          ptrib, provost, dean, dept, stu1]


for person in people:
    print(person)

print(30*"="+"Sorted"+30*"=")
sorted_people = people[:]
sorted_people.sort()
for person in sorted_people:
    print(person)

print(30*"="+"UnSorted"+30*"=")

for person in people:
    print(person)
