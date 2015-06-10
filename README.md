Information Machine API
=================
Due to the UniRest package dependency this SDK only works under Python 2.7
It will not work using Python 3.x

How To Configure:
=================
File test\clienttest.txt contains several parameters in order to fully test the api using APITest.py python file.
Each line of this file represents a certain expected value that you need to give in order to test the api.
The file initially contains the following:

1. YOUR_CLIENT_ID
2. YOUR_CLIENT_SECRET
3. STORE_NAME(EXAMPLE:WALMART)
4. USERNAME_FOR_GIVEN_STORE
5. PASSWORD_FOR_GIVEN_STORE

So, you need to replace the lines in clienttest.txt file with corresponding value.

How To Build:
=============
The generated code uses Python libraries named UniRest and Jsonpickle.

PIP is a popular tool for managing python packages[1] which is installed if you have Python 2.7.9+.
To resolve these packages:
1) From terminal/cmd navigate to the root directory
2) Invoke 'pip install -r requirements.txt'

Note: You will need internet access to resolve these dependencies.

How To Use:
===========
The following shows how to make invoke the LookupController controller.
It is also shown in [2].

    1. Create a "LookupControllerTest.py" file in the root directory.
    2. Add the following import statement
        'from InformationMachineAPILib.Controllers.LookupController import *'
    3. Create a new instance using 'controller = LookupController(client_id, client_secret)'
    4. Invoke an endpoint with the appropriate parameters, for example
        'response = controller.lookup_get_product_alternative_types()'
    5. "response" will now be an object of type GetProductAlternativeTypesWrapper.
    6. To test the response you get, print out a property of "response",
        for example 'print response.result[0].name'.

[1] PIP - https://pip.pypa.io

[2] from InformationMachineAPILib.Controllers.LookupController import *

	controller = LookupController(client_id, client_secret)
    response = controller.lookup_get_product_alternative_types()

    print response.result[0].name

The quickest way to see how you should use the API and library itself is by opening APITest.py python file and see for your self how to use the methods and what kind of flow for calling the api methods is expected.

All methods return wrapper object which contains meta information (number of available requests, maximum number of requests per minute) and result object. Additionally if the result is of an array type, meta object will contain paging information (current page, items per page, total number of items, url to next page if there is a next page).

For more information on which methods are available please go to [Information Machine](http://iamdata.co/swagger/ui/index)
