temperature = int(input("whats the temperature: "))

if temperature >= 0 and temperature <= 30:
    print("good to go!")
elif temperature >= 31 and temperature <=39:
    print("don't go out!")
elif not temperature == 25:
    print("wear something warm")