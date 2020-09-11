class Handphone:
    TotalCount = 0
    def __init__(self, count, model):
        self.TotalCount += count
        self.dic_phone = {model: count}

    def sell(self):
        print(self.TotalCount)
        print(self.dic_phone)

handphone = Handphone({3, "iphone"}, {4, "Galaxy"})
handphone.sell()