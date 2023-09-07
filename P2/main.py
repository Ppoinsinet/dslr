from cmath import sqrt

import matplotlib.pyplot as plt

class Feature:
    def __init__(self, fields, data, featureName) -> None:
        self.count = 0
        self.mean = 0

        self.fields = fields
        self.toDecimal(data)
        self.featureName = featureName
        self.getFeatureIndex()
        self.getInfo()

    def toDecimal(self, data):
        self.data = []

        for line in data:
            tmp = []
            for val in line:
                if self.is_float(val):
                    tmp.append(float(val))
                else:
                    tmp.append(val)
            self.data.append(tmp)

    def is_float(self, str):
        try:
            f = float(str)
            return True
        except ValueError:
            return False
        
    def getFeatureIndex(self):
        tmp = 0
        for it in self.fields:
            if it.upper() == self.featureName.upper():
                self.index = tmp
            tmp += 1
        if self.index == -1: 
            raise Exception("Could not find feature")
    
    def getInfo(self):
        values = []
        homes = []
        
        self.data = list(filter(lambda x: len(x) >= self.index and self.is_float(x[self.index]), self.data))
        min_value = min(list(map(lambda x: x[self.index], self.data)))

        for line in self.data:
            if len(line) <= self.index or line[self.index] == "":
                continue
            if line[1] not in homes:
                homes.append(line[1])
                values.append((abs(line[self.index]) + abs(min_value)))
            else:
                values[homes.index(line[1])] += (line[self.index] + abs(min_value))
        
        self.values = list(map(lambda x: x / max(values), values))
        self.homes = homes

        avg = sum(self.values) / len(self.values)
        std = sqrt(sum([pow(i - avg, 2) for i in self.values]) / len(self.values)).real
        print("Standard Deviation for " + self.featureName + " == ", std)
    
    def getProperty(self, val):
        if val == 0:
            return ""
        elif val == 1:
            return self.count.real
        elif val == 2:
            return self.mean.real
        elif val == 3:
            return self.std.real
        elif val == 4:
            return self.min.real
        elif val in range(8):
            return self.percentiles[val - 5].real
        elif val == 8:
            return self.max.real


def openData():
    file = open("dataset_train.csv", "r")
    str = file.read()

    lines = str.split("\n")
    first_line = lines.pop(0)
    fields = first_line.split(",")
    result = []
    for line in lines:
        tab = line.split(",")
        result.append(tab)
    return [fields, result]

def getFeatures(fields, data, names):
    result = []
    for it in names:
        if it != "":
            result.append(Feature(fields, data, it))
    return result


[fields, data] = openData()

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

features = getFeatures(fields, data, names)
first_column = [
    "",
    "Count",
    "Mean",
    "Std",
    "Min",
    "25%",
    "50%",
    "75%",
    "Max"
]

colors=[
    "r","g","b","y","p"
]

index = 0
for it in features:

    index_home = 0
    for home in it.homes:
        plt.bar([(index * 5) + (index_home * 0.25)], it.values[index_home], width=0.25, color=colors[index_home])
        index_home += 1

    index += 1

plt.xticks([i * 5 for i in range(len(names))], names)
plt.show()