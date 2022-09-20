import pytest

from pytestsDemo.BaseClass import BaseClass


# paramaterized fixture - used when we want to return a value
# py.test --html=report.html

@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):
    def test_editProfile(self,dataLoad):
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])