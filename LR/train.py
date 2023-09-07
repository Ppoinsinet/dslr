from cmath import exp, log, sqrt
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.LogReg import LogisticRegression

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

def getCost(x, y, weight, bias):
    z = weight * x + bias
    hypothesis = 1/(1 + exp(-z).real)
    return -(y * log(hypothesis, 10).real + (1 - y) * log(1 - hypothesis, 10).real)

featureNames = [
    "Astronomy",
    "Herbology",
    "Charms",
    "Defense Against the Dark Arts",
    "Divination",
    "Ancient Runes",
    "Potions"
]

homes = [
    "Ravenclaw",
    "Slytherin",
    "Gryffindor",
    "Hufflepuff"
]

features = []
alpha = 0.000001

[fields, data] = openData()

for it in homes:
    LogisticRegression(it, featureNames, fields, data)

# f = open("./weights.csv", "w")
# for i in features:
#     f.write(i.name + "," + str(i.weight) + "," + str(i.bias) + "\n")

# f.close()
# plt.show()