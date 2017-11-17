# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Controllers.ProductsController


"""
import requests

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetProductsWrapper import GetProductsWrapper
from InformationMachineAPILib.Models.GetProductWrapper import GetProductWrapper
from InformationMachineAPILib.Models.GetProductPurchasesWrapper import GetProductPurchasesWrapper
from InformationMachineAPILib.Models.GetProductPricesWrapper import GetProductPricesWrapper
from InformationMachineAPILib.Models.GetProductsAlternativesWrapper import GetProductsAlternativesWrapper
from InformationMachineAPILib.Models.GetUserProducts import GetUserProducts
from InformationMachineAPILib.Models.GetUPCsByNameRequestWrapper import GetUPCsByNameRequestWrapper
from InformationMachineAPILib.Models.GetUPCsByNameResponseWrapper import GetUPCsByNameResponseWrapper


class ProductsController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self,
                 client_id,
                 client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def products_search_products(self,
                                 name=None,
                                 product_identifier=None,
                                 page=None,
                                 per_page=None,
                                 request_data=None,
                                 full_resp=None):
        """Does a GET request to /v1/products.

        You can query the IM product database by either product name or
        UPC/EAN/ISBN identifier. Note: If both parameters are specified,
        UPC/EAN/ISBN has higher priority.

        Args:
            name (string, optional): Product name (or part)
            product_identifier (string, optional): UPC/EAN/ISBN
            page (int, optional): TODO: type description here.
            per_page (int, optional): default:10, max:50
            request_data (string, optional): Additional request data sent by
                IM API customer. Expected format:"Key1:Value1;Key2:Value2"
            full_resp (bool, optional): default:false (set true for response
                with nutrients)

        Returns:
            GetProductsWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products"

        # Process optional query parameters
        query_parameters = {
            "name": name,
            "product_identifier": product_identifier,
            "page": page,
            "per_page": per_page,
            "request_data": request_data,
            "full_resp": full_resp,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductsWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_product(self,
                             product_id,
                             full_resp=None):
        """Does a GET request to /v1/products/{product_id}.

        Get details about a single product in the IM database by specifying a
        Information Machine Product ID.

        Args:
            product_id (string): TODO: type description here.
            full_resp (bool, optional): default:false (set true for response
                with nutrients)

        Returns:
            GetProductWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products/{product_id}"

        # Process optional template parameters
        query_builder = APIHelper\
            .append_url_with_template_parameters(query_builder, {
                "product_id": product_id
            })

        # Process optional query parameters
        query_parameters = {
            "full_resp": full_resp,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_product_purchases(self,
                                       product_id,
                                       page=None,
                                       per_page=None):
        """Does a GET request to /v1/products/{product_id}/purchases.

        Get all purchases a user has made for a product by specifying the
        associated product ID.

        Args:
            product_id (string): TODO: type description here.
            page (int, optional): TODO: type description here.
            per_page (int, optional): default:10, max:50

        Returns:
            GetProductPurchasesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products/{product_id}/purchases"

        # Process optional template parameters
        query_builder = APIHelper\
            .append_url_with_template_parameters(query_builder, {
                "product_id": product_id
            })

        # Process optional query parameters
        query_parameters = {
            "page": page,
            "per_page": per_page,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductPurchasesWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_product_prices(self,
                                    product_ids):
        """Does a GET request to /v1/products_prices.

        Get prices (from available stores) for specified product IDs. Note: It
        is possible to query 20 product IDs per each request. Please separate
        IDs with commas (e.g.: "325365, 89300").

        Args:
            product_ids (string): TODO: type description here.

        Returns:
            GetProductPricesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products_prices"

        # Process optional query parameters
        query_parameters = {
            "product_ids": product_ids,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductPricesWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_products_alternatives(self,
                                           product_ids,
                                           type_id=None):
        """Does a GET request to /v1/products_alternatives.

        Get product alternatives for a specified alternative type (e.g.:
        "type_id: 7" will display alternatives of the "general" type) for a
        list of products specified by product IDs. Note: See "Lookup" section,
        "product_alternative_type" for list of all possible alternative types.
        List of product ids must not contain more than 20 ids or else Bad
        Request will be returned.

        Args:
            product_ids (string): TODO: type description here.
            type_id (string, optional): TODO: type description here.

        Returns:
            GetProductsAlternativesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products_alternatives"

        # Process optional query parameters
        query_parameters = {
            "product_ids": product_ids,
            "type_id": type_id,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
        if response.status_code == 400:
            raise APIException("Bad request", 400, response.json())

        elif response.status_code == 404:
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductsAlternativesWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_user_products(self,
                                   user_id,
                                   page=None,
                                   per_page=None,
                                   full_resp=None,
                                   food_only=None):
        """Does a GET request to /v1/users/{user_id}/products.

        Get full history of products purchased by a specified user at
        connected stores, must define "user_id".

        Args:
            user_id (string): TODO: type description here.
            page (int, optional): TODO: type description here.
            per_page (int, optional): default:10, max:50
            full_resp (bool, optional): default:false (set true for response
                with nutrients)
            food_only (bool, optional): default:false (set true to list food
                products only)

        Returns:
            GetUserProducts: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/products"

        # Process optional template parameters
        query_builder = APIHelper\
            .append_url_with_template_parameters(query_builder, {
                "user_id": user_id
            })

        # Process optional query parameters
        query_parameters = {
            "page": page,
            "per_page": per_page,
            "full_resp": full_resp,
            "food_only": food_only,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
            raise APIException("Not found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetUserProducts(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_submit_product_names_for_upc_resolve(self,
                                                      payload,
                                                      webhook_url=None):
        """Does a POST request to /v1/products/upc_resolve_request.

        Request POST model is simple list of strings. Each list item can be
        submitted in two variations: name only OR name+store [use semicolon
        ';' as name and store separator].Use "result" property in response,
        received after successful request submission, to list resolving
        results (endpoint below... GET
        v1/products/upc_resolve_response/{request_id}). Webhook JSON model
        example: { "name":"UB RDY RICE WHL BROWN", "store":"",
        "resolve_status":"Finished", "upcs":"123456789012,123456789012" }

        Args:
            payload (NameResolveRequest): TODO: type description here.
            webhook_url (string, optional): URL we'll use to ping you as soon
                as product name is resolved to UPC. Please find POST body
                above.

        Returns:
            GetUPCsByNameRequestWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products/upc_resolve_request"

        # Process optional query parameters
        query_parameters = {
            "webhook_url": webhook_url,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8"
        }

        # Prepare and invoke the API call request to fetch the response
        response = requests.post(
            query_url, headers=headers,
            params=APIHelper.json_serialize(payload))

        # Error handling using HTTP status codes
        if response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetUPCsByNameRequestWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def products_get_upc_by_product_name_answer(self,
                                                request_id):
        """Does a GET request to /v1/products/upc_resolve_response/{request_id}.

        Use request ID recevied in "v1/products/upc_resolve_request/" [request
        initiate].Response model has four properties: "name" - product name
        submitted for UPC resolve"store" - store submitted (in combination
        with name)"resolve_status" - "Queued" or "Finished""upcs" - list of
        UPCs that correspond to submitted name or name+store request

        Args:
            request_id (string): TODO: type description here.

        Returns:
            GetUPCsByNameResponseWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/products/upc_resolve_response/{request_id}"

        # Process optional template parameters
        query_builder = APIHelper\
            .append_url_with_template_parameters(query_builder, {
                "request_id": request_id
            })

        # Process optional query parameters
        query_parameters = {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        }
        query_builder = APIHelper\
            .append_url_with_query_parameters(query_builder, query_parameters)

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
        if response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetUPCsByNameResponseWrapper(**response.json())

        # If we got here then an error occured while trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())
