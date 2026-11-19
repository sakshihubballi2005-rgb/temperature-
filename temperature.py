def convert (celsius):
    return (celsius * 9/5) + 32
    c = float (input("Enter temperature in celsisu"))
    print("Fahrenheit:", convert(c))