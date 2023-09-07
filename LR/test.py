from cmath import exp, log, sqrt
from xml.sax.handler import feature_validation
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from src.Feature import Feature

def getWeights():
    results = []

    f = open("./weights.csv", "r")
    line = f.readline()
    while line:
        print("line : " + line)
        tab = line.split(",")
        if len(tab) == 3:
            tmp = Feature(tab[0])
            tmp.weight = float(tab[1])
            tmp.bias = float(tab[2])
            results.append(tmp)
        line = f.readline()
    f.close()
    return results

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

features = getWeights()

[fields, data] = openData()


for it in data:
    print(it)
    print("fields : ", fields, " et ", it)
    index = fields.index(it)

# z = features[i].weight * x + features[i].bias
# hypothesis = 1/(1 + exp(-z).real)

# iteration(fields, data, homes, features)
f = open("./weights", "w")
for i in features:
    f.write(i.name + "," + str(i.weight) + "," + str(i.bias) + "\n")

f.close()
plt.show()