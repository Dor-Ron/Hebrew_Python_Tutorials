# לקלוט בפייתון משתמשיפ בפונקצייט input
# שמחזירה סוג של מחרוזת
username = input("Your name: ")
print(username)

# בגלל שinput
# מחזירה מחרוזת מתמתיקה יכולה להפתיע אותנו
first = input("Enter first number: ")
second = input("Enter 2nd #: ")
print(first + second)

# לכן אם אנחנו רוצים להפוך את המידע שקלטנו אפשר
# להפוך את סוג המשתנה
first = int(first)
second = int(second)

print(first + second)

"""
בפייתון 2 קיימת פונקציית
raw_input()
שדומה לinput
בפייתון 3 בזה שתיהן מחזירות מחרוזות
אבל קיימת אך ורק בפייתון 2
ויש גם את פונקציית input()
בפייתון 2 אבל בניגוד לפייתון 3
היא מחזירה סוג של מספר ולא מחרוזת!
יש לה גם בעיות בטחוניות אז מומלץ להשתמש רק בraw_input
"""
