"""
   InformationMachineAPILib.Models.ConnectUserStoreRequest
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class ConnectUserStoreRequest(object):

    """Implementation of the 'ConnectUserStoreRequest' model.

    TODO: type model description here.

    Attributes:
        store_id (int): TODO: type description here.
        username (string): TODO: type description here.
        password (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ConnectUserStoreRequest class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    store_id -- int -- Sets the attribute store_id
                    username -- string -- Sets the attribute username
                    password -- string -- Sets the attribute password
        
        """
        # Set all of the parameters to their default values
        self.store_id = None
        self.username = None
        self.password = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "store_id": "store_id",
            "username": "username",
            "password": "password",
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
            "username": "username",
            "password": "password",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)