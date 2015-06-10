"""
   InformationMachineAPILib.Models.PurchaseItemProduct
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class PurchaseItemProduct(object):

    """Implementation of the 'PurchaseItemProduct' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (string): TODO: type description here.
        upc (string): TODO: type description here.
        category_id (int): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchaseItemProduct class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- int -- Sets the attribute id
                    name -- string -- Sets the attribute name
                    upc -- string -- Sets the attribute upc
                    category_id -- int -- Sets the attribute category_id
        
        """
        # Set all of the parameters to their default values
        self.id = None
        self.name = None
        self.upc = None
        self.category_id = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "id": "id",
            "name": "name",
            "upc": "upc",
            "category_id": "category_id",
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
            "id": "id",
            "name": "name",
            "upc": "upc",
            "category_id": "category_id",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)