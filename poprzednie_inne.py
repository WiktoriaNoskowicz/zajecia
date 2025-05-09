import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Dane: średnie miesięczne temperatury w 2023
Temperatury = {
    "Warszawa": [2.9, 2.9, 7.3, 11.2, 14.2, 19.7, 20.1, 19.2, 15.9, 11.0, 7.2, 2.0],
    "Londyn":   [6.0, 6.0, 8.0, 11.0, 14.0, 17.0, 19.0, 19.0, 16.0, 13.0, 9.0, 7.0]
}

miesiace = list(range(1, 13))
tempW = Temperatury["Warszawa"]
tempL = Temperatury["Londyn"]

fig, (temp1, temp2, temp3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# --- Wykres 1: Liniowy ---
temp1.plot(miesiace, tempW, label="Warszawa", color="red", marker="o")
temp1.plot(miesiace, tempL, label="Londyn", color="green", marker="s")
temp1.legend()
temp1.set_ylabel("Temperatura (°C)")
temp1.set_title("Średnie miesięczne temperatury w 2023 r.")
temp1.grid(True)

# --- Wykres 2: Słupkowy różnica ---
roznice = [l - w for l, w in zip(tempL, tempW)]
kolory = ["red" if r > 0 else "blue" for r in roznice]
temp2.bar(miesiace, roznice, color=kolory)
temp2.set_ylabel("Różnica (Londyn - Warszawa)")
temp2.set_title("Różnica temperatur")
temp2.grid(True)

# --- Wykres 3: Punktowy z kolorem i adnotacjami ---
sc = temp3.scatter(tempW, tempL, c=roznice, cmap="bwr", vmin=-max(abs(r) for r in roznice), vmax=max(abs(r) for r in roznice))
for i in range(12):
    temp3.annotate(str(i+1), (tempW[i], tempL[i]), textcoords="offset points", xytext=(5,5), ha='center')
temp3.plot([min(tempW + tempL), max(tempW + tempL)], [min(tempW + tempL), max(tempW + tempL)], 'k--', label="y = x")
temp3.set_xlabel("Warszawa (°C)")
temp3.set_ylabel("Londyn (°C)")
temp3.set_title("Porównanie temperatur")
plt.colorbar(sc, ax=temp3, label="Londyn - Warszawa")
temp3.grid(True)

plt.tight_layout()
plt.savefig("plik.png")
plt.show()

# # sc = temp3.scatter(
#     tempW,                  # Oś X: temperatura w Warszawie
#     tempL,                  # Oś Y: temperatura w Londynie
#     c=roznice,              # Kolor punktu zależny od różnicy: Londyn - Warszawa (może być + lub -)
#     cmap="bwr",             # Mapa kolorów: Blue-White-Red
#     vmin=-max(abs(r) for r in roznice),  # Skala kolorów: dolna granica
#     vmax= max(abs(r) for r in roznice)   # Skala kolorów: górna granica
# )

