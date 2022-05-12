import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
import random
import numpy


# funkcja do wyliczania statystyk dla zmiennych numerycznych
def get_stats(dane):

  stats = {}
  stats['Średnia'] = dane.mean()
  stats['Dominanta'] = dane.mode()
  stats['Odchylenie standardowe'] = dane.std()
  stats['Odchylenie przeciętne'] = dane.mad()
  stats['Pierwszy kwartyl'] = dane.quantile(0.25)
  stats['Mediana'] = dane.median()
  stats['Trzeci kwartyl'] = dane.quantile(0.75)
  stats['Wartość minimalna'] = dane.min()
  stats['Wartość maksymalna'] = dane.max()
  stats['Wariancja'] = dane.var()
  stats['Skośność'] = dane.skew()
  stats['Kurtoza'] = dane.kurt()
  stats['Test skośności'] = st.skewtest(dane)
  stats['Test kurtozy'] = st.kurtosistest(dane)

  return pd.DataFrame.from_dict(stats, orient='index')


# funkcja do wyliczania statystyk dla zmiennych nominalnych
def get_nominal(dane):

    stats = {}
    stats['Ilość różnych odpowiedzi'] = dane.nunique()
    stats['Odpowiedzi'] = dane.unique()
    stats['Częstości'] = dane.value_counts()
    stats['Dominanta'] = dane.mode()

    return pd.DataFrame.from_dict(stats, orient='index')

# wczytanie DataFrame'u
dane = pd.read_csv("dane.csv")


# czyszczenie danych
dane.drop(columns = ["id", "work_type", "smoking_status"])
dane['age'] = dane['age'].astype(int)
dane.dropna(inplace=True)

#
# # analiza wieku
# print("Wiek:")
# stats_age = get_stats(dane['age'])
# print(stats_age)
# # histogram
# plt.hist(dane.age, bins=range(0, 84, 2), edgecolor="White", color="#4169E1")
# plt.xlabel("Wiek [w latach]")
# plt.ylabel("Częstość")
# plt.xlim([-1, 83])
# plt.savefig("Wykres wieku")
# plt.show()
#
# print("")
#
# # analiza poziomu glukozy
# print("Poziom glukozy:")
# stats = get_stats(dane['avg_glucose_level'])
# print(stats)
# # histogram
# plt.hist(dane.avg_glucose_level, bins=range(0, 272, 5),
#          edgecolor="White", color='#4169E1')
# plt.xlabel("Poziom glukozy [mg/dl]")
# plt.ylabel("Częstość")
# plt.savefig("Wykres poziomu glukozy")
# plt.show()
#
# print("")
#
# # analiza bmi
# print("BMI:")
# print(get_stats(dane['bmi']))
# # histogram
# plt.hist(dane.bmi, bins=range(0, 98, 2), edgecolor="White", color="#4169E1")
# plt.xlabel("Współczynnik BMI [kg/m^2]")
# plt.ylabel("Częstość")
# plt.xlim([-1, 98])
# plt.savefig("Wykres bmi")
# plt.show()
#
# print("")
#
# # analiza płci
# print(get_nominal(dane.gender))
# labels = [r'Mężczyzna', r'Kobieta', r'Inne']
# liczenie = dane.groupby('gender')['gender'].count()
# myexplode = [0.1, 0.1, 0.1]
# # wykres kołowy
# plt.pie(liczenie, explode=myexplode, autopct='%1.02f%%',
#           colors=["#00CED1", "#CD5C5C", "#2F4F4F"])
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.savefig("Wykres płci")
# plt.show()
#
# print("")
#
# # analiza zmiennej "stroke"
# print("Udar:")
# print(get_nominal(dane.stroke))
# labels = [r'Nie;', r'Tak', ]
# liczenie = dane.groupby('stroke')['stroke'].count()
# # wykres kołowy
# plt.pie(liczenie, autopct='%1.00f%%', colors = ["#3CB371", "#CD5C5C"])
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.savefig("Wykres udaru")
# plt.show()
#
# print("")
#
# # analiza zmiennej "heart_disease"
# print("Choroby serca:")
# print(get_nominal(dane.heart_disease))
# labels = [r'Nie;', r'Tak', ]
# liczenie = dane.groupby('heart_disease')['heart_disease'].count()
# # wykres kołowy
# plt.pie(liczenie, autopct='%1.00f%%', colors = ["#3CB371", "#CD5C5C"])
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.savefig("Wykres chorób serca")
# plt.show()
#
# print("")
#
# # listy częstości wystąpień danej odpoweidzi
# values_hypertension = []
# values_hypertension.append(dane.stroke.value_counts()[0])
# values_hypertension.append(dane.stroke.value_counts()[1])
#
# values_heart = []
# values_heart.append(dane.heart_disease.value_counts()[0])
# values_heart.append(dane.heart_disease.value_counts()[1])
#
# values_stroke = []
# values_stroke.append(dane.stroke.value_counts()[0])
# values_stroke.append(dane.stroke.value_counts()[1])
#
# # podwójny wykres słupkowy udar x choroby serca
# labels = ["nie", "tak"]
# index = np.arange(len(labels))
# plt.figure(figsize = (7, 4))
# plt.barh(labels, width = values_hypertension, height = 0.5,alpha = 0.6, label='Nadciśnienie', color = "#1E90FF")
# plt.barh(labels, width = values_heart, height = 0.5, alpha = 0.6, label='Choroby serca', color = "#3CB371")
# plt.xlabel('Częstość')
# plt.ylabel('Czy ma Pan/Pani nadciśnienie/chorobę serca?')
# plt.legend()
# plt.savefig("Wykres nadciśnienie x choroby serca")
# plt.show()
#
# print("")
#
# # podwójny wykres słupkowy
# labels = ["nie", "tak"]
# width = 0.25
# index = np.arange(len(labels))
# plt.figure(figsize = (6, 4))
# plt.bar(index - width/2, values_stroke, width, label='Udar', color = "#3CB371")
# plt.bar(index + width/2, values_heart, width, label='Choroby serca', color = "#CD5C5C")
# plt.xticks(index, labels)
# plt.xlabel('Czy miał Pan/Pani kiedykolwiek udar/chorobę serca?')
# plt.ylabel('Częstość')
# plt.legend()
# plt.savefig("Wykres udar x choroby serca")
# plt.show()

print("")

print('Pearson wiek x poziom glukozy:')
print(st.pearsonr(dane.age, dane.avg_glucose_level))

# # wykres rozrzutu wiek x poziom glukozy
# plt.figure(figsize = (7, 3))
# plt.plot(dane['avg_glucose_level'], dane['age'], 'o', markersize= 2.7, alpha = 0.3, color="#6495ED")
# plt.xlabel('Poziom glukozy [mg/dl]')
# plt.ylabel('Wiek [w latach]')
# plt.gca().set_aspect('equal')
# plt.xlim([0,300])
# plt.ylim([-5,85])
# plt.tight_layout()
# plt.savefig('Wykres rozrzutu', dpi = 500)
# plt.show()

print("")

# korelacje pearsona między wszystkimi zmiennymi
print(dane.corr(method = "pearson"))
