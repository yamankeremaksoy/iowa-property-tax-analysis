import matplotlib.pyplot as plt
import pandas as pd

# 1. Analiz Ettiğin Verileri Tanımla
data = {
    "City": [
        "Audubon",
        "Corning",
        "Brayton",
        "Centerville",
        "Lansing",
        "Adair",
        "Cincinnati",
        "Greenfield",
        "Exline",
        "Fontanelle",
        "Bridgewater",
        "Carbon",
        "Harpers Ferry",
    ],
    "Total_Levy_Rate": [
        21.36320,
        19.48752,
        18.87297,
        17.47205,
        17.16459,
        14.69725,
        14.68677,
        12.40006,
        11.72667,
        10.62662,
        10.41856,
        8.32767,
        7.98888,
    ],
}

df = pd.DataFrame(data)

# 2. Grafik Oluştur
plt.figure(figsize=(10, 6))
plt.barh(df["City"], df["Total_Levy_Rate"], color="#2b5c8f")
plt.xlabel("Total Property Tax Levy Rate")
plt.ylabel("City Name")
plt.title("Iowa Cities Total Property Tax Levy Rates (FY 2017)")
plt.gca().invert_yaxis()  # En yüksek oranı en üste getir
plt.tight_layout()

# 3. Grafiği Kaydet
plt.savefig("tax_rates_chart.png", dpi=300)
print("Grafik 'tax_rates_chart.png' adıyla başarıyla oluşturuldu!")