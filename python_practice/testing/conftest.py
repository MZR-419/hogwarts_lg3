import pytest

# scope='session' 整个session域只执行一次
@pytest.fixture(scope='session')
def connDB():
    print("连接数据库")
    yield
    print("断开数据库连接")