# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.InvoiceData
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class InvoiceData(object):

    """Implementation of the 'InvoiceData' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        store_id (int): TODO: type description here.
        store_name (string): TODO: type description here.
        total (double): TODO: type description here.
        total_without_tax (double): TODO: type description here.
        tax (double): TODO: type description here.
        purchase_date (string): TODO: type description here.
        recorded_at (string): TODO: type description here.
        order_number (string): TODO: type description here.
        receipt_id (string): TODO: type description here.
        receipt_image_url (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the InvoiceData class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    id -- int -- Sets the attribute id
                    store_id -- int -- Sets the attribute store_id
                    store_name -- string -- Sets the attribute store_name
                    total -- double -- Sets the attribute total
                    total_without_tax -- double -- Sets the attribute total_without_tax
                    tax -- double -- Sets the attribute tax
                    purchase_date -- string -- Sets the attribute purchase_date
                    recorded_at -- string -- Sets the attribute recorded_at
                    order_number -- string -- Sets the attribute order_number
                    receipt_id -- string -- Sets the attribute receipt_id
                    receipt_image_url -- string -- Sets the attribute receipt_image_url
        
        """
        # Set all of the parameters to their default values
        self.id = None
        self.store_id = None
        self.store_name = None
        self.total = None
        self.total_without_tax = None
        self.tax = None
        self.purchase_date = None
        self.recorded_at = None
        self.order_number = None
        self.receipt_id = None
        self.receipt_image_url = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "id": "id",
            "store_id": "store_id",
            "store_name": "store_name",
            "total": "total",
            "total_without_tax": "total_without_tax",
            "tax": "tax",
            "purchase_date": "purchase_date",
            "recorded_at": "recorded_at",
            "order_number": "order_number",
            "receipt_id": "receipt_id",
            "receipt_image_url": "receipt_image_url",
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
            "store_id": "store_id",
            "store_name": "store_name",
            "total": "total",
            "total_without_tax": "total_without_tax",
            "tax": "tax",
            "purchase_date": "purchase_date",
            "recorded_at": "recorded_at",
            "order_number": "order_number",
            "receipt_id": "receipt_id",
            "receipt_image_url": "receipt_image_url",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)