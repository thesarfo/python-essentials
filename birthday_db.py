birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4',
    'David': 'Nov 23',
    'Emily': 'May 7',
    'Frank': 'Sep 14',
    'Gina': 'Feb 3',
    'Henry': 'Oct 17',
    'Isaac': 'Jul 31',
    'Jack': 'Apr 30',
    'Kelly': 'Jan 15',
    'Larry': 'Dec 1',
    'Maggie': 'Jun 11',
    'Nancy': 'Aug 20',
    'Oliver': 'Feb 28',
    'Peter': 'Nov 7',
    'Quincy': 'Mar 18',
    'Rachel': 'Sep 2',
    'Samuel': 'Jan 11',
    'Tom': 'Jul 25',
    'Ursula': 'Oct 4',
    'Victor': 'Apr 17',
    'Wendy': 'Dec 8',
    'Xavier': 'May 20',
    'Yvette': 'Aug 14',
    'Zoe': 'Feb 9',
    'Aaron': 'Nov 14',
    'Bella': 'Jun 24',
    'Caleb': 'Oct 29',
    'Diana': 'Mar 12',
    'Ethan': 'Jul 6',
    'Fiona': 'Dec 18',
    'Greg': 'May 5',
    'Hannah': 'Sep 10',
    'Ian': 'Feb 23',
    'Julia': 'Nov 19',
    'Kevin': 'Mar 31',
    'Lena': 'Aug 26',
    'Max': 'Jan 6',
    'Nina': 'May 29',
    'Oscar': 'Oct 8',
    'Penelope': 'Apr 15',
    'Quentin': 'Jul 28',
    'Riley': 'Dec 6',
    'Sarah': 'Feb 13',
    'Toby': 'Nov 30',
    'Uma': 'Mar 24',
    'Vincent': 'Sep 7',
    'Willow': 'Jun 16',
    'Xander': 'Jan 28',
    'Yara': 'Aug 9',
    'Zack': 'Feb 4',
    'Abby': 'Nov 11',
    'Ben': 'May 23',
    'Chris': 'Oct 19',
    'Daisy': 'Mar 8',
    'Eli': 'Jul 15',
    'Felicity': 'Dec 2',
    'George': 'Apr 10',
    'Hazel': 'Sep 28',
    'Ivy': 'Feb 18',
    'Jackie': 'Nov 6',
    'Katie': 'Mar 29',
    'Liam': 'Aug 2',
    'Mia': 'Jan 16',
    'Nate': 'Jun 4',
    'Olivia': 'Oct 1',
    'Penny': 'Apr 28',
    'Quinn': 'Jul 22',
    'Ralph': 'Dec 30',
    'Samantha': 'Feb 7',
    'Tina': 'Nov 3',
    'Uri': 'May 12',
    'Violet': 'Sep 19',
    'Wyatt': 'Jan 24',
    'Xiao': 'Aug 6'
}


while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# The updates performed to the database is forgotten when the program terminates
