from pyowm import OWM
import tkinter as tk
from tkinter import font

API_KEY = '59a0c2393027c6658a551a1dcb0dbff6'
HEIGHT = 350
WIDTH = 450

owm = OWM(API_KEY)

def get_weather():

    mgr = owm.weather_manager()
    place = entry_field.get() 
    observation = mgr.weather_at_place(place)
    w = observation.weather
        
    w.detailed_status         # 'clouds'
    w.wind()                  # {'speed': 4.6, 'deg': 330}
    w.humidity                # 87
    w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain                    # {}
    w.heat_index              # None
    w.clouds                  # 75

    label['text'] = f"City: {place}\nConditions: {w.detailed_status }\nTemperature is {round(w.temperature('celsius')['temp'], 2)} ℃" f"\nWind speed is {w.wind()['speed']} km/h\nHumidity of the air is {w.humidity} %" 
  
    return 
  
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 14))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 10), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()