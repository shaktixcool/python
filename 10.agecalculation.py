def ageFunc(age):
    new_age = age + 10
    return new_age

age = float(input("Enter age: "))
if age > 105:
    print("How is this possible")
else:
    print(ageFunc(age))
