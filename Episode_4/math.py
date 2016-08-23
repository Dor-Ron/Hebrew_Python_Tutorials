'''
מוסיפים מספרים ככה
'''

print(1 + 7 + -9)

'''
חיסור מספרים
'''

print(8 - 9 - 12)

'''
חילוק מספרים

בפייתון 2 חילוק בין 2 מספרים מסוג מספר מלא מחזיר מספר מלא
כגון:

9 / 2 = 4

אבל בין סוג נקודה צפה למספר שלם:

9.0 / 2 = 4.5

וגם שני סמני חילוק משקיפים התנהגות של חילוק בין מספרים מלאים

9.0 // 2 = 4.0

אבל פייתון 3 יותר חכמה אז
'''

print(9 / 2) # => 4.5

'''
כיפול מספרים
'''

print(8 * 7)

'''
ואל תשכחו את סדר הפעולות

8 * 2 + 3

שונה מ

8 * (2 + 3)
'''

'''
כוח של מספר
'''

print(2 ** 3)
print( pow(2, 3) )

'''
למצוא מה שנשאר מחילוק
מה שנקרא מודולוס
'''

print(11 % 3)  # => 2


'''
ייבוי מודול / ספרייה
'''

import math

'''
אל תשכחו שלהשתמש בספרייה צריך להתחיל עם

math.
'''

print(math.cos(2))
print(math.sin(2.6))
print(math.tan(1.7))
print(math.pi)
print(math.e)
print(math.sqrt(9))  # => 3 שורש

print(math.floor(12.9))  # => 12
print(math.ceil(12.1))  # => 13
print(round(12.49))  # => 12
print(round(12.51))  # => 13


'''
לבדוק את התוכן של ספריית "math"
'''

print(dir(math))
