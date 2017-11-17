from InformationMachineAPILib.Controllers import *
from InformationMachineAPILib.Models import *
import time


class APITestException(Exception):

    def __init__(self,
                 reason):
        Exception.__init__(self, reason)


def wait_for_scrape_to_finish(user_stores_controller,
                              user_identifier, store_id):

    # try to see if the users credentials are valid
    for i in range(0, 120):
        connected_store = user_stores_controller\
            .user_stores_get_single_store(user_identifier, store_id)

        if (connected_store is not None and
            (connected_store.result.scrape_status == "Done" or
             connected_store.result.scrape_status == "DoneWithWarning")):
            return True

        time.sleep(3)
    return False


def check_store_validity(user_stores_controller, user_identifier, store_id):

    # try to see if the users credentials are valid
    for i in range(0, 15):
        connected_store = user_stores_controller\
            .user_stores_get_single_store(user_identifier, store_id)

        if (connected_store is not None and
            (connected_store.result.scrape_status == "Done" or
             connected_store.result.scrape_status == "DoneWithWarning" or
             connected_store.result.scrape_status == "Scraping")):
            if connected_store.result.credentials_status == "Verified":
                return True
            else:
                return False

        time.sleep(3)

    return False


def user_management_controller_test(email,
                                    user_management_controller, user_id):

    register_user_request = RegisterUserRequest()
    register_user_request.email = email
    register_user_request.user_id = user_id
    register_user_request.zip = "21000"

    user = user_management_controller\
        .user_management_create_user(register_user_request)

    if (user.result.email != email or user.result.user_id != user_id):
        raise APITestException("Error: create user")

    all_users = user_management_controller.user_management_get_all_users()

    if (all_users.result.__len__() == 0):
        raise APITestException("Error: get all users")

    user_response = user_management_controller\
        .user_management_get_single_user(user_id)
    if (user_response.result.email != email):
        raise APITestException("Error: get single user")


def test_user_purchase(products_controller, client_id,
                       client_secret, store_id, username, password):

    email = "testuser@iamdata.co"
    user_id = "testuserId1234"

    user_management_controller = UserManagementController(
        client_id, client_secret)
    user_stores_controller = UserStoresController(client_id, client_secret)
    user_purchases_controller = UserPurchasesController(
        client_id, client_secret)
    user_scans_controller = UserScansController(client_id, client_secret)

    user_management_controller_test(email, user_management_controller, user_id)

    encoded_image = None
    with open("encoded_logo.txt", "r") as myfile:
        encoded_image = myfile.read()

    receipt_id = "fe6ba83b-d45c-457a-afd5-35bdb3cdffff"
    receipt_request = UploadReceiptRequest()
    receipt_request.image = encoded_image
    receipt_request.receipt_id = receipt_id

    user_scans_controller.user_scans_upload_receipt(receipt_request, user_id)

    store_connect = ConnectUserStoreRequest()
    store_connect.store_id = store_id
    store_connect.username = username
    store_connect.password = password

    user_store = user_stores_controller\
        .user_stores_connect_store(store_connect, user_id).result

    store_connection_valid = check_store_validity(
        user_stores_controller, user_id, user_store.id)
    if not store_connection_valid:
        user_stores_controller\
            .user_stores_delete_single_store(user_id, user_store.id)
        raise APITestException("Error: could not connect to store")

    if not wait_for_scrape_to_finish(user_stores_controller,
                                     user_id, user_store.id):
        raise APITestException("Error: scrape is not finished")

    stores = user_stores_controller.user_stores_get_all_stores(user_id).result
    if (stores.__len__() == 0 or stores[0].id <= 0):
        raise APITestException("Error: could not get all stores")

    user_products = products_controller\
        .products_get_user_products(user_id, 1, 15, True, True).result
    if (user_products.__len__() == 0):
        raise APITestException("Error: get user products")

    user_purchases = user_purchases_controller\
        .user_purchases_get_all_user_purchases(
            user_id, None, 1, 15, None, None,
            None, None, None, None, None, None, True, None, None, None, None)\
        .result
    if (user_purchases.__len__() == 0):
        raise APITestException("Error: get all user purchases")

    purchase_history = user_purchases_controller\
        .user_purchases_get_purchase_history_unified(
            user_id, None, None, None, None, None, None)
    if purchase_history.__len__() == 0:
        raise APITestException("Error: get purchase history")

    user_purchase = user_purchases_controller\
        .user_purchases_get_single_user_purchase(
            user_id, user_purchases[0].id, True).result
    if user_purchase is None or user_purchase.id != user_purchases[0].id:
        raise APITestException("Error: get single user purchases")

    barcode_request = UploadBarcodeRequest()
    barcode_request.bar_code = "021130126026"
    barcode_request.bar_code_type = "UPC-A"

    barcode_response = user_scans_controller\
        .user_scans_upload_barcode(barcode_request, user_id).result
    if barcode_response.bar_code_type != "UPC-A" or\
            barcode_response.bar_code != "021130126026":
        raise APITestException("Error: upload barcode")

    user_stores_controller\
        .user_stores_delete_single_store(user_id, user_store.id)

    user_management_controller.user_management_delete_user(user_id)


