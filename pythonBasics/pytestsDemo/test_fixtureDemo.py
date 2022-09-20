# FIXTURE- finds fixture connection and runs the fixture first
# fixtures are used as setup and tear down methods for test cases
# yield - whatever is written after this runs after the fixture test case execution
import pytest

# @pytest.fixture()
# def setup():
#     print("I will be executing first")
#     yield
#     print("i will be executed last")


# when you have n num of test cases , you don't have to pass fixture in them individually , use class

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")