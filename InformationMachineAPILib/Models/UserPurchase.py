"""
   InformationMachineAPILib.Models.UserPurchase
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.UserStore import UserStore
from InformationMachineAPILib.Models.PurchaseItemData import PurchaseItemData

class UserPurchase(object):

    """Implementation of the 'UserPurchase' model.

    TODO: type model description here.

    Attributes:
        user_store (UserStore): TODO: type description here.
        purchase_items (list of PurchaseItemData): TODO: type description
            here.
        id (int): TODO: type description here.
        date (string): TODO: type description here.
        total (double): TODO: type description here.
        total_without_tax (double): TODO: type description here.
        tax (double): TODO: type description here.
        order_number (string): TODO: type description here.
        receipt_id (string): TODO: type description here.
        receipt_image_url (string): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the UserPurchase class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    user_store -- UserStore -- Sets the attribute user_store
                    purchase_items -- list of PurchaseItemData -- Sets the attribute purchase_items
                    id -- int -- Sets the attribute id
                    date -- string -- Sets the attribute date
                    total -- double -- Sets the attribute total
                    total_without_tax -- double -- Sets the attribute total_without_tax
                    tax -- double -- Sets the attribute tax
                    order_number -- string -- Sets the attribute order_number
                    receipt_id -- string -- Sets the attribute receipt_id
                    receipt_image_url -- string -- Sets the attribute receipt_image_url
        
        """
        # Set all of the parameters to their default values
        self.user_store = None
        self.purchase_items = None
        self.id = None
        self.date = None
        self.total = None
        self.total_without_tax = None
        self.tax = None
        self.order_number = None
        self.receipt_id = None
        self.receipt_image_url = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "user_store": "user_store",
            "purchase_items": "purchase_items",
            "id": "id",
            "date": "date",
            "total": "total",
            "total_without_tax": "total_without_tax",
            "tax": "tax",
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

            # Other objects also need to be initialised properly
            if "user_store" in kwargs:
                self.user_store = UserStore(**kwargs["user_store"])

            # Other objects also need to be initialised properly
            if "purchase_items" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.purchase_items = list()
                for item in kwargs["purchase_items"]:
                    self.purchase_items.append(PurchaseItemData(**item))

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
            "user_store": "user_store",
            "purchase_items": "purchase_items",
            "id": "id",
            "date": "date",
            "total": "total",
            "total_without_tax": "total_without_tax",
            "tax": "tax",
            "order_number": "order_number",
            "receipt_id": "receipt_id",
            "receipt_image_url": "receipt_image_url",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)