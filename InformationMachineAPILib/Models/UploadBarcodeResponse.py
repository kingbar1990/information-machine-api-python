# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.UploadBarcodeResponse
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.ProductData import ProductData

class UploadBarcodeResponse(object):

    """Implementation of the 'UploadBarcodeResponse' model.

    TODO: type model description here.

    Attributes:
        bar_code (string): TODO: type description here.
        bar_code_type (string): TODO: type description here.
        api_product (ProductData): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the UploadBarcodeResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    bar_code -- string -- Sets the attribute bar_code
                    bar_code_type -- string -- Sets the attribute bar_code_type
                    apiProduct -- ProductData -- Sets the attribute api_product
        
        """
        # Set all of the parameters to their default values
        self.bar_code = None
        self.bar_code_type = None
        self.api_product = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "bar_code": "bar_code",
            "bar_code_type": "bar_code_type",
            "apiProduct": "api_product",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "apiProduct" in kwargs:
                self.api_product = ProductData(**kwargs["apiProduct"])

    def resolve_names(self):
        """Creates a dictionary representation of this object.
        
        This method converts an object to a dictionary that represents the
        format that the model should be in when passed into an API Request.
        Because of this, the generated dictionary may have different
        property names to that of the model itself.
        
        Returns:
            dict: The dictionary representing the object.
        
        """
        # Create a mapping from Model property names to API property names
        replace_names = {
            "bar_code": "bar_code",
            "bar_code_type": "bar_code_type",
            "api_product": "apiProduct",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)