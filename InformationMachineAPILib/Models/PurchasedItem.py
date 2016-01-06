# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.PurchasedItem
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.PurchaseInfo import PurchaseInfo
from InformationMachineAPILib.Models.ProductTimestamps import ProductTimestamps
from InformationMachineAPILib.Models.ProductIdentifiers import ProductIdentifiers
from InformationMachineAPILib.Models.ProductData import ProductData

class PurchasedItem(object):

    """Implementation of the 'PurchasedItem' model.

    TODO: type model description here.

    Attributes:
        product_id (int): TODO: type description here.
        name (string): TODO: type description here.
        purchase_history (list of PurchaseInfo): TODO: type description here.
        product_timestamps (ProductTimestamps): TODO: type description here.
        product_identifiers (ProductIdentifiers): TODO: type description
            here.
        product_details (ProductData): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PurchasedItem class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    product_id -- int -- Sets the attribute product_id
                    name -- string -- Sets the attribute name
                    purchase_history -- list of PurchaseInfo -- Sets the attribute purchase_history
                    product_timestamps -- ProductTimestamps -- Sets the attribute product_timestamps
                    product_identifiers -- ProductIdentifiers -- Sets the attribute product_identifiers
                    product_details -- ProductData -- Sets the attribute product_details
        
        """
        # Set all of the parameters to their default values
        self.product_id = None
        self.name = None
        self.purchase_history = None
        self.product_timestamps = None
        self.product_identifiers = None
        self.product_details = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "product_id": "product_id",
            "name": "name",
            "purchase_history": "purchase_history",
            "product_timestamps": "product_timestamps",
            "product_identifiers": "product_identifiers",
            "product_details": "product_details",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "purchase_history" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.purchase_history = list()
                for item in kwargs["purchase_history"]:
                    self.purchase_history.append(PurchaseInfo(**item))

            # Other objects also need to be initialised properly
            if "product_timestamps" in kwargs:
                self.product_timestamps = ProductTimestamps(**kwargs["product_timestamps"])

            # Other objects also need to be initialised properly
            if "product_identifiers" in kwargs:
                self.product_identifiers = ProductIdentifiers(**kwargs["product_identifiers"])

            # Other objects also need to be initialised properly
            if "product_details" in kwargs:
                self.product_details = ProductData(**kwargs["product_details"])

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
            "name": "name",
            "purchase_history": "purchase_history",
            "product_timestamps": "product_timestamps",
            "product_identifiers": "product_identifiers",
            "product_details": "product_details",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)