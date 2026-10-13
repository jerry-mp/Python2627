print('The program will guess your favorite animal!')
classification = input('Is your animal a mammal, a reptile, a bird, or a fish? ').lower()
if classification == 'mammal':
    meow = input('Does your favorite animal meow? ').lower()
    if meow == 'yes':
        meow_size = input('Is this animal big or small? ').lower()
        if meow_size == 'big':
            print('Your favorite animal is a lion!')
        else:
            print('Your favorite animal is a cat!')
    elif meow == 'no':
        woof = input('Does your animal bark? ').lower()
        if woof == 'yes':
            woof_size = input('Is this animal big or small? ').lower()
            if woof_size == 'big':
                print('Your favorite animal is a wolf!')
            else:
                print('Your favorite animal is a dog!')
elif classification == 'reptile':
    slither = input('Does your animal slither on the ground? ').lower()
    if slither == 'yes':
        print('Your favorite animal is a snake!')
    else:
        print('Your favorite animal is a lizard!')
elif classification == 'bird':
    beak = input('Does your animal have a beak for seeds or a beak for meat? ').lower()
    if beak == 'seeds':
        print('Your favorite animal is a chicken!')
    else:
        print('Your favorite animal is an eagle!')
elif classification == 'fish':
    bones = input('Does your animal have bones or cartiledge? ').lower()
    if bones == 'bones':
        print('Your favorite animal is a tuna!')
    else:
        print('Your favorite animal is a shark!')
else:
    print('Sorry, that animal is not covered!')