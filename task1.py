persons = [{'name': 'Hassan', 'age': 23, 'hobbies': ['cricket']},
           {'name': 'Khan', 'age': 12, 'hobbies': ['cricket']}]
print(persons)

names = [person['name'] for person in persons]
print(names)

older = [person['name'] for person in persons if person['age'] > 20]
print(older)

# copied_person = persons[:]
copied_persons = [person.copy() for person in persons]
copied_persons[0]['name'] = 'Test'
print(copied_persons)
print(persons)

p1, p2 = persons
print(p1, p2)
