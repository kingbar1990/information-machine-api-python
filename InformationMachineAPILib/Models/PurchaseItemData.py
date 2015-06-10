"""
   InformationMachineAPILib.Models.PurchaseItemData
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.PurchaseItemProduct import PurchaseItemProduct

class PurchaseItemData(object):

    """Implementation of the 'PurchaseItemData' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        purchase_id (int): TODO: type description here.
        name (string): TODO: type description here.
        quantity (double): TODO: type description here.
        price (double): TODO: type description here.
        discounted_price (double): TODO: type description here.
        unit_of_measurement (string): TODO: type description here.
        upc (string): TODO: type description here.
        product (PurchaseItemProduct): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchaseItemData class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- int -- Sets the attribute id
                    purchase_id -- int -- Sets the attribute purchase_id
                    name -- string -- Sets the attribute name
                    quantity -- double -- Sets the attribute quantity
                    price -- double -- Sets the attribute price
                    discounted_price -- double -- Sets the attribute discounted_price
                    unit_of_measurement -- string -- Sets the attribute unit_of_measurement
                    upc -- string -- Sets the attribute upc
                    product -- PurchaseItemProduct -- Sets the attribute product
        
        """
        # Set all of the parameters to their default values
        self.id = None
        self.purchase_id = None
        self.name = None
        self.quantity = None
        self.price = None
        self.discounted_price = None
        self.unit_of_measurement = None
        self.upc = None
        self.product = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "id": "id",
            "purchase_id": "purchase_id",
            "name": "name",
            "quantity": "quantity",
            "price": "price",
            "discounted_price": "discounted_price",
            "unit_of_measurement": "unit_of_measurement",
            "upc": "upc",
            "product": "product",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "product" in kwargs:
                self.product = PurchaseItemProduct(**kwargs["product"])

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
            "purchase_id": "purchase_id",
            "name": "name",
            "quantity": "quantity",
            "price": "price",
            "discounted_price": "discounted_price",
            "unit_of_measurement": "unit_of_measurement",
            "upc": "upc",
            "product": "product",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)