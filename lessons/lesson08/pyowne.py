from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM("key")
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Lviv,UA')
print(observation.weather)
w = observation.weather
print(w.wind())
print(w.detailed_status    )     # 'clouds'
print(w.wind()  )                # {'speed': 4.6, 'deg': 330}
print(w.humidity  )              # 87
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(w.rain  )                  # {}
print(w.heat_index)              # None
print(w.clouds)                  # 75

# Will it be clear tomorrow at this time in Milan (Italy) ?
# forecast = mgr.forecast_at_place('Milan,IT', 'daily')
# answer = forecast.will_be_clear_at(timestamps.tomorrow())

