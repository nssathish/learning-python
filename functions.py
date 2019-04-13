def greet_user():
    print("Hi there!")
    print("Welcome!!")

greet_user()

def greet_user_with_names(first_name,last_name):
    print(f'Hi {first_name} {last_name}')
    print('Welcome!!')

greet_user_with_names("Seethu", "Sathish")

greet_user_with_names(last_name="Seethu", first_name="Sathish")

greet_user_with_names("Seethu", first_name="Sathish") #runtime error

#greet_user_with_names(first_name="Seethu", "sathish") #compiletime error

greet_user_with_names("Seethu", last_name="Sathish")