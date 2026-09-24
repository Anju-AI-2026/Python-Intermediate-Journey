# 6
subjects = ["Python", "DBMS", "Networking", "Math"]
scores = [82, 76, 91, 68]

for subject, score in zip(subjects, scores):
    if score >= 80:
        print(f"{subject} ➡️  Excellent")
    else:
        print(f"{subject} ➡️  Needs improvement")


# 7
names = ["Anju", "Ravi", "Rossy", "Arjun"]
expected = [85, 70, 90, 80]
actual = [85, 65, 95, 80]

for name, expectedM, actualM in zip(names, expected, actual):
    if expectedM == actualM:
        print(f"{name}  ➡️   Match")
    else:
        print(f"{name}  ➡️   Mismatch")


# 8
products = ["Laptop", "Phone", "Tablet", "Watch"]
prices = [55000, 25000, 30000, 12000]
discounts = [10, 20, 15, 5]

for product, price, discount in zip(products, prices, discounts):
    new_discount = price * discount / 100
    print(f"{product} Discount : {new_discount}")


# 9
names = ["Anju", "Ravi", "Rossy", "Arjun"]
python_marks = [85, 72, 91, 64]
dbms_marks = [78, 88, 95, 70]

for name, p_mark, d_mark in zip(names, python_marks, dbms_marks):
    if p_mark >= 75 and d_mark >= 75:
        print(f"{name} → Good")
    else:
        print(f"{name} → Improve")


# 10
names = ["Anju", "Ravi", "Rossy", "Arjun"]
scores = [85, 45, 72, 91]
results = ["Pass", "Fail", "Pass", "Pass"]

for name, score, result in zip(names, scores, results):
    if score < 50 and result == "Fail":
        print(f"{name} → Correct")
    elif score >= 50 and result == "Pass":
        print(f"{name} → Correct")
    else:
        print(f"{name} → Incorrect")