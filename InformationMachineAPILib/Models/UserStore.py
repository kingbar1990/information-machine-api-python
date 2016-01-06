# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.UserStore
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.UserData import UserData

class UserStore(object):

    """Implementation of the 'UserStore' model.

    TODO: type model description here.

    Attributes:
        user (UserData): TODO: type description here.
        id (int): TODO: type description here.
        supermarket_id (int): TODO: type description here.
        store_name (string): TODO: type description here.
        username (string): TODO: type description here.
        credentials_status (string): TODO: type description here.
        scrape_status (string): TODO: type description here.
        mtype (string): TODO: type description here.
        account_locked (bool): TODO: type description here.
        unlock_url (string): TODO: type description here.
        oauth_provider (string): TODO: type description here.
        oauth_authorization_url (string): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the UserStore class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    user -- UserData -- Sets the attribute user
                    id -- int -- Sets the attribute id
                    supermarket_id -- int -- Sets the attribute supermarket_id
                    store_name -- string -- Sets the attribute store_name
                    username -- string -- Sets the attribute username
                    credentials_status -- string -- Sets the attribute credentials_status
                    scrape_status -- string -- Sets the attribute scrape_status
                    type -- string -- Sets the attribute mtype
                    account_locked -- bool -- Sets the attribute account_locked
                    unlock_url -- string -- Sets the attribute unlock_url
                    oauth_provider -- string -- Sets the attribute oauth_provider
                    oauth_authorization_url -- string -- Sets the attribute oauth_authorization_url
                    created_at -- string -- Sets the attribute created_at
                    updated_at -- string -- Sets the attribute updated_at
        
        """
        # Set all of the parameters to their default values
        self.user = None
        self.id = None
        self.supermarket_id = None
        self.store_name = None
        self.username = None
        self.credentials_status = None
        self.scrape_status = None
        self.mtype = None
        self.account_locked = None
        self.unlock_url = None
        self.oauth_provider = None
        self.oauth_authorization_url = None
        self.created_at = None
        self.updated_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "user": "user",
            "id": "id",
            "supermarket_id": "supermarket_id",
            "store_name": "store_name",
            "username": "username",
            "credentials_status": "credentials_status",
            "scrape_status": "scrape_status",
            "type": "mtype",
            "account_locked": "account_locked",
            "unlock_url": "unlock_url",
            "oauth_provider": "oauth_provider",
            "oauth_authorization_url": "oauth_authorization_url",
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
            "supermarket_id": "supermarket_id",
            "store_name": "store_name",
            "username": "username",
            "credentials_status": "credentials_status",
            "scrape_status": "scrape_status",
            "mtype": "type",
            "account_locked": "account_locked",
            "unlock_url": "unlock_url",
            "oauth_provider": "oauth_provider",
            "oauth_authorization_url": "oauth_authorization_url",
            "created_at": "created_at",
            "updated_at": "updated_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)