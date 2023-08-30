'''
1. to use setup fixture at methodf level use test_one(setup)
2. to use setup fixture at class level use below
    @pytest.mark.usefixtuture('setup')
    class TestFixture:
        pass

'''

import pytest

def test_one(setup):
    print("test one")

def test_two(setup):
    print("test two")

@pytest.mark.usefixtures('setup')
class TestFixture:

    def test_first(self):
        print("first test")

    def test_second(self):
        print("second test")

    def test_third(self, getData):
        print(getData[0], getData[1])
