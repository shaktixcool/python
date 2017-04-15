def cTOf(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit
celsius = int(input ("Enter temperature in celsius: "))
if celsius < -273.15:
    print("How is this possible")
else:
    print (cTOf(celsius))
