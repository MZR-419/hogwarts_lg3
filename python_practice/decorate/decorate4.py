import time


def time_1(time_2): # 最外层管理 装饰器的参数
    def func1(func):# 管理传入函数的对象

        def func2(m_time): # 最内层管壁被装饰的函数的参数
            if time_1:
                print("开始的时间为",time.strftime("%S"))
                func(m_time)
                print("结束的时间为",time.strftime("%S"))
            else:
                func(m_time)
        return func2
    return func1

# @time_1(time_2 = True)
def be_dacorate(m_time):
    time.sleep(m_time)
    print("被装饰器装饰的函数")

# be_dacorate(2)
f1 = time_1(time_2 = True)  # ->返回func1对象
f2 = f1(be_dacorate)  # ->相当于func1() ==返回func2的函数对象
f2(3) # ->相当于