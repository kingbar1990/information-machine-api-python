"""
   InformationMachineAPILib.Controllers.UserCartsController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetCartsWrapper import GetCartsWrapper
from InformationMachineAPILib.Models.AddCartWrapper import AddCartWrapper
from InformationMachineAPILib.Models.GetCartWrapper import GetCartWrapper
from InformationMachineAPILib.Models.AddCartItemWrapper import AddCartItemWrapper
from InformationMachineAPILib.Models.DeleteCartWrapper import DeleteCartWrapper
from InformationMachineAPILib.Models.DeleteCartItemWrapper import DeleteCartItemWrapper
from InformationMachineAPILib.Models.ExecuteCartWrapper import ExecuteCartWrapper


class UserCartsController(object):


    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self,
                 client_id,
                 client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def user_carts_get_carts(self,
                             user_id):
        """Does a GET request to /users/{user_id}/carts.

        Get all carts (including items in carts) associated with a specified
        user ID.

        Args:
            user_id (string): ID of a user

        Returns:
            GetCartsWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
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
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetCartsWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_create_cart(self,
                               user_id,
                               payload):
        """Does a POST request to /users/{user_id}/carts.

        IM API will generate Cart ID and return it in the response

        Args:
            user_id (string): ID of a user
            payload (AddCartRequest): TODO: type description here.

        Returns:
            AddCartWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8"
        }

        # Prepare and invoke the API call request to fetch the response
        if payload is not None and hasattr(payload, "resolve_names") and callable(getattr(payload, "resolve_names")):
            payload = payload.resolve_names()

        response = unirest.post(query_url, headers=headers,  params=APIHelper.json_serialize(payload))

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("Bad Request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return AddCartWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_get_cart(self,
                            user_id,
                            cart_id):
        """Does a GET request to /users/{user_id}/carts/{cart_id}.

        Get detailed information on a single user cart by specifying User ID
        and Cart ID. Cart items are included in response.

        Args:
            user_id (string): ID of a user
            cart_id (string): ID of a cart

        Returns:
            GetCartWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts/{cart_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "cart_id": cart_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
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
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetCartWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_add_cart_item(self,
                                 user_id,
                                 cart_id,
                                 payload):
        """Does a POST request to /users/{user_id}/carts/{cart_id}.

        Add item/product to a cart, must specify product UPC and Cart ID.

        Args:
            user_id (string): ID of a user
            cart_id (string): ID of a cart
            payload (AddCartItemRequest): TODO: type description here.

        Returns:
            AddCartItemWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts/{cart_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "cart_id": cart_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "client_id": self.__client_id,
            "client_secret": self.__client_secret
        })

        # Validate and preprocess url
        query_url = APIHelper.clean_url(query_builder)

        # Prepare headers
        headers = {
            "user-agent": "IAMDATA V1",
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8"
        }

        # Prepare and invoke the API call request to fetch the response
        if payload is not None and hasattr(payload, "resolve_names") and callable(getattr(payload, "resolve_names")):
            payload = payload.resolve_names()

        response = unirest.post(query_url, headers=headers,  params=APIHelper.json_serialize(payload))

        # Error handling using HTTP status codes
        if response.code == 400:
            raise APIException("Bad Request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return AddCartItemWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_delete_cart(self,
                               user_id,
                               cart_id):
        """Does a DELETE request to /users/{user_id}/carts/{cart_id}.

        Use specified Cart ID to delete cart and all associated items in
        specified cart.

        Args:
            user_id (string): ID of a user
            cart_id (string): ID of a cart

        Returns:
            DeleteCartWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts/{cart_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "cart_id": cart_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
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
        response = unirest.delete(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return DeleteCartWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_remove_cart_item(self,
                                    user_id,
                                    cart_id,
                                    cart_item_id):
        """Does a DELETE request to /users/{user_id}/carts/{cart_id}/items/{cart_item_id}.

        Remove item/product from a cart, must specify Cart and Cart Item ID.

        Args:
            user_id (string): ID of a user
            cart_id (string): ID of a cart
            cart_item_id (string): ID of a cart item

        Returns:
            DeleteCartItemWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts/{cart_id}/items/{cart_item_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "cart_id": cart_id,
            "cart_item_id": cart_item_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
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
        response = unirest.delete(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return DeleteCartItemWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_carts_execute_cart(self,
                                user_id,
                                cart_id,
                                store_id):
        """Does a GET request to /users/{user_id}/carts/{cart_id}/stores/{store_id}.

        Currently, only Amazon cart is supported.

        Args:
            user_id (string): ID of a user
            cart_id (string): ID of a cart
            store_id (int): ID of a store (check "Lookup" section, "v1/stores"
                endpoint)

        Returns:
            ExecuteCartWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/users/{user_id}/carts/{cart_id}/stores/{store_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "cart_id": cart_id,
            "store_id": store_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
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
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable Entity", 422, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return ExecuteCartWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
