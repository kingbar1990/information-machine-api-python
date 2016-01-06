# -*- coding: utf-8 -*-

"""
   InformationMachineAPILib.Models.ProductData
 
   
"""
from InformationMachineAPILib.APIHelper import APIHelper
from InformationMachineAPILib.Models.NutrientData import NutrientData

class ProductData(object):

    """Implementation of the 'ProductData' model.

    TODO: type model description here.

    Attributes:
        nutrients (list of NutrientData): TODO: type description here.
        recipes (list of string): TODO: type description here.
        plus (list of string): TODO: type description here.
        visibility_count (int): TODO: type description here.
        score (double): TODO: type description here.
        amazon_link (string): TODO: type description here.
        manufacturer (string): TODO: type description here.
        ingredients_count (int): TODO: type description here.
        large_image (string): TODO: type description here.
        small_image (string): TODO: type description here.
        serving_size_in_grams (double): TODO: type description here.
        serving_size_unit (string): TODO: type description here.
        servings_per_container (string): TODO: type description here.
        serving_size (string): TODO: type description here.
        ingredients (string): TODO: type description here.
        weight (string): TODO: type description here.
        description (string): TODO: type description here.
        brand (string): TODO: type description here.
        upc (string): TODO: type description here.
        tags (list of string): TODO: type description here.
        category (string): TODO: type description here.
        category_id (int): TODO: type description here.
        name (string): TODO: type description here.
        id (int): TODO: type description here.

    """

    def __init__(self,
                 **kwargs):
        """Constructor for the ProductData class
        
        Args:
            **kwargs: Keyword Arguments in order to initialise the
                object. Any of the attributes in this object are able to
                be set through the **kwargs of the constructor. The values
                that can be supplied and their types are as follows::

                    nutrients -- list of NutrientData -- Sets the attribute nutrients
                    recipes -- list of string -- Sets the attribute recipes
                    plus -- list of string -- Sets the attribute plus
                    visibility_count -- int -- Sets the attribute visibility_count
                    score -- double -- Sets the attribute score
                    amazon_link -- string -- Sets the attribute amazon_link
                    manufacturer -- string -- Sets the attribute manufacturer
                    ingredients_count -- int -- Sets the attribute ingredients_count
                    large_image -- string -- Sets the attribute large_image
                    small_image -- string -- Sets the attribute small_image
                    serving_size_in_grams -- double -- Sets the attribute serving_size_in_grams
                    serving_size_unit -- string -- Sets the attribute serving_size_unit
                    servings_per_container -- string -- Sets the attribute servings_per_container
                    serving_size -- string -- Sets the attribute serving_size
                    ingredients -- string -- Sets the attribute ingredients
                    weight -- string -- Sets the attribute weight
                    description -- string -- Sets the attribute description
                    brand -- string -- Sets the attribute brand
                    upc -- string -- Sets the attribute upc
                    tags -- list of string -- Sets the attribute tags
                    category -- string -- Sets the attribute category
                    category_id -- int -- Sets the attribute category_id
                    name -- string -- Sets the attribute name
                    id -- int -- Sets the attribute id
        
        """
        # Set all of the parameters to their default values
        self.nutrients = None
        self.recipes = None
        self.plus = None
        self.visibility_count = None
        self.score = None
        self.amazon_link = None
        self.manufacturer = None
        self.ingredients_count = None
        self.large_image = None
        self.small_image = None
        self.serving_size_in_grams = None
        self.serving_size_unit = None
        self.servings_per_container = None
        self.serving_size = None
        self.ingredients = None
        self.weight = None
        self.description = None
        self.brand = None
        self.upc = None
        self.tags = None
        self.category = None
        self.category_id = None
        self.name = None
        self.id = None

        # Create a mapping from API property names to Model property names
        replace_names = {
            "nutrients": "nutrients",
            "recipes": "recipes",
            "plus": "plus",
            "visibility_count": "visibility_count",
            "score": "score",
            "amazon_link": "amazon_link",
            "manufacturer": "manufacturer",
            "ingredients_count": "ingredients_count",
            "large_image": "large_image",
            "small_image": "small_image",
            "serving_size_in_grams": "serving_size_in_grams",
            "serving_size_unit": "serving_size_unit",
            "servings_per_container": "servings_per_container",
            "serving_size": "serving_size",
            "ingredients": "ingredients",
            "weight": "weight",
            "description": "description",
            "brand": "brand",
            "upc": "upc",
            "tags": "tags",
            "category": "category",
            "category_id": "category_id",
            "name": "name",
            "id": "id",
        }

        # Parse all of the Key-Value arguments
        if kwargs is not None:
            for key in kwargs:
                # Only add arguments that are actually part of this object
                if key in replace_names:
                    setattr(self, replace_names[key], kwargs[key])

            # Other objects also need to be initialised properly
            if "nutrients" in kwargs:
                # Parameter is an array, so we need to iterate through it
                self.nutrients = list()
                for item in kwargs["nutrients"]:
                    self.nutrients.append(NutrientData(**item))

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
            "nutrients": "nutrients",
            "recipes": "recipes",
            "plus": "plus",
            "visibility_count": "visibility_count",
            "score": "score",
            "amazon_link": "amazon_link",
            "manufacturer": "manufacturer",
            "ingredients_count": "ingredients_count",
            "large_image": "large_image",
            "small_image": "small_image",
            "serving_size_in_grams": "serving_size_in_grams",
            "serving_size_unit": "serving_size_unit",
            "servings_per_container": "servings_per_container",
            "serving_size": "serving_size",
            "ingredients": "ingredients",
            "weight": "weight",
            "description": "description",
            "brand": "brand",
            "upc": "upc",
            "tags": "tags",
            "category": "category",
            "category_id": "category_id",
            "name": "name",
            "id": "id",
        }

        retval = dict()

        return APIHelper.resolve_names(self, replace_names, retval)