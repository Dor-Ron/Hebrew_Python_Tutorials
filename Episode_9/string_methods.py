# להגדיל את האות הראשונה של מחרוזות
print("israel".capitalize())  #=> Israel

# להגדיל את כל האותיות במחרוזת
print("israel".upper())  #=>ISRAEL

# להקטין אצ כל האותיות במחרוזת
print("IsRAeL".lower())  #=> israel

# להוציא אותיות מצד שמאל של המחרוזת
print("nothing".lstrip("no"))  #=> thing

# להוציא אותיות מצד ימין של המחרוזת
print("sitting".rstrip("ting"))  #=> sit

# להוציא אותיות משני הצדדים של מחרוזת
print("lol".strip("l"))  #=> o

# להוציא אותיות מכל מקום במחרוזת
print("israwl".replace("w", "e"))  #=> israel

# לבדוק אם מחרוזת מתחילה עם אות מסיומת
print("israel".startswith("i"))  #=> True

# לבדוק אם מחרוזת מסתיימת עם אות מסיומת
print("israel".endswith("q"))  #=> False

# לבדוק את האורך של מחרוזת
print(len("israel"))  #=> 6
