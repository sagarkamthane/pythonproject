import pytest

'''Notes'''
'''
1. pytest file should always start/end with test
2. In pytest we have to use test functions to write test
3. test function nsme should start/end with test, same test file can't have multiple files with same name, the 1st test will get overridden by 2nd
4. to run pytest tests through interpreter : click on file neme present at top right>click on edit configuration>click on +> select pytest
5. to run through terminal: go to directory> use command "pytest -v -s" -v: verbose:gives info of tests, -s: to see console logs in terminal
6. we can use py.test or pytest command to run pytest file
7. to run tests from specific test file use: "pytest <test_file_name.py>"
8. If we want to run specific test cases, we have use -k <wordfromtetsname> , ex: pytest -k demo
9. to run a specific test case like smoke, we can add @pytest.mark.smoke above test method name and to run test case use "pytest -m smoke"
10. @pytest.mark.skip skips test case
11. @pytest.mark.xfail decorator is used to mark a test function as expected to fail. This is often used when you anticipate a test to fail due to a known issue, but you still want to run the test and monitor its status.
12. @pytest.mark.xfail test will not be reported a sfailed event if it fails, status would be XFAIL

'''

@pytest.mark.smoke
def test_demo():
    print("Hi")

@pytest.mark.skip
def test_demo2():
    print("Good morining!")

@pytest.mark.xfail
def test_xfail():
    assert 5 == 6
