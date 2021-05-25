# 面向对象之回合制游戏
class Game():
    def __init__(self, my_hp, your_hp):
        self.my_hp = my_hp
        self.my_power = 200
        self.your_hp = your_hp
        self.your_power = 199
    def fight(self):
        while True:
            self.my_hp = self.my_hp - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("你输了")
                break

class HouYi(Game):
    # AttributeError: 'HouYi' object has no attribute 'my_hp'
    # 如果重名的话，子类的属性，会覆盖掉父类的属性
    def __init__(self):
        self.defense = 100
        # TypeError: __init__() missing 2 required positional arguments: 'my_hp' and 'your_hp'
        # 继承父类的构造方法， 如果父类的构造方法有形参， 需要传递参数
        super().__init__(1000,1300)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("你输了")
                break

houyi = HouYi()
houyi.fight()