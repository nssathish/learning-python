import random

for i in range(5):
    print(random.random())

for i in range(5):
    print(random.randint(100,200))

team_members = ['sathish','krishanth','muthu','suhas','balaji']

scrum_master = random.choice(team_members)

print(f'scrum master: {scrum_master}')