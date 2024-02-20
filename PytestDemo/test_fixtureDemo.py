import pytest


@pytest.fixture()
def setup():
    print("I will execute first becoz i'm fixture")
    #yield
    #print("I will execute at last")

def test_fitureDemo(setup):
    print("I will execute steps in fixture method")
