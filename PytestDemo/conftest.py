import pytest


# @pytest.fixture()
@pytest.fixture(scope="class")
def setup():
    print("I will execute first becoz i'm fixture")
    yield
    print("I will execute at last")


@pytest.fixture()
def dataLoad():
    print("use login data")
    return ["Ketan", "123"]
