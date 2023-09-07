from cmath import sqrt
from xml.sax.handler import feature_validation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Features import Feature


def openData():
    file = open("dataset_train.csv", "r")
    str = file.read()

    lines = str.split("\n")
    first_line = lines.pop(0)
    fields = first_line.split(",")
    result = []
    for line in lines:
        tab = line.split(",")
        if tab.count("") > 0:
            continue
        result.append(tab)
    return [fields, result]

def getFeatures(fields, data, names, home):
    result = []
    for it in names:
        if it != "":
            result.append(Feature(fields, data, it, homes))
    return result


[fields, data] = openData()

homes = []
homes_number = []

for it in data:
    if len(it) >= 2:
        if it[1] not in homes:
            homes.append(it[1])
            homes_number.append(1)
        else:
            homes_number[homes.index(it[1])] += 1

names = [
    "Arithmancy",
    "Transfiguration",
    "Care of Magical Creatures",
    "Astronomy",
    "History of Magic",
    "Herbology",
    "Charms",
    "Defense Against the Dark Arts",
    "Muggle Studies",
    "Divination",
    "Ancient Runes",
    "Potions",
    "Flying"
]

# names = [
#     "Astronomy",
#     "Herbology",
#     "Charms",
#     "Defense Against the Dark Arts",
#     "Divination",
#     "Ancient Runes",
#     "Potions"
# ]

df_list = []

for home in homes:
    obj = {}
    length = 0
    for featureName in names:
        feature = Feature(fields, data, featureName, home)
        obj[featureName[0 : 4]] = feature.values
        length = len(feature.values)
    obj["home"] = [home for i in range(length)]
    df_list.append(pd.DataFrame(obj))

df = pd.concat(df_list)

# sns.set(style="ticks")
g = sns.pairplot(df, diag_kind="kde", hue="home", palette="Set1")

plt.show()