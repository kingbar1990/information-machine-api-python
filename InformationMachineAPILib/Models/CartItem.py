# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.CartItem
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class CartItem(object):

    """Implementation of the 'CartItem' model.

    TODO: type model description here.

    Attributes:
        cart_item_id (string): TODO: type description here.
        upc (string): TODO: type description here.
        quantity (int): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the CartItem class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    cart_item_id -- string -- Sets the attribute cart_item_id
                    upc -- string -- Sets the attribute upc
                    quantity -- int -- Sets the attribute quantity
                    created_at -- string -- Sets the attribute created_at
                    updated_at -- string -- Sets the attribute updated_at
        
        """
        # Set all of the parameters to their default values
        self.cart_item_id = None
        self.upc = None
        self.quantity = None
        self.created_at = None
        self.updated_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "cart_item_id": "cart_item_id",
            "upc": "upc",
            "quantity": "quantity",
            "created_at": "created_at",
            "updated_at": "updated_at",
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
            "cart_item_id": "cart_item_id",
            "upc": "upc",
            "quantity": "quantity",
            "created_at": "created_at",
            "updated_at": "updated_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)