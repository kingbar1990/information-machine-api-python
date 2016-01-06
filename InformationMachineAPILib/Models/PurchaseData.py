# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.PurchaseData
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.PurchasedItem import PurchasedItem
from InformationMachineAPILib.Models.InvoiceData import InvoiceData

class PurchaseData(object):

    """Implementation of the 'PurchaseData' model.

    TODO: type model description here.

    Attributes:
        purchased_items (list of PurchasedItem): TODO: type description here.
        invoices (list of InvoiceData): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchaseData class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    purchased_items -- list of PurchasedItem -- Sets the attribute purchased_items
                    invoices -- list of InvoiceData -- Sets the attribute invoices
        
        """
        # Set all of the parameters to their default values
        self.purchased_items = None
        self.invoices = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "purchased_items": "purchased_items",
            "invoices": "invoices",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "purchased_items" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.purchased_items = list()
                for item in kwargs["purchased_items"]:
                    self.purchased_items.append(PurchasedItem(**item))

            # Other objects also need to be initialised properly
            if "invoices" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.invoices = list()
                for item in kwargs["invoices"]:
                    self.invoices.append(InvoiceData(**item))

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
            "purchased_items": "purchased_items",
            "invoices": "invoices",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)