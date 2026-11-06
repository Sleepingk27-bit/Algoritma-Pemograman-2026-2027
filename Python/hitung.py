celsius = float(input("Suhu (C): "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
reamur = celsius * 4 / 5
status = "Panas" if celsius > 32 else "Normal"
print(f"Fahrenheit: {fahrenheit:.1f}")
print(f"Kelvin: {kelvin:.2f}")
print(f"Reamur: {reamur:.1f}")
print(f"Status: {status}")