# מילוי מחרוזות
# למלות מחרוזת צריך להשתמש ב% כדי לסלמל
# לפייתון שאנחנו רוצים למלות את המחרוזת

# %s = מחרוזת
# %d = מספר שלם
# %f = מספר עם נקודה

receipt1 = """
Receipt:
--------

%s: %d
item2: %f
item3: %d

Total: %f
"""

item1 = "kadoor"
item1_price = 9
item2_price = 10
item3_price = 11

total = item1_price + item2_price + item3_price

# שממלים את המחרוזת משתמשים ב% ואח״כ סוגריים עם
# שאר הפרמטרים מופרדים מפסיק
print(receipt1 % (item1,
                  item1_price,
                  item2_price,
                  item3_price,
                  total))

##############################

# בדרך השנייה אנחנו משתמשים בסוגריים מסולסלים
# כדי לציין את מיקופ המילוי העתידי
# בדרך הזרת אין צורך לציין את סוג הנתונים

receipt2 = """
Receipt:
--------

{}: {}
item2: {}
item3: {}

Total: {}
"""

# ממלים את המחרוזות עם הפונקציית מחרוזות format
# בצורה דומה למקודם

print(receipt2.format(item1,
                      item1_price,
                      item2_price,
                      item3_price,
                      total))

################################

# הדרך הזאת עובדת רק בפייתון 3
# שימו לב לאות f
# לפני פתיחת המחרוזת שנרצה למלות
# פשוט משתמשים בסוגריים מסולסלים עם שם המשתנה שכבר
# צריך להיות קיים לפני שאתם יוצרים את החרוזת אותה תרצו למלות
receipt3 = f"""
Receipt:
--------

{item1}: {item1_price}
item2: {item2_price}
item3: {item3_price}

Total: {total}
"""

print(receipt3)
