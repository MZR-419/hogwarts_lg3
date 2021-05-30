# class Bicycle():
#     def run(self, km):
#         self.km = km
#         print(f"我骑行了{self.km}")
#
# class EBicycle(Bicycle):
#     def __init__(self, valume):
#         self.valume = valume
#
#     def fill_charge(self, vol):
#         self.vol = vol
#         print(f"充了多少电，目前有多少点{self.valume + self.vol}")
#
#     def run(self, km):
#         power_km = self.valume*10
#         if power_km > km:
#             print(f"我使用了电瓶电量骑行了{km}")
#         else:
#             print(f"我使用了电瓶骑行了{power_km}")
#
#         super().run(km - power_km)
#
#
#
#
# ebike = EBicycle(10)
# ebike.run(300)


class Bicycle():
    def run(self, km):
        self.km = km
        print(f"我骑行了{self.km},很累呀")

class EBicycle(Bicycle):
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.vol = vol
        power_km = self.valume + self.vol
        print(f"目前的电量有{power_km}")

    def run(self, km):
        hp_km = self.valume*10
        if hp_km > km:
            print(f"使用了电量骑行了{km}")
        else:
            print(f"使用了电瓶骑行了{hp_km}")

        super().run(km - hp_km)

bike = EBicycle(10)
bike.run(300)
