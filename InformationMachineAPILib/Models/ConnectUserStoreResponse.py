"""
   InformationMachineAPILib.Models.ConnectUserStoreResponse
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.UserData import UserData

class ConnectUserStoreResponse(object):

    """Implementation of the 'ConnectUserStoreResponse' model.

    TODO: type model description here.

    Attributes:
        user (UserData): TODO: type description here.
        id (int): TODO: type description here.
        store_name (string): TODO: type description here.
        username (string): TODO: type description here.
        credentials_status (string): TODO: type description here.
        scrape_status (string): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ConnectUserStoreResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    user -- UserData -- Sets the attribute user
                    id -- int -- Sets the attribute id
                    store_name -- string -- Sets the attribute store_name
                    username -- string -- Sets the attribute username
                    credentials_status -- string -- Sets the attribute credentials_status
                    scrape_status -- string -- Sets the attribute scrape_status
                    created_at -- string -- Sets the attribute created_at
                    updated_at -- string -- Sets the attribute updated_at
        
        """
        # Set all of the parameters to their default values
        self.user = None
        self.id = None
        self.store_name = None
        self.username = None
        self.credentials_status = None
        self.scrape_status = None
        self.created_at = None
        self.updated_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "user": "user",
            "id": "id",
            "store_name": "store_name",
            "username": "username",
            "credentials_status": "credentials_status",
            "scrape_status": "scrape_status",
            "created_at": "created_at",
            "updated_at": "updated_at",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "user" in kwargs:
                self.user = UserData(**kwargs["user"])

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
            "user": "user",
            "id": "id",
            "store_name": "store_name",
            "username": "username",
            "credentials_status": "credentials_status",
            "scrape_status": "scrape_status",
            "created_at": "created_at",
            "updated_at": "updated_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)