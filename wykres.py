import requests
import matplotlib.pyplot as plt # dokumentacja = https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
from datetime import datetime, timedelta
import PySide6

latitude = 51.25
longitude = 22.57

start_date = datetime.now().date()
end_date = start_date + timedelta(days=7)


url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&daily=sunrise,sunset"
    f"&hourly=temperature_2m,apparent_temperature,precipitation"
    f"&start_date={start_date}&end_date={end_date}"
    f"&timezone=Europe/Warsaw"
)
response = requests.get(url)
data = response.json()


format = "%Y-%m-%dT%H:%M"
# y = data["hourly"]["temperature_2m"] sama temperatura
#dodawanie na wykres dwóch zmiennych y
precipitation = data['hourly']['precipitation']
temperature_2m = data["hourly"]["temperature_2m"]
apparent_temperature = data["hourly"]["apparent_temperature"]
# print(y)
x = [datetime.strptime(i, format) for i in data["hourly"]["time"]] #tworzy nowa liste przechodzac i w data[hourly][time] i przeksztalca i w datetime
#wykres liniowy
# print(x)
# plt.figure(figsize=(6,4)) #rozmiar wykresu (szerokosc,wysokosc)
# # plt.plot(x,y)
# plt.plot(x,temperature_2m,label="temperatura",color="red")
# plt.plot(x,apparent_temperature,label="temperatura odczuwalna",color="green")
# plt.legend()
# plt.ylabel("temperatura")
# plt.xlabel("czas")
# plt.xticks(rotation = 45)
# plt.title('Wykres')
# plt.grid(True) #linie siatki 

#wyswietlanie przedzialow pomiedzt zmierzchem a switem na szarym tle
days = []
for i in range(len(data["daily"]["time"])): #(wschod,zachod,data)
    days.append((data["daily"]["sunrise"][i],data["daily"]["sunset"][i], data['daily']['time'][i]))

print(days)

fig, (ax_temp, ax_rain) = plt.subplots(2,1,figsize=(6,8), sharex=True) # sharex=True-> oba wykresy dziela jedna osX, plt.subplots(2,1,)-> dwa wykresy sa w dwoch wierszach w jednej kolumnie,dpi do pliku
# fig, (ax_temp, ax_rain) = plt.subplots(2,1,figsize=(6,8), sharex=True,dpi=600) -> po dodaniu dpi sie rozjechal
#fig -> okno z wykresami, (ax_temp, ax_rain) – dwie osie (Axes), czyli dwa osobne wykresy:
ax_temp.plot(x, temperature_2m, label='Temperatura', color='red')
ax_temp.plot(x, apparent_temperature, label='Temperatura odczuwalna')

for day in days:
    ax_temp.axvspan(day[0],day[1],color = "yellow",alpha = 0.2) #zaznacza na zolto dzien(wschod-zachod), alpha=przezroczystosc
    ax_temp.axvspan(day[2],day[0], color='black', alpha = 0.2) #noc
    ax_temp.axvspan(day[1], datetime.strptime(day[2], "%Y-%m-%d")+timedelta(days=1), color='black', alpha = 0.5) #od wieczoru do nastepnego dnia
# axvspan() – rysuje pionowe pasy na wykresie w określonym przedziale X (czasu), na całej wysokości osi Y.


ax_rain.bar(x, precipitation, label='Opady')
ax_rain.set_title("wykres opadow")
ax_temp.legend()
ax_temp.set_ylabel('temperatura')
ax_temp.set_xlabel("czas")

ax_rain.tick_params(axis='x',rotation = 45)
fig.suptitle('Wykrey',fontsize=14)
for ax in [ax_temp, ax_rain]: #petla dodajaca siatke do obu wykresow
    ax.grid(True) 
plt.show()
#jeslii chcemy zapisac do pliku to komentujemy show()
# plt.savefig('plot.png')

# print(data["daily"])
# print(data["hourly"])