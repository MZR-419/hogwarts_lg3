import pytest

@pytest.fixture(params=[('tom',123456),('jerry',654321)])
def login(request):
    return request.parm


def test_case1(login):
    print(f"username: {login[0]}, password:{login[1]}")
    print("case1")