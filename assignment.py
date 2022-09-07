list = ['Hassan', 'Khan']

for name in list:
    if (len(name) > 5 and ('n' in name or 'N' in name)):
        print(len(name))


while len(list) >= 1:
    list.pop()

print(list)
