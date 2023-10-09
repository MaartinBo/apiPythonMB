import pytest

from mbtest.src.helpers.orders_helper import OrdersHelper
from mbtest.src.utilities.genericUtilities import generate_random_string
from mbtest.src.utilities.wooAPIUtility import WooAPIUtility

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.parametrize("new_status", [
    pytest.param('cancelled', marks=[pytest.mark.O3, pytest.mark.smoke]),
    pytest.param('completed', marks=pytest.mark.O4),
    pytest.param('on-hold', marks=pytest.mark.O5)
])
def test_update_order_status(new_status):
    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()

    # get new order current status and validate is not already cancelled
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}" \
                                     f"Unable to run test"

    # update the status by using 'update' request
    order_id = order_json['id']
    payload = {"status": new_status}
    rs_update = order_helper.call_update_an_order(order_id, payload)
    # verify the new order status is what was updated in that response
    assert rs_update['status'] == new_status, (f"Updated order status tp {new_status},"
                                               f"but order is still {rs_update['status']}")

    # get order information by 'retrieve' request just for sure, I know it should be the same as before in response
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, (f"Updated order status tp {new_status},"
                                                    f"but order is still {new_order_info['status']}")


@pytest.mark.O6
def test_update_order_status_to_random_string():
    new_status = generate_random_string()

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the status by using 'update' request

    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)
    assert rs_api['code'] == 'rest_invalid_param', f"Update order status to random string didn't have the correct" \
                                                   f" response code. Actual: {rs_api['code']}, but expected:" \
                                                   f" 'rest_invalid_param'"

    assert rs_api[
               'message'] == 'Invalid parameter(s): status', f"Update order status to random string didn't have the correct" \
                                                             f" message. Actual: {rs_api['message']}, but expected:" \
                                                             f" 'Invalid parameter(s): status'"

@pytest.mark.O7
def test_update_order_customer_note():

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # create the payload and send 'update' request
    rand_string = new_status = generate_random_string(25)
    payload = {"customer_note": rand_string}
    rs_update = order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    assert new_order_info['customer_note'] == rand_string, (f"Update order's 'customer_note' field"
                                                            f"failed. Actual: {new_order_info['customer_note']}. "
                                                            f"Expected: {rand_string}")

