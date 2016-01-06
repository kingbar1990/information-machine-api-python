# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.ConnectOAuthUserStoreRequest
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class ConnectOAuthUserStoreRequest(object):

    """Implementation of the 'ConnectOAuthUserStoreRequest' model.

    TODO: type model description here.

    Attributes:
        store_id (int): TODO: type description here.
        oauth_provider (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ConnectOAuthUserStoreRequest class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    store_id -- int -- Sets the attribute store_id
                    oauth_provider -- string -- Sets the attribute oauth_provider
        
        """
        # Set all of the parameters to their default values
        self.store_id = None
        self.oauth_provider = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "store_id": "store_id",
            "oauth_provider": "oauth_provider",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

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
            "store_id": "store_id",
            "oauth_provider": "oauth_provider",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)