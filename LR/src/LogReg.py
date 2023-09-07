from cmath import exp
from .Feature import Feature

class LogisticRegression:

    def __init__(self, name, features, fields, dataset) -> None:
        print("LogisticRegression for ", name)
        self.name = name
        self.features = []
        for feat in features:
            index = fields.index(feat)
            self.features.append(Feature(feat, index))
        self.dataset = [a for a in dataset if a[1] == name]
        self.m = len(self.dataset)

        for row in self.dataset:
            prob = self.getProbability(row)

    def getProbability(self, row):
        v = 0
        for i in self.features:
            v += float(row[i.index]) * i.theta
        try:
            result = 1/(1 - exp(-v))
        except OverflowError:
            result = float('inf')

        return result

    def getCost(self, prob):
        return (1/self.m) * ()