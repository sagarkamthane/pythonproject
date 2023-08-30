import pytest
'''
1. @pytest.fixture decorator is used to define setup and teardown method
2. pass the setup method name as argument to test methods ex: test_one(setup)
3. by default the scope of @pytest.fixture is module, to change scope to class use @pytest.fixture(scope = "class")
'''

@pytest.fixture(scope = 'class')
def setup():
    print("Ill be printed first")
    yield
    print("I'll be printed last")

@pytest.fixture()
def getData():
    return ['sagar', 'kamthane', '25']

@pytest.fixture(params=[('Chrome', 'Desktop'), ('Chrome', 'Mobile')])
def param_example(request):
    return request.param