from pytest_bdd import scenario, given, when, then

from retirement import retirement_age


@scenario('../feature/retirement.feature', 'calculate full retirement age')
def test_add():
    pass


@given("I was born in 1985")
def retirement():
    return retirement_age(year=1985)


@when("I input my birthday month as 12")
def calc_retirement(retirement):
    retirement.input(12)


@then("I will get my retirement age is 67")
def retirement_year(retirement):
    assert retirement.retirement_age() == 67
