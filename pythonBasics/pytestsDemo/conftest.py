# name of this file should be conftest.py always
# whatever fixture you create here will be available to all files in the folder
# it is used to invoke browser

import pytest

# defining scope=class means that fixture will run once after entering class and once at the end...not everytime
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("i will be executed last")

@pytest.fixture()
def dataLoad():
    print("data is being created")
    return ["Nishita", "Toshi", "rahulshettyacademy.com"]

@pytest.fixture(params=[("chrome","Nishita"),"IE"])
def crossBrowser(request):
    return request.param
#test_Demo1

capabilities = {
        "build": "Sample PY Build",
        "platformName": "Windows 11",
        "browserName": "Chrome",
        "browserVersion": "latest",
}