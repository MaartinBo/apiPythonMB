import pytest

from mbtest.src.utilities.requestsUtility import RequestsUtility


@pytest.mark.customers
@pytest.mark.C2
def test_get_all_customer():
    # make the call
    req_helper = RequestsUtility()
    rs_api = req_helper.get('customers')

    #verify the response is not empty
    assert rs_api, f"Response of list all customers is empty"
