# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.ProductAlternativesRecord
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.ProductData import ProductData

class ProductAlternativesRecord(object):

    """Implementation of the 'ProductAlternativesRecord' model.

    TODO: type model description here.

    Attributes:
        product_id (int): TODO: type description here.
        product_alternatives (list of ProductData): TODO: type description
            here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ProductAlternativesRecord class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    productId -- int -- Sets the attribute product_id
                    productAlternatives -- list of ProductData -- Sets the attribute product_alternatives
        
        """
        # Set all of the parameters to their default values
        self.product_id = None
        self.product_alternatives = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "productId": "product_id",
            "productAlternatives": "product_alternatives",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "productAlternatives" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.product_alternatives = list()
                for item in kwargs["productAlternatives"]:
                    self.product_alternatives.append(ProductData(**item))

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
            "product_id": "productId",
            "product_alternatives": "productAlternatives",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)