# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.Cart
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.CartItem import CartItem

class Cart(object):

    """Implementation of the 'Cart' model.

    TODO: type model description here.

    Attributes:
        cart_id (string): TODO: type description here.
        cart_name (string): TODO: type description here.
        cart_items (list of CartItem): TODO: type description here.
        created_at (string): TODO: type description here.
        updated_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the Cart class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    cart_id -- string -- Sets the attribute cart_id
                    cart_name -- string -- Sets the attribute cart_name
                    cart_items -- list of CartItem -- Sets the attribute cart_items
                    created_at -- string -- Sets the attribute created_at
                    updated_at -- string -- Sets the attribute updated_at
        
        """
        # Set all of the parameters to their default values
        self.cart_id = None
        self.cart_name = None
        self.cart_items = None
        self.created_at = None
        self.updated_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "cart_id": "cart_id",
            "cart_name": "cart_name",
            "cart_items": "cart_items",
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
            if "cart_items" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.cart_items = list()
                for item in kwargs["cart_items"]:
                    self.cart_items.append(CartItem(**item))

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
            "cart_id": "cart_id",
            "cart_name": "cart_name",
            "cart_items": "cart_items",
            "created_at": "created_at",
            "updated_at": "updated_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)