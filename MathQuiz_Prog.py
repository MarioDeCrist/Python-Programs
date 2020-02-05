'''
Mario DeCristofaro
md2224
9/25/17
CS126 - 001
'''

import random

# Program to generate a math quiz with Beginner, Intermediate, and Advanced questions

# Set Variables
ProbCorrect = 0
# Get Input
print('\n\n=====Welcome to the CS126L Math Quiz Show!=====')
MathQues = int(input('How many problems would you like to attempt?: '))
MathLev = input('Beginner, Intermediate, or Advanced: ')
MathLev = MathLev.lower()
print('\nRemeber to round to the nearest whole number...')
print('===================================')
# Set Conditionals
for i in range(MathQues):
    # Beginner Work
    if MathLev == 'beginner':
        OneTen1 = random.randint(1, 10)
        OneTen2 = random.randint(1, 10)
        operator = random.randint(1, 2)
        if operator == 1:
            addQBeg = OneTen1 + OneTen2
            PCAnswer = addQBeg
            operator = '+'
        elif operator == 2:
            subQBeg = OneTen1 - OneTen2
            PCAnswer = subQBeg
            operator = '-'
        UAns = input('\nWhat is %d %s %d?: ' % (OneTen1, operator, OneTen2))
        UAns = float(UAns)
        if UAns == PCAnswer:
            print('Correct')
            ProbCorrect += 1
        elif UAns != PCAnswer:
            print('Incorrect, the answer is: %d' % (PCAnswer))
# Intermediate Work
    elif MathLev == 'intermediate':
        OneTen1 = random.randint(1, 25)
        OneTen2 = random.randint(1, 25)
        operator = random.randint(1, 4)
        if operator == 1:
            addQBeg = OneTen1 + OneTen2
            PCAnswer = addQBeg
            operator = '+'
        elif operator == 2:
            subQBeg = OneTen1 - OneTen2
            PCAnswer = subQBeg
            operator = '-'
        elif operator == 3:
            mulQBeg = OneTen1 * OneTen2
            PCAnswer = mulQBeg
            operator = '*'
        elif operator == 4:
            divQBeg = OneTen1 / OneTen2
            PCAnswer = round(divQBeg, 2)
            operator = '/'
        tempinput = OneTen1, operator, OneTen2
        UserAnswer = float(input('\nWhat is %d %s %d?: ' % (tempinput)))
        if UserAnswer == PCAnswer:
                    print('Correct')
                    ProbCorrect += 1
        elif UserAnswer != PCAnswer:
                    print('Incorrect, the answer is: %d' % (PCAnswer))
# Advanced Work
    elif MathLev == 'advanced':
        # Operation 1
        operator1 = random.randint(1, 5)
        OneTen1 = random.randint(1, 25)
        OneTen2 = random.randint(1, 25)
        operator = random.randint(1, 5)
        if operator1 == 1:
            addQBeg = OneTen1 + OneTen2
            PCAnswer1 = addQBeg
            operator1 = '+'
        elif operator1 == 2:
            subQBeg = OneTen1 - OneTen2
            PCAnswer1 = subQBeg
            operator1 = '-'
        elif operator1 == 3:
            mulQBeg = OneTen1 * OneTen2
            PCAnswer1 = mulQBeg
            operator1 = '*'
        elif operator1 == 4:
            divQBeg = OneTen1 / OneTen2
            PCAnswer1 = round(divQBeg, 2)
            operator1 = '/'
        elif operator1 == 5:
            expQBeg = OneTen1 ** OneTen2
            PCAnswer1 = round(expQBeg, 2)
            operator1 = '^'
# Operation 2
        OneTen3 = random.randint(1, 25)
        OneTen4 = random.randint(1, 25)
        operator2 = random.randint(1, 5)
        if operator2 == 1:
            addQBeg = OneTen3 + OneTen4
            PCAnswer2 = addQBeg
            operator2 = '+'
        elif operator2 == 2:
            subQBeg = OneTen3 - OneTen4
            PCAnswer2 = subQBeg
            operator2 = '-'
        elif operator2 == 3:
            mulQBeg = OneTen3 * OneTen4
            PCAnswer2 = mulQBeg
            operator2 = '*'
        elif operator2 == 4:
            divQBeg = OneTen3 / OneTen4
            PCAnswer2 = round(divQBeg, 2)
            operator2 = '/'
        elif operator2 == 5:
            expQBeg = OneTen3 ** OneTen4
            PCAnswer2 = round(expQBeg, 2)
            operator2 = '^'
        PCAnswer = PCAnswer1 + PCAnswer2
        t1 = ('%d %s %d' % (OneTen1, operator1, OneTen2))
        t2 = ('%d %s %d' % (OneTen3, operator2, OneTen4))
        UAns = input('\nWhat is (%s) + (%s)?: ' % (t1, t2))
        UAns = float(UAns)
        if UAns == PCAnswer:
                    print('Correct')
                    ProbCorrect += 1
        elif UAns != PCAnswer:
                    print('Incorrect, the answer is: %d' % (PCAnswer))
# Return results
print('\nOut of %d problems, you got %d correct.' % (MathQues, ProbCorrect))
PercentTotal = (ProbCorrect / MathQues)
if PercentTotal == 100 or PercentTotal > (2/3):
    print('Well Done!')
elif PercentTotal <= (2/3)and PercentTotal > (1/3):
    print('You need more practice.')
elif PercentTotal <= (1/3):
    print('Please ask your math teacher for help!')
