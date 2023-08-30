'''
1. the getData fixture in conftest is used here in test_third test method
2. in example 2 the gatData is used at class level still it's passed again in method because we are using getData in that method
'''


import pytest

# example1
@pytest.mark.usefixtures('setup')
class TestFixture:

    def test_first(self):
        print("first test")

    def test_second(self):
        print("second test")

    def test_third(self, getData):
        print(getData[0], getData[1])

# example2
@pytest.mark.usefixtures('getData')
class TestGetData:

    def test_get_data(self, getData):
        print(getData[0], getData[1], getData[2])

# example3
class TestGetData2:

    def test_get_data(self, getData):
        print(getData[0], getData[1], getData[2])