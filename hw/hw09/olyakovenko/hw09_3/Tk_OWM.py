import tkinter as tk
from pyowm import OWM


def get_weather(*args):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    owm = OWM(API_KEY)
    try:
        city_to_check = city.get()
        observation = owm.weather_at_place(city_to_check)
        w = observation.get_weather()
        forecast = 'Clouds: ' + str(w.get_clouds()) \
        + '\nWind: ' + str(w.get_wind())\
        +'\nHumidity: ' + str(w.get_humidity())\
        +'\nTemperature: ' + str(w.get_temperature('celsius'))\
        + '\nRain: ' + str(w.get_rain())\
        +'\nClouds: ' + str(w.get_clouds())
        results.set(forecast)
    except ValueError:
        pass

HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

city = tk.StringVar()
results = tk.StringVar()
entry_field = tk.Entry(frame, font=('Courier', 12), textvariable=city)
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)
button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, text='The weather forecast: ', textvariable=results, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.bind('<Return>', get_weather)

root.mainloop()

