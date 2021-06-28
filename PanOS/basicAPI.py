#!/usr/bin/python3

import requests

# defining the api-endpoint
API_ENDPOINT = "https://192.168.10.1/api"

# your API key here
API_KEY = "LUFRPT1sdmZnZUtNR2t6ejhmNTRCR0hsUTVjZUpka0k9U1dNSTBJbjc2QnRyMzd2am1GWkpwRnFDWGdoQ1JwVHJ6bXJza09NN3Baem9IbXp5V294bkdQbEs2ZnlpM09TVg=="

params = dict(key=API_KEY, type='op', cmd='<show><routing><route><type>static</type></route></routing></show>')

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, params = params)

# extracting response text
panOS_response = r.text
print("The panOS response is:%s"%panOS_response)
