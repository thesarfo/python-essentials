#defining variables for the users name, course and score
name = input('Enter your name: ')
course = input('Enter your course: ')
score = float(input('What was your score? '))

#conditions that show the user's grade based on their score
if score > 80:
    print('Name:', name, 'You had an A in', course)
elif score >= 75 and  score <=79:
    print('Name:', name, 'You had a B+ in', course)
elif score >= 70 and  score <=74:
    print('Name:', name, 'You had a B in', course)
elif score >= 65 and  score <=69:
    print('Name:', name, 'You had a C+ in', course)
elif score >= 60 and  score <=64:
    print('Name:', name, 'You had a C in', course)
elif score >= 55 and  score <=59:
    print('Name:', name, 'You had a D+ in', course)
elif score >= 50 and  score <=54:
    print('Name:', name, 'You had a D in', course)
elif score >= 45 and  score <=50:
    print('Name:', name, 'You had an E in', course)
else:
    print('Name:', name, 'You had an F in', course)
