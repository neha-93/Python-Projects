import requests
from twilio.rest import Client

API_KEY = "a32a6f89dc653e4fbf0bf5acfce21007"
MY_LAT = -8.392862
MY_LONG = -74.582619
PHONE_NUMBER = +14159430923
account_sid = "ACa2f8236b50c779872b903a80a18b5dd1"
auth_token = "b441abe4e49d0b75f69917ff4757f84f"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall",
                        params=parameters)
response.raise_for_status()
weather_data = response.json()

rain = False
for x in range(0, 12):
    weather_id = weather_data["hourly"][x]["weather"][0]["id"]
    if int(weather_id) < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today. Bring an umbrella ☂.",
        from_="+14159430923",
        to="+919110032823"
    )

    print(message.status)



