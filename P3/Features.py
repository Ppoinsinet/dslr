class Feature:
    def __init__(self, fields, data, featureName, home) -> None:
        self.count = 0
        self.mean = 0

        self.fields = fields
        self.toDecimal(data)
        self.featureName = featureName
        self.getFeatureIndex()
        self.getInfo(home)

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
    
    def getInfo(self, home):
        self.values = []

        for it in self.data:
            if len(it) < self.index or self.data.count("") > 0:
                continue
            if it[1] == home and it[self.index]:
                self.values.append(it[self.index])
                self.mean = sum(self.values) / len(self.values)


        
    
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