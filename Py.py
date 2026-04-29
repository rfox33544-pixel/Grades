# برنامج حساب التقدير بناءً على درجة الطالب

while True:
    user_input = input("أدخل درجة الطالب أو اكتب 'خروج': ")

    if user_input == "خروج":
        print("تم إنهاء البرنامج")
        break

    try:
        grade = float(user_input)
    except:
        print("إدخال غير صحيح، حاول مرة أخرى")
        continue

    if grade >= 90:
        result = "A"
    elif grade >= 80:
        result = "B"
    elif grade >= 70:
        result = "C"
    elif grade >= 60:
        result = "D"
    else:
        result = "F"

    print("التقدير:", result)
