"""
   InformationMachineAPILib.Controllers.UserPurchasesController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.GetSingleUserPurchaseWrapper import GetSingleUserPurchaseWrapper
from InformationMachineAPILib.Models.GetAllUserPurchasesWrapper import GetAllUserPurchasesWrapper

class UserPurchasesController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self, client_id, client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__client_id = client_id
        self.__client_secret = client_secret

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
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/purchases/{purchase_id}"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id,
            "purchase_id": purchase_id
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
            raise APIException("Not Found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetSingleUserPurchaseWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_purchases_get_all_user_purchases(self,
                                              user_id,
                                              page=None,
                                              per_page=None,
                                              purchase_date_before=None,
                                              purchase_date_after=None,
                                              purchase_total_less=None,
                                              purchase_total_greater=None,
                                              full_resp=None):
        """Does a GET request to /v1/users/{user_id}/purchases.

        Get full history of purchases made by a specified user from connected
        stores, must specify "user_id".

        Args:
            user_id (string): TODO: type description here.
            page (int, optional): TODO: type description here.
            per_page (int, optional): default:10, max:50
            purchase_date_before (string, optional): yyyy-MM-dd [e.g.,
                2015-04-18]
            purchase_date_after (string, optional): yyyy-MM-dd [e.g.,
                2015-04-18]
            purchase_total_less (double, optional): TODO: type description
                here.
            purchase_total_greater (double, optional): TODO: type description
                here.
            full_resp (bool, optional): default:false (set true for response
                with purchase item details)

        Returns:
            GetAllUserPurchasesWrapper: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/purchases"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "page": page,
            "per_page": per_page,
            "purchase_date_before": purchase_date_before,
            "purchase_date_after": purchase_date_after,
            "purchase_total_less": purchase_total_less,
            "purchase_total_greater": purchase_total_greater,
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
            raise APIException("Not Found", 404, response.body)

        elif response.code == 401:
            raise APIException("Unauthorized", 401, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return GetAllUserPurchasesWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 
