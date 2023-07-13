print("""
** WELCOME TO THE TEMPERATURE UNITS CONVERTER **
""")
conversion = input("""
Choose a function:
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celcius
: """)
value = input("Write a Value to convert: ")


if conversion == "1":
    result = ((int(value) * (9/5)) + 32)
    print(f"{value} °C are {result} °F")
elif conversion == "2":
    result = (((int(value) - 32) * (5/9)))
    print(f"{value} °F are {result} °C")
else:
    print("Invalid Function")
