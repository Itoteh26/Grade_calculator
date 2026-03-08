# Grade Calculator - Chapters 1-3 only
#
# 1. Ask user for exam score (0-100)
print('=' * 40)
print('     GRADE CALCULATOR')
print('=' * 40)
try:
    user_score = float(input('Enter exam score (0-100): '))
    if user_score > 100 or user_score < 0:
        print('invalid score. \nPlease enter a score between 0 and 100.')
    elif user_score >= 70:
        print('A - Excellent')
    elif user_score >= 60:
        print('B - Good')
    elif user_score >= 50:
        print('C - Fair')
    elif user_score >= 45:
        print('D - pass')
    else:
        print('F - Fail')
except ValueError:
    print('Invalid input. \nPlease enter a numeric score between 0 and 100.')
print('=' * 40)
# 2. If score > 100 or < 0, print error message
# 3. If score >= 70, print "A - Excellent"
# 4. If score >= 60, print "B - Good"
# 5. If score >= 50, print "C - Fair"
# 6. If score >= 45, print "D - Pass"
# 7. If score < 45, print "F - Fail"
# 8. Test with different scores