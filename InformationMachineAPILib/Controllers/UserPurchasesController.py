# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Controllers.UserPurchasesController


"""
import requests

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetUserPurchaseHistoryWrapper import GetUserPurchaseHistoryWrapper
from InformationMachineAPILib.Models.GetAllUserPurchasesWrapper import GetAllUserPurchasesWrapper
from InformationMachineAPILib.Models.GetAllUserLoyaltyPurchasesWrapper import GetAllUserLoyaltyPurchasesWrapper
from InformationMachineAPILib.Models.GetSingleUserPurchaseWrapper import GetSingleUserPurchaseWrapper


class UserPurchasesController(object):


    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self,
                 client_id,
                 client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def user_purchases_get_purchase_history_unified(self,
                                                    user_id,
                                                    store_id=None,
                                                    food_only=None,
                                                    upc_only=None,
                                                    show_product_details=None,
                                                    receipts_only=None,
                                                    upc_resolved_after=None):
        """Does a GET request to /v1/users/{user_id}/purchases_product_based.

        Get history of purchases made by a specified user from connected
        stores, must specify "user_id".

        Args:
            user_id (string): TODO: type description here.
            store_id (int, optional): Check Lookup/Stores section for ID of
                all stores. E.g., Amazon = 4, Walmart = 3.
            food_only (bool, optional): default:false [Filter out food
                purchase items.]
            upc_only (bool, optional): default:false [Filter out purchase
                items with UPC.]
            show_product_details (bool, optional): default:false [Show details
                of a purchased products (image, nutrients, ingredients,
                manufacturer, etc..)]
            receipts_only (bool, optional): default:false [Filter out
                purchases transcribed from receipts.]
            upc_resolved_after (string, optional): List only purchases having
                UPC resolved by IM after specified date. Expected format:
                "yyyy-MM-dd"

        Returns:
            GetUserPurchaseHistoryWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/purchases_product_based"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, {
            "user_id": user_id
        })

        # Process optional query parameters
        query_parameters = {
            "store_id": store_id,
            "food_only": food_only,
            "upc_only": upc_only,
            "show_product_details": show_product_details,
            "receipts_only": receipts_only,
            "upc_resolved_after": upc_resolved_after,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetUserPurchaseHistoryWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.status_code, response.json())

    def user_purchases_get_all_user_purchases(self,
                                              user_id,
                                              store_id=None,
                                              page=None,
                                              per_page=None,
                                              purchase_date_from=None,
                                              purchase_date_to=None,
                                              purchase_date_before=None,
                                              purchase_date_after=None,
                                              purchase_total_from=None,
                                              purchase_total_to=None,
                                              purchase_total_less=None,
                                              purchase_total_greater=None,
                                              full_resp=None,
                                              food_only=None,
                                              upc_only=None,
                                              receipts_only=None,
                                              upc_resolved_after=None):
        """Does a GET request to /v1/users/{user_id}/purchases_invoice_based.

        Get history of purchases made by a specified user from connected
        stores, must specify "user_id".

        Args:
            user_id (string): TODO: type description here.
            store_id (int, optional): Check Lookup/Stores section for ID of
                all stores. E.g., Amazon = 4, Walmart = 3.
            page (int, optional): default:1
            per_page (int, optional): default:10, max:50
            purchase_date_from (string, optional): Define multiple date ranges
                by specifying "from" range date components, separated by comma
                ",". Equal number of "from" and "to" parameters is mandatory.
                Expected format: "yyyy-MM-dd, yyyy-MM-dd"e.g., "2015-04-18,
                2015-06-25"
            purchase_date_to (string, optional): Define multiple date ranges
                by specifying "to" range date components, separated by comma
                ",". Equal number of "from" and "to" parameters is mandatory.
                Expected format: "yyyy-MM-dd, yyyy-MM-dd"e.g., "2015-04-28,
                2015-07-05"
            purchase_date_before (string, optional): Filter out purchases made
                before specified date. Expected format: yyyy-MM-dd[e.g.,
                2015-04-18]
            purchase_date_after (string, optional): Filter out purchases made
                after specified date. Expected format: yyyy-MM-dd[e.g.,
                2015-04-18]
            purchase_total_from (string, optional): Define multiple total
                purchase price ranges by specifying "from" range price
                components, separated by comma ",". Equal number of "from" and
                "to" parameters is mandatory. Expected format: "X.YZ,
                X.YZ"e.g., "5.5, 16.5"
            purchase_total_to (string, optional): Define multiple total
                purchase price ranges by specifying "to" range price
                components, separated by comma ",". Equal number of "from" and
                "to" parameters is mandatory. Expected format: "X.YZ,
                X.YZ"e.g., "5.7, 20"
            purchase_total_less (double, optional): Filter out purchases with
                grand total price less than specified amount.
            purchase_total_greater (double, optional): Filter out purchases
                with grand total price greater than specified amount.
            full_resp (bool, optional): default:false [Set true for response
                with purchase item details.]
            food_only (bool, optional): default:false [Filter out food
                purchase items.]
            upc_only (bool, optional): default:false [Filter out purchase
                items with UPC.]
            receipts_only (bool, optional): default:false [Filter out
                purchases transcribed from receipts.]
            upc_resolved_after (string, optional): List only purchases having
                UPC resolved by IM after specified date. Expected format:
                "yyyy-MM-dd"

        Returns:
            GetAllUserPurchasesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/purchases_invoice_based"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, {
            "user_id": user_id
        })

        # Process optional query parameters
        query_parameters = {
            "store_id": store_id,
            "page": page,
            "per_page": per_page,
            "purchase_date_from": purchase_date_from,
            "purchase_date_to": purchase_date_to,
            "purchase_date_before": purchase_date_before,
            "purchase_date_after": purchase_date_after,
            "purchase_total_from": purchase_total_from,
            "purchase_total_to": purchase_total_to,
            "purchase_total_less": purchase_total_less,
            "purchase_total_greater": purchase_total_greater,
            "full_resp": full_resp,
            "food_only": food_only,
            "upc_only": upc_only,
            "receipts_only": receipts_only,
            "upc_resolved_after": upc_resolved_after,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetAllUserPurchasesWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.status_code, response.json())

    def user_purchases_get_all_user_loyalty_purchases(self,
                                                      user_id,
                                                      store_id=None,
                                                      page=None,
                                                      per_page=None,
                                                      food_only=None,
                                                      upc_only=None,
                                                      upc_resolved_after=None,
                                                      record_created_after=None):
        """Does a GET request to /v1/users/{user_id}/loyalty_purchases.

        This endpoint is obsolete. Consider using
        "users/{user_id}/purchase_history/".   Get history of loyalty
        purchases made by a specified user from connected stores, must specify
        "user_id".

        Args:
            user_id (string): TODO: type description here.
            store_id (int, optional): Check Lookup/Stores section for ID of
                all stores. E.g., Amazon = 4, Walmart = 3.
            page (int, optional): default:1
            per_page (int, optional): default:10, max:50
            food_only (bool, optional): default:false [Filter out food
                purchase items.]
            upc_only (bool, optional): default:false [Filter out purchase
                items with UPC.]
            upc_resolved_after (string, optional): List only purchases having
                UPC resolved by IM after specified date. Expected format:
                "yyyy-MM-dd".
            record_created_after (string, optional): List only purchases
                collected, i.e., database inserted by bots, after specified
                date. Not to be confused with purchase date (not existing for
                many loyalty purchases). Expected format: "yyyy-MM-dd"

        Returns:
            GetAllUserLoyaltyPurchasesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/loyalty_purchases"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, {
            "user_id": user_id
        })

        # Process optional query parameters
        query_parameters = {
            "store_id": store_id,
            "page": page,
            "per_page": per_page,
            "food_only": food_only,
            "upc_only": upc_only,
            "upc_resolved_after": upc_resolved_after,
            "record_created_after": record_created_after,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetAllUserLoyaltyPurchasesWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.status_code, response.json())

    def user_purchases_get_single_user_purchase(self,
                                                user_id,
                                                purchase_id,
                                                full_resp=None):
        """Does a GET request to /v1/users/{user_id}/purchases/{purchase_id}.

        Get details about an identified purchase (specify "purchase_id") made
        my a specific user (specify "user_id").

        Args:
            user_id (string): TODO: type description here.
            purchase_id (string): TODO: type description here.
            full_resp (bool, optional): default:false (set true for response
                with purchase item details)

        Returns:
            GetSingleUserPurchaseWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/purchases/{purchase_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, {
            "user_id": user_id,
            "purchase_id": purchase_id
        })

        # Process optional query parameters
        query_parameters = {
            "full_resp": full_resp,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetSingleUserPurchaseWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.status_code, response.json())
