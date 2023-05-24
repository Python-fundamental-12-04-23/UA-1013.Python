celc_temp = input("Enter the temperature in Celsius ")

if float(celc_temp) >=-273.15:
    faren_temp = round(float(celc_temp)*9/5 +32, 2)
    print(str(celc_temp) + "°C is equivalent to " + str(faren_temp) +"°F")
else:
    print("Error. Temperature below absolute zero (-273.15°C)")