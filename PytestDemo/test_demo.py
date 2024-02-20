import pytest


def test_firstpytestprogram():
    print("Welcome to Pytest")


@pytest.mark.smoke
def test_Name():
    print("Welcome to Ketan h")
