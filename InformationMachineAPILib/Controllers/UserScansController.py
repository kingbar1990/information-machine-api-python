"""
   InformationMachineAPILib.Controllers.UserScansController

   
"""
import unirest

from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Configuration import Configuration
from InformationMachineAPILib.APIException import APIException
from InformationMachineAPILib.Models.UploadBarcodeWrapper import UploadBarcodeWrapper
from InformationMachineAPILib.Models.UploadReceiptWrapper import UploadReceiptWrapper

class UserScansController(object):

    """A Controller to access Endpoints in the InformationMachineAPILib API."""

    def __init__(self, client_id, client_secret):
        """
        Constructor with authentication and configuration parameters
        """
        self.__clientId = client_id
        self.__clientSecret = client_secret

    def user_scans_upload_barcode(self,
                                  payload,
                                  user_id):
        """Does a POST request to /v1/users/{user_id}/barcode.

        Upload a new product by barcode and associate it to a specified user. 
        Note: Execution might take up to 15 seconds, depending on whether
        barcode exists in database or IM service must gather data around
        uploaded barcode.  POST payload example: { "bar_code" :
        "021130126026", "bar_code_type" : "UPC-A" }

        Args:
            payload (UploadBarcodeRequest): TODO: type description here.
            user_id (string): ID of user in your system

        Returns:
            UploadBarcodeWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/barcode"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "client_id": self.__clientId,
            "client_secret": self.__clientSecret
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

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return UploadBarcodeWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 

    def user_scans_upload_receipt(self,
                                  payload,
                                  user_id):
        """Does a POST request to /v1/users/{user_id}/receipt.

        Upload a receipt with unique ID ("receipt_id") and associate it to a
        specified user using "user_id" parameter. Note: Uploaded receipt image
        should be Base 64 encoded. For testing purposes you can find our Base
        64 encoded logo here:
        http://api.iamdata.co/images/base64/encoded_logo.txt

        Args:
            payload (UploadReceiptRequest): TODO: type description here.
            user_id (string): TODO: type description here.

        Returns:
            UploadReceiptWrapper: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        # The base uri for api requests
        query_builder = Configuration.BASEURI
 
        # Prepare query string for API call
        query_builder += "/v1/users/{user_id}/receipt"

        # Process optional template parameters
        query_builder = APIHelper.append_url_with_template_parameters(query_builder, { 
            "user_id": user_id
        })

        # Process optional query parameters
        query_builder = APIHelper.append_url_with_query_parameters(query_builder, {
            "client_id": self.__clientId,
            "client_secret": self.__clientSecret
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

        elif response.code == 500:
            raise APIException("Internal Server Error", 500, response.body)

        elif response.code < 200 or response.code > 206:  # 200 = HTTP OK
            raise APIException("HTTP Response Not OK", response.code, response.body)
        
        # Try to cast response to desired type
        if isinstance(response.body, dict):
            # Response is already in a dictionary, return the object 
            return UploadReceiptWrapper(**response.body)
        
        # If we got here then an error occured while trying to parse the response
        raise APIException("Invalid JSON returned", response.code, response.body) 