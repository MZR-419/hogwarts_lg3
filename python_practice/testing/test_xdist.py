from time import sleep

import pytest
@pytest.mark.parametrize('a', [1,2,3,4])
def test_x(a):
    sleep(1)
    print('xxxx')