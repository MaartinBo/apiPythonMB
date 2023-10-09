import pytest

from mbtest.src.dao.products_dao import ProductsDAO
from mbtest.src.helpers.products_helper import ProductsHelper
from mbtest.src.utilities.requestsUtility import RequestsUtility

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.P2
def test_get_all_products():
    # make the call
    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')

    # verify the response is not empty
    assert rs_api, f"Response of list all products is empty"

@pytest.mark.P3
def test_get_product_by_id():

    # get a product from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_product_name = rand_product[0]['post_title']

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_products_by_id(rand_product_id)
    api_product_name = rs_api['name']

    # verify the response
    assert db_product_name == api_product_name, f"Get product by id returned wrong product. Id: {rand_product_id}" \
                                                f"Db name: {db_product_name}, Api_name: {api_product_name}"
