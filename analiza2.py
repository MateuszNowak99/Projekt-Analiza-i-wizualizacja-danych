import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from matplotlib import pyplot
import random
import numpy
import scipy.stats.contingency as st_ct


def get_stats(dane):
  stats = {}
  stats['Średnia'] = np.mean(dane)
  stats['Dominanta'] = statistics.mode(dane)
  stats['Odchylenie standardowe'] = np.std(dane)
  stats['Mediana'] = statistics.median(dane)
  stats['Wariancja'] = dane.var()
  stats['Skośność'] = dane.skew()
  stats['Kurtoza'] = dane.kurt()
  stats['Test skośności'] = st.skewtest(dane)
  stats['Test kurtozy'] = st.kurtosistest(dane)

  return pd.DataFrame.from_dict(stats, orient='index')


# wczytanie DataFrame'u
dane = pd.read_csv("dane.csv")

# czyszczenie danych
dane.drop(columns=["id", "work_type", "smoking_status"])
dane['age'] = dane['age'].astype(int)
dane.dropna(inplace=True)
#
# stats = get_stats(dane['age'])
# print(stats)
# plt.hist(dane.age, bins=range(0, 84, 2), edgecolor="White", color='#3366cc')
# plt.xlabel("Wiek")
# plt.ylabel("Częstotliwość")
# plt.xlim([-1, 83])
# # plt.savefig()
# plt.show()
#
# print(dane.stroke.value_counts())
# labels = [r'Nie;', r'Tak', ]
# liczenie = dane.groupby('stroke')['stroke'].count()
# plt.pie(liczenie, autopct='%1.2f%%')
# plt.title('Udar')
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.show()
#
# print(dane.heart_disease.value_counts())
# labels = [r'Nie;', r'Tak', ]
# liczenie = dane.groupby('heart_disease')['heart_disease'].count()
# plt.pie(liczenie, autopct='%1.2f%%')
# plt.title('Choroby serca')
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.show()
#
#
# stats = get_stats(dane['stroke'])
# print(stats)
# pyplot.hist(dane.stroke, alpha=0.5, label='Udar')
# pyplot.hist(dane.hypertension, alpha=0.5, label='Nadciśnienie')
# pyplot.legend(loc='upper right')
# pyplot.show()
#
# print('statystyka problemow z sercem')
# stats = get_stats(dane['heart_disease'])
# print(stats)
# pyplot.hist(dane.heart_disease, alpha=0.5, label='Problemy z sercem')
# pyplot.hist(dane.hypertension, alpha=0.5, label='Nadciśnienie')
# pyplot.legend(loc='upper right')
# pyplot.show()
#
# stats = get_stats(dane['avg_glucose_level'])
# print(stats)
# plt.hist(dane.avg_glucose_level, bins=range(0, 272, 10),
#          edgecolor="White", color='#3366cc')
# plt.xlabel("Glukoza")
# plt.ylabel("Częstotliwość")
# plt.show()
#
#
# print(dane.gender.describe())
# dominant_work_type = dane.gender.value_counts().index[0]
# print(dane.gender.value_counts())
# labels = [r'Mężczyzna', r'Kobieta',
#           r'Inne']
# liczenie = dane.groupby('gender')['gender'].count()
# plt.pie(liczenie, autopct='%1.2f%%')
# plt.title('Plec')
# plt.legend(labels)
# plt.gca().set_aspect('equal')
# plt.show()
#
#
# stats = get_stats(dane['bmi'])
# # histogram
# plt.hist(dane.bmi, bins=range(0, 98, 2), edgecolor="White", color='#3366cc')
# plt.xlabel("Współczynnik BMI")
# plt.ylabel("Częstość")
# plt.xlim([-1, 98])
# # plt.savefig("Wykres bmi")
# plt.show()
#
#
# print('pearson')
# print(st.pearsonr(dane.age, dane.avg_glucose_level))
#
# pd.crosstab(dane.avg_glucose_level, dane['gender'])  # tabela krzyżowa
# st_ct.association(pd.crosstab(dane.avg_glucose_level,
#                   dane['gender']), method='cramer', correction=True)
#
# stats = get_stats(dane['stroke'])
# print(stats)
# plt.bar(dane.stroke, height=dane.stroke.value_counts(), color='#3366cc')
# plt.xlabel("Glukoza")
# plt.ylabel("Częstotliwość")
# plt.show()
#
# # rozkład zmiennych względem siebie (wykres rozrzutu)
# plt.figure(figsize=(5, 5))
# plt.plot(dane['avg_glucose_level'], dane['age'],
#          'o', markersize=2.7, alpha=0.3)
# plt.plot([0, 100], [0, 100], color='k', linewidth=0.5, alpha=0.2)
# plt.xlabel('Średni poziom glukozy')
# plt.ylabel('Wiek')
# plt.gca().set_aspect('equal')
# plt.xlim([50, 300])
# plt.ylim([-5, 85])
# plt.tight_layout()
# # plt.savefig('', dpi = 500)
# plt.show()
# print(dane.stroke.value_counts())
#
# values = []
# values.append(dane.stroke.value_counts()[0])
# values.append(dane.stroke.value_counts()[1])
# values_2 = []
# values_2.append(dane.heart_disease.value_counts()[0])
# values_2.append(dane.heart_disease.value_counts()[1])
# plt.bar(['nie', 'tak'], values)
# plt.bar(['nie', 'tak'], values_2)
# plt.xlabel('Czy miał Pan/Pani kiedykolwiek udar?')
# plt.ylabel('Częstość')
# plt.show()


plt.scatter(dane.gender, dane.stroke.value_counts())
plt.show()


print(dane.corr(method="pearson"))
