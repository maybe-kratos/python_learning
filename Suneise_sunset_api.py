import requests

MY_LAT = 23.098106
MY_LNG = 72.523869

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
req = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
req.raise_for_status()
data = req.json()
sun_rise = data['results']['sunrise']
sun_set = data['results']['sunset']
print("sunrise :",sun_rise)
print("sunset :",sun_set)