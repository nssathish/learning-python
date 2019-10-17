command = ""
car_has_started = False

while command != 'quit':
    command = input('>').lower().strip()
    if command == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit the game')
    elif command == 'start':
        if car_has_started:
            print('Car has already started')
        else:
            car_has_started = True
            print('Car started.. Ready to go..')
    elif command == 'stop':
        if not car_has_started:
            print('Car has already stopped')
        else:
            car_has_started = False
            print('Car stopped.')
    elif command == 'quit':
        break
    else:
        print("Sorry, i don't understand that")
