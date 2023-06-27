import tkinter as tk
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450


def get_weather():
    city = entry_field.get()

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        city_label.config(text=f"City: {city}")
        conditions_label.config(text=f"Conditions: {w.detailed_status}")
        temperature_label.config(text=f"Temperature: {round(w.temperature('celsius')['temp'], 2)} °C")
        wind_speed_label.config(text=f"Wind Speed: {w.wind()['speed']} km/h")
        humidity_label.config(text=f"Humidity: {w.humidity}%")

    except:
        city_label.config(text="Oops! Error retrieving weather data.")
        conditions_label.config(text="")
        temperature_label.config(text="")
        wind_speed_label.config(text="")
        humidity_label.config(text="")


root = tk.Tk()
root.title("Weather App")

# Set window size and position
window_width = root.winfo_screenwidth() // 4
window_height = root.winfo_screenheight() // 4
window_x = (root.winfo_screenwidth() // 2) - (window_width // 2)
window_y = (root.winfo_screenheight() // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="light blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry_field = tk.Entry(frame, font=("Courier", 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="white", font=("Courier", 8), command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="gold", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

city_label = tk.Label(lower_frame, font=("Courier", 14))
city_label.pack()

conditions_label = tk.Label(lower_frame, font=("Courier", 12))
conditions_label.pack()

temperature_label = tk.Label(lower_frame, font=("Courier", 12))
temperature_label.pack()

wind_speed_label = tk.Label(lower_frame, font=("Courier", 12))
wind_speed_label.pack()

humidity_label = tk.Label(lower_frame, font=("Courier", 12))
humidity_label.pack()

root.mainloop()
