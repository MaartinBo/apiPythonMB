import pytest

from mbtest.src.dao.products_dao import ProductsDAO
from mbtest.src.helpers.products_helper import ProductsHelper
from mbtest.src.utilities.genericUtilities import generate_random_string

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.P1
def test_create_1_simple_products():
    # generate some data
    payload = dict()
    payload['name'] = generate_random_string(20)
    payload['type'] = "simple"
    payload['regular_price'] = "10,99"

    # make the call
    product_rs = ProductsHelper().post_create_product(payload)

    # verify the response
    assert product_rs, f"Create product api response is empty. Payload: {payload}"
    assert product_rs['name'] == payload['name'], f"Create product api post response has" \
        f"unexpected name. Expected {payload['name']}, Actual {product_rs['name']}"

    # verify the product exists in db
    product_id = product_rs['id']
    db_product = ProductsDAO().get_product_by_id(product_id)

    assert payload['name'] == db_product[0]['post_title'], f"Create product, title in db doesn't match"\
        f"title in api, DB: {db_product['post_title']}, API: {payload['name']}"

