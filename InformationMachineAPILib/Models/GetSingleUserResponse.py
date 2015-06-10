"""
   InformationMachineAPILib.Models.GetSingleUserResponse
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class GetSingleUserResponse(object):

    """Implementation of the 'GetSingleUserResponse' model.

    TODO: type model description here.

    Attributes:
        email (string): TODO: type description here.
        zip (string): TODO: type description here.
        user_id (string): TODO: type description here.
        owner_app_id (string): TODO: type description here.
        created_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the GetSingleUserResponse class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    email -- string -- Sets the attribute email
                    zip -- string -- Sets the attribute zip
                    user_id -- string -- Sets the attribute user_id
                    owner_app_id -- string -- Sets the attribute owner_app_id
                    created_at -- string -- Sets the attribute created_at
        
        """
        # Set all of the parameters to their default values
        self.email = None
        self.zip = None
        self.user_id = None
        self.owner_app_id = None
        self.created_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "email": "email",
            "zip": "zip",
            "user_id": "user_id",
            "owner_app_id": "owner_app_id",
            "created_at": "created_at",
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
            "email": "email",
            "zip": "zip",
            "user_id": "user_id",
            "owner_app_id": "owner_app_id",
            "created_at": "created_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)