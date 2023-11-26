age = int(input("age = "))

if age == 100:
    print("Woah too old man. get better things to do")
elif age >= 18:
    print(age,"is old enough")
elif age < 0:
    print("Not born!")
else:
    print(age,"is not old enough")
