"""
   InformationMachineAPILib.Controllers.ProductsController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetProductsWrapper import GetProductsWrapper
from InformationMachineAPILib.Models.GetProductWrapper import GetProductWrapper
from InformationMachineAPILib.Models.GetProductPurchasesWrapper import GetProductPurchasesWrapper
from InformationMachineAPILib.Models.GetProductPricesWrapper import GetProductPricesWrapper
from InformationMachineAPILib.Models.GetProductsAlternativesWrapper import GetProductsAlternativesWrapper
from InformationMachineAPILib.Models.GetUserProducts import GetUserProducts

class ProductsController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self, client_id, client_secret):
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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/products"

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "name": name,
            "product_identifier": product_identifier,
            "page": page,
            "per_page": per_page,
            "request_data": request_data,
            "full_resp": full_resp,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetProductsWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/products/{product_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "product_id": product_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "full_resp": full_resp,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetProductWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/products/{product_id}/purchases"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "product_id": product_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "page": page,
            "per_page": per_page,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetProductPurchasesWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/products_prices"

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "product_ids": product_ids,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetProductPricesWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/products_alternatives"

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "product_ids": product_ids,
            "type_id": type_id,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("Bad request", 400, response.body)

        elif response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetProductsAlternativesWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/products"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "page": page,
            "per_page": per_page,
            "full_resp": full_resp,
            "food_only": food_only,
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json"
        }


        # Prepare and invoke the API call request to fetch the response
        response = unirest.get(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetUserProducts(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
