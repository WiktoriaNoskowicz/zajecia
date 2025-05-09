import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import PySide6  # (niewykorzystany w tym kodzie, ale nie przeszkadza)

# Współrzędne lokalizacji (Lublin)
latitude = 51.25
longitude = 22.57

# Zakres dat: od dziś przez 7 dni
start_date = datetime.now().date()
end_date = start_date + timedelta(days=7)

# Budowanie URL do API
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&daily=sunrise,sunset"
    f"&hourly=temperature_2m,apparent_temperature,precipitation"
    f"&start_date={start_date}&end_date={end_date}"
    f"&timezone=Europe/Warsaw"
)

# Pobranie danych pogodowych
response = requests.get(url)
data = response.json()

# Konwersja danych czasowych
format_hourly = "%Y-%m-%dT%H:%M"
x = [datetime.strptime(i, format_hourly) for i in data["hourly"]["time"]]

# Dane pogodowe
temperature_2m = data["hourly"]["temperature_2m"]
apparent_temperature = data["hourly"]["apparent_temperature"]
precipitation = data["hourly"]["precipitation"]

# Przetwarzanie wschodów, zachodów słońca oraz dat
days = []
for i in range(len(data["daily"]["time"])):
    sunrise = datetime.strptime(data["daily"]["sunrise"][i], "%Y-%m-%dT%H:%M")
    sunset = datetime.strptime(data["daily"]["sunset"][i], "%Y-%m-%dT%H:%M")
    day_date = datetime.strptime(data["daily"]["time"][i], "%Y-%m-%d")
    days.append((sunrise, sunset, day_date))

# Tworzenie wykresów
fig, (ax_temp, ax_rain) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, dpi=100)

# Wykres temperatur
ax_temp.plot(x, temperature_2m, label='Temperatura', color='red')
ax_temp.plot(x, apparent_temperature, label='Temperatura odczuwalna', color='green')

# Zaznaczenie pór dnia/nocy
for sunrise, sunset, date in days:
    ax_temp.axvspan(sunrise, sunset, color="yellow", alpha=0.2)  # dzień
    ax_temp.axvspan(date, sunrise, color="black", alpha=0.2)     # noc przed wschodem
    ax_temp.axvspan(sunset, date + timedelta(days=1), color="black", alpha=0.5)  # noc po zachodzie

# Wykres opadów
ax_rain.bar(x, precipitation, label='Opady', color='blue')

# Podpisy, legenda, siatka
ax_temp.legend()
ax_temp.set_ylabel("Temperatura (°C)")
ax_rain.set_ylabel("Opady (mm)")
ax_rain.set_xlabel("Czas")
ax_rain.tick_params(axis='x', rotation=45)

for ax in [ax_temp, ax_rain]:
    ax.grid(True)

# Tytuł główny wykresu
fig.suptitle("Prognoza pogody: temperatura i opady", fontsize=16)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()

# Można też zapisać do pliku:
# plt.savefig("wykres_pogody.png")
