while True:
    c_temperature = int(input("Write current temperature in °C: "))
    if c_temperature < -273.15:
        print("Error: Temperature below absolute zero -273.15°C")
        print("-" * 25)
    else:
        f = (c_temperature * 9 / 5) + 32
        print(f"{c_temperature}°С is equal to {f}°F")
        print("-" * 25)
        enter_again = input("Want to continue ? (y/n) ")
        print("-" * 25)
        if enter_again == "y":
            c_temperature = None
        else:
            print("See you later ! :)")
            break




