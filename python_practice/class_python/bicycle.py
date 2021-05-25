## 面向对象之开小车
class Bicycle:
    def run(self, km):
        print(f"一共用脚骑了{km}公里,累死了")

# 电动自行车类EBicycle继承自Bicycle
class EBicycle(Bicycle):
    # 如果属性需要传参定义， 那么可以使用构造函数
    def __init__(self, valume):
        self.valume = valume

    def fill_charge(self, vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")
    def run(self ,km):
        power_km = self.valume*10
        # 如果目前电量所能电动骑行的最大里程数大于要骑行的里程数，全程用电瓶就足够了
        if power_km >= km:
            print(f"我使用电瓶电量骑了{km}")
        else:
            print(f"我使用电瓶骑行了{power_km}")
            # 非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)

            # 继承调用
            super().run(km - power_km)



ebike = EBicycle(10)
ebike.run(200)

# bike = Bicycle()
# bike.run(10)