def lookup_controller_test(lookup_controller, store_name):

    categories = lookup_controller.lookup_get_categories().result
    if (categories.__len__() == 0 or categories[0].id != 1):
        raise APITestException("Error: categories")

    nutrients = lookup_controller.lookup_get_nutrients().result
    if (nutrients.__len__() == 0 or nutrients[0].id != 7):
        raise APITestException("Error: nutrients")

    alternatives = lookup_controller\
        .lookup_get_product_alternative_types().result
    if alternatives.__len__() == 0 or alternatives[0].id != 1 or\
            alternatives[0].name != "Reduce Sodium":
        raise APITestException("Error: alternatives")

    tags = lookup_controller.lookup_get_tags().result
    if (tags.__len__() == 0 or tags[0].id != 29 or tags[0].name != "Low Fat"):
        raise APITestException("Error: tags")

    units_of_measurement = lookup_controller.lookup_get_uo_ms().result
    if units_of_measurement.__len__() == 0 or\
            units_of_measurement[0].id != 1 or\
            units_of_measurement[0].name != "g":
        raise APITestException("Error: units of measurements")

    stores = lookup_controller.lookup_get_stores().result
    if stores.__len__() == 0 or stores[0].id != 1 or\
            stores[0].name != "FreshDirect":
        raise APITestException("Error: stores")

    for store in stores:
        if(store.name == store_name):
            return store.id


def products_controller_test(products_controller):

    kale_products = products_controller\
        .products_search_products("Kale", None, 1, 25, None, True).result
    if kale_products.__len__() == 0 or kale_products[0].name is None:
        raise APITestException("Error: get products")

    if kale_products[0].nutrients[0].name == "":
        raise APITestException("Error: get detail product info")

    second_page_kale_products = products_controller\
        .products_search_products("Kale", None, 2, 25, None, True).result
    if second_page_kale_products.__len__() == 0 or\
            second_page_kale_products[0].name is None or\
            second_page_kale_products[0].id == kale_products[0].id:
        raise APITestException("Error: get 2nd page products")

    upc_product = products_controller\
        .products_search_products(None, "014100044208", 1, 25, None, True)\
        .result

    if upc_product.__len__() == 0 or\
        upc_product[0]\
            .name != "Pepperidge Farm Cracker Chips Classic BBQ":
        raise APITestException("Error: get upc products")

    ean_product = products_controller\
        .products_search_products(
            None, "096619872404", None, None, None, True)\
        .result

    if ean_product.__len__() == 0 or\
            ean_product[0]\
            .name != "Beckett Basketball Monthly Houston Rocket English":
        raise APITestException("Error: get ean products")

    product_full = products_controller\
        .products_get_product("103781", True).result
    if product_full is None or\
            product_full.name != "Mammy-Apple, (Mamey), Raw":
        raise APITestException("Error: get full product")

    products_alternatives = products_controller\
        .products_get_products_alternatives("120907, 120902", "7").result
    if products_alternatives.__len__() == 0 or\
            products_alternatives[0]\
            .product_alternatives[0]\
            .name != "Lightlife Smart Deli Veggie Slices Roast Turkey":
        raise APITestException("Error: get full product")

    product_prices = products_controller\
        .products_get_product_prices("149109, 113427").result
    if product_prices.__len__() == 0 or\
            product_prices[0].prices[0].store_id != 4:
        raise APITestException("Error: get full product")


try:
    lines = [line.rstrip('\n') for line in open('clienttest.txt')]
    client_id = lines[0]
    client_secret = lines[1]
    store_name = lines[2]
    username = lines[3]
    password = lines[4]

#    requests.timeout(30)

    store_id = lookup_controller_test(
        LookupController(client_id, client_secret), store_name)
    products_controller = ProductsController(client_id, client_secret)

    products_controller_test(products_controller)

    test_user_purchase(
        products_controller, client_id,
        client_secret, store_id, username, password)

    print ("All tests passed")
except APITestException as ex:
    print ("Unexpected error:", ex)
    raise
except APIException as ex:
    print ("Unexpected error:", ex)
    raise
