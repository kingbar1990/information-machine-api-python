"""
   InformationMachineAPILib.Models.UploadBarcodeWrapper
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.UploadBarcodeResponse import UploadBarcodeResponse
from InformationMachineAPILib.Models.MetaBase import MetaBase

class UploadBarcodeWrapper(object):

    """Implementation of the 'UploadBarcodeWrapper' model.

    TODO: type model description here.

    Attributes:
        result (UploadBarcodeResponse): TODO: type description here.
        meta (MetaBase): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the UploadBarcodeWrapper class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    result -- UploadBarcodeResponse -- Sets the attribute result
                    meta -- MetaBase -- Sets the attribute meta
        
        """
        # Set all of the parameters to their default values
        self.result = None
        self.meta = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "result": "result",
            "meta": "meta",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "result" in kwargs:
                self.result = UploadBarcodeResponse(**kwargs["result"])

            # Other objects also need to be initialised properly
            if "meta" in kwargs:
                self.meta = MetaBase(**kwargs["meta"])

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
            "result": "result",
            "meta": "meta",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)