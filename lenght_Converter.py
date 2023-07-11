print()
print("*** Welcome to the Longitudinal Units Converter ***")

conversion_table = {
    "mm": {
        "conv_rate": 0.001,
        "name": "Millimeters"
    },
    "cm": {
        "conv_rate": 0.01,
        "name": "Centimeters"
    },
    "m": {
        "conv_rate": 1.0,
        "name": "Meters"
    },
    "km": {
        "conv_rate": 1000.0,
        "name": "Kilometers"
    },
    "in": {
        "conv_rate": 0.0254,
        "name": "Inches"
    },
    "ft": {
        "conv_rate": 0.3048,
        "name": "Foot"
    },
    "yd": {
        "conv_rate": 0.9144,
        "name": "Yards"
    },
    "mi": {
        "conv_rate": 1609.0,
        "name": "Miles"
    }
}

print()

value = float(input("Provide the value to convert: "))
print()
print('''Possible units are: 
Millimeters (mm), Centimeters (cm), Meters (m) , Kilometers (km)
Inches (in), Foot (ft), Yards (yd), Miles (mi)''')
print()
from_unit = input("Wich unit it is?: ")
result_unit = input("to wich unit do you want to convert it?: ")
value_o = value

if from_unit.lower() == "cm":
    value = value * 0.01
elif from_unit.lower() == "km":
    value = value * 1000
elif from_unit.lower() == "mm":
    value = value * 0.001
elif from_unit.lower() == "mi":
    value = value * 1609
elif from_unit.lower() == "yd":
    value = value * 0.9144
elif from_unit.lower() == "ft":
    value = value * 0.3048
elif from_unit.lower() == "in":
    value = value * 0.0254


result = value / conversion_table[str(result_unit)]["conv_rate"]
from_unit = conversion_table[str(from_unit)]["name"]
result_unit = conversion_table[str(result_unit)]["name"]
print()
print(f"{value_o} {from_unit} are {result} {result_unit}")
print()
print("*** Bye, Bye!!! ***")
print()
