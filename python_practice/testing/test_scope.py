import pytest




def test_case1(connDB):
    print("case1")

class TestDemno:
    def test_a(self, connDB):
        print("testa")

    def test_b(self, connDB):
        print("testb")

class TestDemno1:
    def test_c(self, connDB):
        print("testc")

    def test_d(self, connDB):
        print("testd")