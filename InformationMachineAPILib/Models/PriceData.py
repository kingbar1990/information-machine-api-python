"""
   InformationMachineAPILib.Models.PriceData
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.PriceInfo import PriceInfo

class PriceData(object):

    """Implementation of the 'PriceData' model.

    TODO: type model description here.

    Attributes:
        prices (list of PriceInfo): TODO: type description here.
        product_id (int): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the PriceData class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    prices -- list of PriceInfo -- Sets the attribute prices
                    product_id -- int -- Sets the attribute product_id
        
        """
        # Set all of the parameters to their default values
        self.prices = None
        self.product_id = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "prices": "prices",
            "product_id": "product_id",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "prices" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.prices = list()
                for item in kwargs["prices"]:
                    self.prices.append(PriceInfo(**item))

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
            "prices": "prices",
            "product_id": "product_id",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)