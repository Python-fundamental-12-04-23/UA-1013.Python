import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


def get_weather():
    location = entry_field.get()
    observation = mgr.weather_at_place(location)
    w = observation.weather

    result_text = f"Status: {w.detailed_status}\n"
    result_text += f"Wind: {w.wind()}\n"
    result_text += f"Humidity: {w.humidity}\n"
    result_text += f"Temperature: {w.temperature('celsius')}\n"
    result_text += f"Rain: {w.rain}\n"
    result_text += f"Heat Index: {w.heat_index}\n"
    result_text += f"Clouds: {w.clouds}"

    label.config(text=result_text)


button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
