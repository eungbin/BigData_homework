# TotalCount = 0
#
# class Handphone:
#     def __init__(self, dict_phone):
#         global TotalCount
#         for i in dict_phone.values():
#             TotalCount += i
#         self.model_count_dict = dict_phone
#
#     def sell(self, phone_model, count):
#         global TotalCount
#         self.model_count_dict[phone_model] -= count
#         TotalCount -= count
#         print("{0} is selled. stock count of {0} : {1}".format(phone_model, self.model_count_dict[phone_model]))
#         print("Total Count : {0}".format(TotalCount))
#
# dict_phone = {"iphone6": 2, "Galaxy": 3, "Optimus": 5}
# handphone = Handphone(dict_phone)
# handphone.sell("iphone6", 1)
# handphone.sell("Galaxy", 1)

#--------------------------------------------------------------------------------------------------------------------

TotalCount = 0

class Handphone:
    def __init__(self, phone_model, phone_count):
        global TotalCount
        for i in phone_count:
            TotalCount += i
        self.model = phone_model
        self.count = {}

        for model, count in zip(phone_model, phone_count):
            self.count[model] = count

    def sell(self, phone_model, phone_count):
        global TotalCount
        self.count[phone_model] -= phone_count
        TotalCount -= phone_count
        print("{0} is selled. stock count of {0} : {1}".format(phone_model, self.count[phone_model]))
        print("Total Count : {0}".format(TotalCount))

phone_model = ['iphone6', 'Galaxy', 'Optimus']
count = [2, 3, 5]
handphone = Handphone(phone_model, count)

handphone.sell("iphone6", 1)
handphone.sell("Galaxy", 1)