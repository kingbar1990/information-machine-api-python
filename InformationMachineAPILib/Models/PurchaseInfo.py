# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.PurchaseInfo
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class PurchaseInfo(object):

    """Implementation of the 'PurchaseInfo' model.

    TODO: type model description here.

    Attributes:
        invoice_id (int): TODO: type description here.
        store_id (int): TODO: type description here.
        store_name (string): TODO: type description here.
        harvested_name (string): TODO: type description here.
        quantity (double): TODO: type description here.
        price (double): TODO: type description here.
        unit_price (double): TODO: type description here.
        purchase_date (string): TODO: type description here.
        recorded_at (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchaseInfo class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    invoice_id -- int -- Sets the attribute invoice_id
                    store_id -- int -- Sets the attribute store_id
                    store_name -- string -- Sets the attribute store_name
                    harvested_name -- string -- Sets the attribute harvested_name
                    quantity -- double -- Sets the attribute quantity
                    price -- double -- Sets the attribute price
                    unit_price -- double -- Sets the attribute unit_price
                    purchase_date -- string -- Sets the attribute purchase_date
                    recorded_at -- string -- Sets the attribute recorded_at
        
        """
        # Set all of the parameters to their default values
        self.invoice_id = None
        self.store_id = None
        self.store_name = None
        self.harvested_name = None
        self.quantity = None
        self.price = None
        self.unit_price = None
        self.purchase_date = None
        self.recorded_at = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "invoice_id": "invoice_id",
            "store_id": "store_id",
            "store_name": "store_name",
            "harvested_name": "harvested_name",
            "quantity": "quantity",
            "price": "price",
            "unit_price": "unit_price",
            "purchase_date": "purchase_date",
            "recorded_at": "recorded_at",
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
            "invoice_id": "invoice_id",
            "store_id": "store_id",
            "store_name": "store_name",
            "harvested_name": "harvested_name",
            "quantity": "quantity",
            "price": "price",
            "unit_price": "unit_price",
            "purchase_date": "purchase_date",
            "recorded_at": "recorded_at",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)