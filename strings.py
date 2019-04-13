course = "Python's course for beginners"
print(course)
course = 'Python course for "beginners"'
print(course)

course = '''
comment on line 1
comment on line 2
comment on line 3
'''

print(course)
course = 'Python course for "beginners"'
print(course[0])
print(course[-1]) #last character
print(course[-2]) #last before character
print(course[0:3])
print(course[0:-2])
print(course[:])
print(course[:5])

first = 'John'
last = 'smith'

message = first + ' [' + last + '] is a coder'
#formatted string
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

print(len(msg))
print(msg.upper())
print(msg.lower().find('j'))
print(msg.lower().find('smith'))
print(msg.replace('smith', 'çlaude'))

# 'in' operator

print('jon' in msg.lower())