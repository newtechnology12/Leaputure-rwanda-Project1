
print('wellcome to this examination course')

exam = input('do you want to play?: ')

if exam != 'yes':
    quit()

print('ok let start our exam')
score = 0

answer = input('what is teacher name of economics?: ')
if answer == 'sentongo':
    print('correct answer')
    score += 1
else:
    print('wrong answer')
answer = input('what is Rwanda capital?: ')
if answer == 'Kigali':
    print('correct answer')
    score += 1
else:
    print('wrong answer')
answer = input('what is the capital of burundi?: ')
if answer == 'bujumbura':
    print('correct answer')
    score += 1
else:
    print('wrong answer')
print('dear Student your score is: ' + str(score) + "for all this test")
print('and you have : ' + str((score / 3) * 100) + "%.")