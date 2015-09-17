"""
   InformationMachineAPILib.Models.MetaBase
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper

class MetaBase(object):

    """Implementation of the 'MetaBase' model.

    TODO: type model description here.

    Attributes:
        max_number_of_requests_per_day (int): TODO: type description here.
        remaining_number_of_request (int): TODO: type description here.
        time_in_epoch_second_till_reset (double): TODO: type description
            here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the MetaBase class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    max_number_of_requests_per_day -- int -- Sets the attribute max_number_of_requests_per_day
                    remaining_number_of_request -- int -- Sets the attribute remaining_number_of_request
                    time_in_epoch_second_till_reset -- double -- Sets the attribute time_in_epoch_second_till_reset
        
        """
        # Set all of the parameters to their default values
        self.max_number_of_requests_per_day = None
        self.remaining_number_of_request = None
        self.time_in_epoch_second_till_reset = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "max_number_of_requests_per_day": "max_number_of_requests_per_day",
            "remaining_number_of_request": "remaining_number_of_request",
            "time_in_epoch_second_till_reset": "time_in_epoch_second_till_reset",
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
            "max_number_of_requests_per_day": "max_number_of_requests_per_day",
            "remaining_number_of_request": "remaining_number_of_request",
            "time_in_epoch_second_till_reset": "time_in_epoch_second_till_reset",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)