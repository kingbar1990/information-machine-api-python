# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.NameUpcRecord
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class NameUpcRecord(object):

    """Implementation of the 'NameUpcRecord' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        store (string): TODO: type description here.
        resolve_status (string): TODO: type description here.
        upcs (list of string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the NameUpcRecord class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    name -- string -- Sets the attribute name
                    store -- string -- Sets the attribute store
                    resolve_status -- string -- Sets the attribute resolve_status
                    upcs -- list of string -- Sets the attribute upcs
        
        """
        # Set all of the parameters to their default values
        self.name = None
        self.store = None
        self.resolve_status = None
        self.upcs = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "name": "name",
            "store": "store",
            "resolve_status": "resolve_status",
            "upcs": "upcs",
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
            "name": "name",
            "store": "store",
            "resolve_status": "resolve_status",
            "upcs": "upcs",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)