import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Używając Matplotlib stwórz obraz, w którym są trzy pionowo ułożone wykresy:
# 1. Wykres liniowy zawierający średnie miesięczne temperatury w 2023 roku w Warszawie
#   i w Londynie. Każdy wykres innym wyróżnij innym kolorem i markerem.
# 2.  Wykres słupkowy zawierający różnicę temperatur (Londyn - Warszawa). Słupki mają być
#   czerwone gdy Londyn jest cieplejszy, a niebieskie gdy jest zimniejszy.
# 3. Wykres punktowy, gdzie oś X to temperatura w Warszawie, a oś Y temperatura
#   w Londynie. Punkty oznaczają kolejne miesiące - zastosuj adnotacje. Użyj dowolnej mapy
#   kolorów. Ustaw ją tak, aby zero różnicy było w środku skali. Obok wykresu narysuj skalę
#   kolorów. Narysuj linię y=x (równość temperatur).
#   Powstały obraz wyświetl i zapisz do pliku.

# start_date = datetime.now().date()
# end_date = start_date + timedelta(days=7)


# url = (
#     f"https://api.open-meteo.com/v1/forecast?"
#     f"latitude={latitude}&longitude={longitude}"
#     f"&daily=sunrise,sunset"
#     f"&hourly=temperature_2m,apparent_temperature,precipitation"
#     f"&start_date={start_date}&end_date={end_date}"
#     f"&timezone=Europe/Warsaw"
# )
# response = requests.get(url)
# data = response.json()
# format = "%Y-%m-%dT%H:%M"

Temperatury={"Warszawa":[2.9,2.9,7.3,11.2,14.2,19.7,20.1,19.2,15.9,11.0,7.2,2.0],"Londyn":[6.0,6.0,8.0,11.0,14.0,17.0,19.0,19.0,16.0,13.0,9.0,7.0]}
tempW = Temperatury["Warszawa"]
tempL = Temperatury["Londyn"]
x = [1,2,3,4,5,6,7,8,9,10,11,12]
fig, (temp1,temp2,temp3) = plt.subplots(3,1,figsize=(6,8), sharex=True)
temp1.plot(x,tempW,label="Warszawa",color="red")
temp1.plot(x,tempL,label="Lonyn",color="green")
temp1.legend()
temp1.set_ylabel('temperatura')
temp1.set_xlabel("miesiace")
roznica = []
for x in range(1,12,1):
    roznica = tempW[x]-tempL[x]
temp2.bar(x,roznica)


for ax in [temp1, temp2,temp3]: #petla dodajaca siatke do obu wykresow
    ax.grid(True) 
plt.show()
