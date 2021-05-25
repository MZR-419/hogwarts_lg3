# 实现被装饰函数又参数的情况
import time

def func1(func):
    def func2(m_time):
        print("开始的时间为",time.strftime("%S"))
        func(m_time)
        print("结束的时间为",time.strftime("%S"))
    return func2

@func1
def be_dacorate(m_time):
    time.sleep(m_time)
    print("被装饰器装饰的函数")

be_dacorate(10)
