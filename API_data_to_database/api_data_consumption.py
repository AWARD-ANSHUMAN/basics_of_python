# importing python packages using pip

import requests
import pandas as pd
import os
import sys

# rapid api

# https://blog.restcase.com/4-most-used-rest-api-authentication-methods/

# 1: Url= xxxxxx    (url of rest api resource: location)

# 2: Param = {dict}     (API parameters for extra information on data requires.also contains essential/optional parameters)

# 3: Apikey = ******************

# 4: headers = {authorization = "bearer key" + apikey} (authentication & authorization)

# Api_response = request.get(url, parameters- {}, headers= headers).json()
