# any pytest file should start with test_
# pytest method names should start with test
# before running edit configurations to pytest
# any code should be wrapped in method only
# every method is treated as one test case
###############################################
# to run this using cmd:-
# navigate to folder location using cd
# then run 'py.test' or 'py.test -v' command......by default console logs/output is not shown
# to see console logs use 'py.test -v -s'
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])