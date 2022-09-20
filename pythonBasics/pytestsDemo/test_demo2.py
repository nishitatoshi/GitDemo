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
###############################################
#to run specific file
#py.test test_demo2.py -v -s
###############################################
#to run 1 test case from 1 file and 1 from another
#use -k , whatever term you write after this it will look for that term in test case name and will run that
#py.test -k CreditCard -v -s
###############################################
#Marking test cases like bookmarks
#@pytest.mark.markName
#to run it use -m
#py.test -m smoke -v -s
###############################################
#to skip 1 test case use @pytest.mark.skip
#requirement is to not show failing test case in reports
#so we use skip
##############################################
#if you want to run a test case but not report is
#use @pytest.mark.xfail
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed"

def test_secondCreditCard():
    a =4
    b =6
    assert a+2==6, "addition did not match"


