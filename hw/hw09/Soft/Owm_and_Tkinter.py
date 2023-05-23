from pyowm import OWM
import tkinter as tk

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
HEIGHT = 350
WIDTH = 450


def get_weather():
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    city = entry_field.get()

    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    wind_speed = w.wind()['speed']
    clouds = w.clouds
    return f'Temperature in {city}: {temperature}°C\nWind speed: {wind_speed} m/s\nClouds: {clouds}%'


def screen_text():
    label['text'] = get_weather()


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.75, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="yellow", fg="black",
                   font=('Courier', 10),
                   command=lambda: screen_text())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
