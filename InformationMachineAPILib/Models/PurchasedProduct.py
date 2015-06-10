"""
   InformationMachineAPILib.Models.PurchasedProduct
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class PurchasedProduct(object):

    """Implementation of the 'PurchasedProduct' model.

    TODO: type model description here.

    Attributes:
        product_id (int): TODO: type description here.
        date (string): TODO: type description here.
        store (string): TODO: type description here.
        price (double): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchasedProduct class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    product_id -- int -- Sets the attribute product_id
                    date -- string -- Sets the attribute date
                    store -- string -- Sets the attribute store
                    price -- double -- Sets the attribute price
        
        """
        # Set all of the parameters to their default values
        self.product_id = None
        self.date = None
        self.store = None
        self.price = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "product_id": "product_id",
            "date": "date",
            "store": "store",
            "price": "price",
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
            "product_id": "product_id",
            "date": "date",
            "store": "store",
            "price": "price",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)