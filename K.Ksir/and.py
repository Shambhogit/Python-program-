print("Student can take cmputer sscine only if they have taken math in last yeaar and aboove and are above 18")
subject = input("Which was your last subject mt for maths and st for stats ")
age = int (input("Whts your age "))
if subject == "mt" and age >= 18:
    print("You're eligible")
else:
    print("youe're not eligible")
