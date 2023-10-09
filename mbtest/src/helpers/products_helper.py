import logging as logger

from mbtest.src.utilities.requestsUtility import RequestsUtility


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def get_products_by_id(self, product_id):
        return  self.requests_utility.get(f"products/{product_id}")

    def post_create_product(self, payload):
        return self.requests_utility.post(f"products", payload=payload, expected_status_code=201)

    def get_list_products(self, payload=None):
        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add the current page number to the call
            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload=payload)

            #if there is not response then stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages.")

        return all_products
