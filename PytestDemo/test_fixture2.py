import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("method--1")

    def test_fixtureDemo2(self):
        print("method2")