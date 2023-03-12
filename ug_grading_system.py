while True:
    name = input('Enter your name: ')
    course = input('Enter your course: ')
    score = float(input('What was your score? '))

    # conditions that show the user's grade based on their score
    if score > 80:
        print('Name:', name, ' Course:', course, ' Grade: A')
    elif score >= 75 and  score <=79:
        print('Name:', name, ' Course:', course, ' Grade: B+')
    elif score >= 70 and  score <=74:
        print('Name:', name, ' Course:', course, ' Grade: B')
    elif score >= 65 and  score <=69:
        print('Name:', name, ' Course:', course, ' Grade: C+')
    elif score >= 60 and  score <=64:
        print('Name:', name, ' Course:', course, ' Grade: C')
    elif score >= 55 and  score <=59:
        print('Name:', name, ' Course:', course, ' Grade: D+')
    elif score >= 50 and  score <=54:
        print('Name:', name, ' Course:', course, ' Grade: D')
    elif score >= 45 and  score <=50:
        print('Name:', name, ' Course:', course, ' Grade: E')
    else:
        print('Name:', name, ' Course:', course, ' Grade: F')

    # ask user if they want to continue
    choice = input('Do you want to enter another score? (y/n): ')
    if choice.lower() == 'n':
        break
