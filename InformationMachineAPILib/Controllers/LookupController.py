# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Controllers.LookupController


"""
import requests

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetProductAlternativeTypesWrapper\
    import GetProductAlternativeTypesWrapper
from InformationMachineAPILib.Models.GetUOMsWrapper import GetUOMsWrapper
from InformationMachineAPILib.Models.GetCategoriesWrapper\
    import GetCategoriesWrapper
from InformationMachineAPILib.Models.GetNutrientsWrapper\
    import GetNutrientsWrapper
from InformationMachineAPILib.Models.GetStoresWrapper import GetStoresWrapper
from InformationMachineAPILib.Models.GetTagsWrapper import GetTagsWrapper


class LookupController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self,
                 client_id,
                 client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def lookup_get_product_alternative_types(self):
        """Does a GET request to /v1/product_alternative_types.

        Get a list of all possible categories available for alternative
        product recommendations.

        Returns:
            GetProductAlternativeTypesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                status_code, an error message, and the HTTP.json
                that was received in the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/product_alternative_types"

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

        # Error handling using HTTP status_code
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK",
                               response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetProductAlternativeTypesWrapper(**response.json())

        # If we got here then an error occured while trying
        # to parse the response
        raise APIException("Invalid JSON returned",
                           response.status_code, response.json())

    def lookup_get_uo_ms(self):
        """Does a GET request to /v1/units_of_measurement.

        Get a list of the units of measurement that could be associated with a
        product's nutrition facts.

        Returns:
            GetUOMsWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP.json that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/units_of_measurement"

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
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK",
                               response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetUOMsWrapper(**response.json())

        # If we got here then an error occured while trying to
        # parse the response
        raise APIException("Invalid JSON returned",
                           response.status_code, response.json())

    def lookup_get_categories(self):
        """Does a GET request to /v1/categories.

        Get a list of all potential product categories.  Product categories
        follow a hierarchical structure that is defined through the
        "parent_id" field.

        Returns:
            GetCategoriesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                status_code, an error message, and the HTTP.json
                that was received in the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/categories"

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

        # Error handling using HTTP status status_codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK",
                               response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetCategoriesWrapper(**response.json())

        # If we got here then an error occured while
        #  trying to parse the response
        raise APIException("Invalid JSON returned",
                           response.status_code, response.json())

    def lookup_get_nutrients(self):
        """Does a GET request to /v1/nutrients.

        Get a list of all the nutrients that are available on a product's
        nutrition label.

        Returns:
            GetNutrientsWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                status_code, an error message, and the HTTP.json
                that was received in the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/nutrients"

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

        # Error handling using HTTP status status_codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetNutrientsWrapper(**response.json())

        # If we got here then an error occured while
        # trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def lookup_get_stores(self):
        """Does a GET request to /v1/stores.

        Get a list of all stores in the IM API infrastructure. This list is
        constantly expanding. For stores that have "can_scrape" flag set to
        "1", you can use the IM infrastructure to retrieve purchase history.
        To do this, connect the store using the endpoints under the "Users"
        section below.

        Returns:
            GetStoresWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                status_code, an error message, and the HTTP.json that
                was received in the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/stores"

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

        # Error handling using HTTP status status_codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetStoresWrapper(**response.json())

        # If we got here then an error occured while
        # trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())

    def lookup_get_tags(self):
        """Does a GET request to /v1/tags.

        Get a list of all tags available through the IM infrastructure.

        Returns:
            GetTagsWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                status_code, an error message, and the HTTP.json that was
                received in the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI

        # Prepare query string for API call
        query_builder += "/v1/tags"

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

        # Error handling using HTTP status status_codes
        if response.status_code == 404:
            raise APIException("Not Found", 404, response.json())

        elif response.status_code == 401:
            raise APIException("Unauthorized", 401, response.json())

        elif response.status_code < 200 or\
                response.status_code > 206:  # 200 = HTTP OK
            raise APIException(
                "HTTP Response Not OK", response.status_code, response.json())

        # Try to cast response to desired type
        if isinstance(response.json(), dict):
            # Response is already in a dictionary, return the object
            return GetTagsWrapper(**response.json())

        # If we got here then an error occured while
        # trying to parse the response
        raise APIException(
            "Invalid JSON returned", response.status_code, response.json())
