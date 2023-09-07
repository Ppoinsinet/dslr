from cmath import sqrt
from math import ceil


class Feature:
    def __init__(self, fields, data, featureName) -> None:
        self.count = 0
        self.mean = 0
        self.std = 0
        self.max = 0
        self.min = 0
        self.percentiles = [0.0, 0.0, 0.0]

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

        for line in self.data:
            if len(line) <= self.index or line[self.index] == "":
                continue
            self.count += 1
            self.mean += line[self.index]
            values.append(line[self.index])

        values.sort()
        self.mean /= self.count

        for it in values:
            self.std += pow(it - (self.mean/self.count), 2)
        self.std /= self.count
        self.std = sqrt(self.std)
        self.percentiles = [
            values[ceil(0.25 * self.count)],
            values[ceil(0.5 * self.count)],
            values[ceil(0.75 * self.count)]
        ]
        self.min = values[0]
        self.max = values[self.count - 1]
    
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
    "Astronomy",
    "Herbology",
    "Defense Against the Dark Arts",
    "Divination",
    "Muggle Studies",
    "Ancient Runes",
    "History of Magic",
    "Transfiguration",
    "Potions",
    "Care of Magical Creatures",
    "Charms",
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

for row in range(len(first_column)):
    print('{:>5} |'.format(first_column[row]), end="")
    if row == 0:
        for name in names:
            print('{:>30} |'.format(name), end="")
        print()
    else:
        for it in features:
            print('{:>30} |'.format(it.getProperty(row)), end="")
        print()