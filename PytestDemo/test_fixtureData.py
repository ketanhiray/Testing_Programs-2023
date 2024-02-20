import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample3:
    def test_loginData(self, dataLoad):
        print(dataLoad)
