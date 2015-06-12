"""
   InformationMachineAPILib.Controllers.UserManagementController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetAllUsersWrapper import GetAllUsersWrapper
from InformationMachineAPILib.Models.CreateUserWrapper import CreateUserWrapper
from InformationMachineAPILib.Models.DeleteUserWrapper import DeleteUserWrapper
from InformationMachineAPILib.Models.GetSingleUserWrapper import GetSingleUserWrapper

class UserManagementController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self, client_id, client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def user_management_get_all_users(self,
                                      page=None,
                                      per_page=None):
        """Does a GET request to /v1/users.

        Get all users associated with your account.

        Args:
            page (int, optional): TODO: type description here.
            per_page (int, optional): default:10, max:50

        Returns:
            GetAllUsersWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users"

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
        if response.code == 400:
            raise APIException("Bad request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetAllUsersWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_management_create_user(self,
                                    payload):
        """Does a POST request to /v1/users.

        Register a new user by specifying "email", "zip" and "user_id". The
        "user_id" is mandatory and it represents the identifier you will use
        to identify your user in the IM API infrastructure.Note: The following
        characters are restricted within "user_id" string ---&gt; { '/', '^',
        '[',  '\\', 'w', '.', ']', '+', '$', '/' }

        Args:
            payload (RegisterUserRequest): TODO: type description here.

        Returns:
            CreateUserWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users"

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
            raise APIException("Bad request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 422:
            raise APIException("Unprocessable entity", 422, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return CreateUserWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_management_delete_user(self,
                                    id):
        """Does a DELETE request to /v1/users.

        Delete a user from the IM API infrastructure by specifying user's
        "id".

        Args:
            id (string): TODO: type description here.

        Returns:
            DeleteUserWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users"

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "id": id,
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
        if response.code == 404:
            raise APIException("Not found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return DeleteUserWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_management_get_single_user(self,
                                        id):
        """Does a GET request to /v1/users/{id}.

        Get user associated with your account specifying "id" of a user.

        Args:
            id (string): TODO: type description here.

        Returns:
            GetSingleUserWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "id": id
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
        if response.code == 400:
            raise APIException("Bad request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetSingleUserWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
