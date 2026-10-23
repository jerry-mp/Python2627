animals = ['armadillo', 'eel', 'mouse', 'lion', 'beaver', 'pangolin']
what_animal = int(input('Pick a number between 1 and 6: '))
if what_animal in range(1, len(animals)+1):
    print('You won a... ')
    if what_animal == 1:
        print(animals[what_animal-1])
    elif what_animal == 2:
        print(animals[what_animal-1])
    elif what_animal == 3:
        print(animals[what_animal-1])
    elif what_animal == 4:
        print(animals[what_animal-1])
    elif what_animal == 5:
        print(animals[what_animal-1])
    elif what_animal == 6:
        print(animals[what_animal-1])
else:
    print('That is not an option')