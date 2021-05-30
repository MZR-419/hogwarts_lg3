import pytest
""
def setup_module():
    print("setup_module:模块级别")
def teardown_module():
    print("teardown_module:模块级别")

class TestA:
    # setup_class teardown_class 类级别的， 在每个类的执行前后 被 调用一次
    def setup_class(self):
        print("setup_class: 类级别")

    def teardown_class(self):
        print("teardown_class: 类级别")

    # setup teardown 是方法级别的，在每个类里面的测试用例前后分别 被 调用一次
    def setup(self):
        print("step: 测试用例前的准备")

    def teardown(self):
        print("teardown: 测试用例后的资源释放")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")

    def test_c(self):
        print("testc")

    def test_d(self):
        print("testd")


class TestB:
    # setup_class teardown_class 类级别的， 在每个类的执行前后 被 调用一次
    def setup_class(self):
        print("setup_class: B类级别")

    def teardown_class(self):
        print("teardown_class: B类级别")
    def setup(self):
        print("step: 测试用例前的准备")

    def teardown(self):
        print("teardown: 测试用例后的资源释放")

    def test_a(self):
        print("testa")

    def test_b(self):
        print("testb")

    def test_c(self):
        print("testc")

    def test_d(self):
        print("testd")