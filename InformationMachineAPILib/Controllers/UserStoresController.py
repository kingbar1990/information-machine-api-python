"""
   InformationMachineAPILib.Controllers.UserStoresController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetAllStoresWrapper import GetAllStoresWrapper
from InformationMachineAPILib.Models.ConnectStoreWrapper import ConnectStoreWrapper
from InformationMachineAPILib.Models.GetSingleStoresWrapper import GetSingleStoresWrapper
from InformationMachineAPILib.Models.UpdateStoreConnectionWrapper import UpdateStoreConnectionWrapper
from InformationMachineAPILib.Models.DeleteSingleStoreWrapper import DeleteSingleStoreWrapper

class UserStoresController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self, client_id, client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

    def user_stores_get_all_stores(self,
                                   user_id,
                                   page=None,
                                   per_page=None):
        """Does a GET request to /v1/users/{user_id}/stores.

        Get all store connections for a specified user, must identify user by
        "user_id". Note: Within response focus on the following  properties:
        "scrape_status" and "credentials_status". Possible values for
        "scrape_status": "Not defined""Pending" - (scraping request is in
        queue and waiting to be processed)"Scraping" - (scraping is in
        progress)"Done" - (scraping is finished)"Done With Warning" - (not all
        purchases were scraped)Possible values for "credentials_status":"Not
        defined""Verified" - (scraping bots are able to log in to store
        site)"Invalid" - (supplied user name or password are not
        valid)"Unknown" - (user name or password are not know)"Checking" -
        (credentials verification is in progress)

        Args:
            user_id (string): TODO: type description here.
            page (int, optional): TODO: type description here.
            per_page (int, optional): TODO: type description here.

        Returns:
            GetAllStoresWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/stores"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
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
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetAllStoresWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_stores_connect_store(self,
                                  payload,
                                  user_id):
        """Does a POST request to /v1/users/{user_id}/stores.

        Connect a user's store by specifying the user ID ("user_id"), store ID
        ("store_id") and user's credentials for specified store ("username"
        and "password"). Note: Within response you should focus on the
        following properties: "scrape_status" and "credentials_status".
        Possible values for "scrape_status": "Not defined""Pending" -
        (scraping request is in queue and waiting to be processed)"Scraping" -
        (scraping is in progress)"Done" - (scraping is finished)"Done With
        Warning" - (not all purchases were scraped)Possible values for
        "credentials_status":"Not defined""Verified" - (scraping bots are able
        to log in to store site)"Invalid" - (supplied user name or password
        are not valid)"Unknown" - (user name or password are not
        know)"Checking" - (credentials verification is in progress)

        Args:
            payload (ConnectUserStoreRequest): TODO: type description here.
            user_id (string): TODO: type description here.

        Returns:
            ConnectStoreWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/stores"

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
            raise APIException("Bad request", 400, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return ConnectStoreWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_stores_get_single_store(self,
                                     user_id,
                                     id):
        """Does a GET request to /v1/users/{user_id}/stores/{id}.

        Get single store connection by specifying user ("user_id") and store
        connection ID ("user_store_id" - generated upon successful store
        connection). Note: Within response focus on the following properties:
        "scrape_status" and "credentials_status". Possible values for
        "scrape_status": "Not defined""Pending" - (scraping request is in
        queue and waiting to be processed)"Scraping" - (scraping is in
        progress)"Done" - (scraping is finished)"Done With Warning" - (not all
        purchases were scraped)Possible values for "credentials_status":"Not
        defined""Verified" - (scraping bots are able to log in to store
        site)"Invalid" - (supplied user name or password are not
        valid)"Unknown" - (user name or password are not know)"Checking" -
        (credentials verification is in progress)

        Args:
            user_id (string): TODO: type description here.
            id (int): TODO: type description here.

        Returns:
            GetSingleStoresWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/stores/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
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
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetSingleStoresWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_stores_update_store_connection(self,
                                            payload,
                                            user_id,
                                            id):
        """Does a PUT request to /v1/users/{user_id}/stores/{id}.

        Update username and/or password of existing store connection, for a
        specified user ID ("user_id") and user store ID ("user_store_id"  -
        generated on store connect).

        Args:
            payload (UpdateUserStoreRequest): TODO: type description here.
            user_id (string): TODO: type description here.
            id (int): TODO: type description here.

        Returns:
            UpdateStoreConnectionWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/stores/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
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
            "accept": "application/json",
            "content-type": "application/json; charset=utf-8"
        }


        # Prepare and invoke the API call request to fetch the response
        if payload is not None and hasattr(payload, "resolve_names") and callable(getattr(payload, "resolve_names")):
            payload = payload.resolve_names()

        response = unirest.put(query_url, headers=headers,  params=APIHelper.json_serialize(payload))

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 404:
            raise APIException("Not Found", 404, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return UpdateStoreConnectionWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_stores_delete_single_store(self,
                                        user_id,
                                        id):
        """Does a DELETE request to /v1/users/{user_id}/stores/{id}.

        Delete store connection for a specified user ("user_id") and specified
        store ("user_store_id"  - generated on store connect).

        Args:
            user_id (string): TODO: type description here.
            id (int): TODO: type description here.

        Returns:
            DeleteSingleStoreWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/stores/{id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
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
        response = unirest.delete(query_url, headers=headers)

        # Error handling using HTTP status codes
        if response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return DeleteSingleStoreWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
