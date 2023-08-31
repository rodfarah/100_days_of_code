import requests
from datetime import datetime


def isolate_hour(time: str) -> str:
    t_index = time.index("T")
    return time[t_index+1]+time[t_index+2]


sun_schedule = requests.get("https://api.sunrise-sunset.org/json?lat=-27.6626&lng=-48.4764&formatted=0")
sun_schedule.raise_for_status()
data = sun_schedule.json()["results"]
sunrise = data["sunrise"]
sunset = data["sunset"]

current_time = datetime.now()

print(sunrise)

print(sunset)
print(current_time)


print(isolate_hour(sunrise))