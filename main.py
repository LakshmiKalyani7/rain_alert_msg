import requests
from twilio.rest import Client

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "eae9dc540c97052816d10e28011174af"
account_sid = "ACc108d8b0e75bee537fcc99573e52b8a1"
auth_token = "59a2c47bef6fe395131a1b292099ebcb"

weather_param = {
    "lat": 9.033140,
    "lon": 38.750080,
    "appid": api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_EndPoint, params=weather_param)
#print(response.status_code)
response.raise_for_status()
data = (response.json())
#print(data["hourly"][0]["weather"][0]["id"])
weather_slice = data["hourly"][:12]
#print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Raining, take umbrella.",
        from_='+17603136380',
        to='+918106950520'
    )
    print(message.status)