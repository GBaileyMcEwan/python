#!/usr/bin/python3

import requests

# defining the api-endpoint
API_ENDPOINT = "https://192.168.10.1/api"

# your API key here
API_KEY = "LUFRPT1sdmZnZUtNR2t6ejhmNTRCR0hsUTVjZUpka0k9U1dNSTBJbjc2QnRyMzd2am1GWkpwRnFDWGdoQ1JwVHJ6bXJza09NN3Baem9IbXp5V294bkdQbEs2ZnlpM09TVg=="

# specify the file you want to upload - first upload chain
file = {'file': open('/Users/gbaileymcewa/Documents/nginxCerts/chain1.pem','rb')}

# specify the HTTP headers - these are stored in a hash/dictionary with key/value pairs

# for basic cert with no private key attached
params = { 'key': API_KEY, 'type': 'import', 'category': 'certificate', 'certificate-name': 'niftyshorts_chain', 'format': 'pem' }

print("Attempting chain upload...\n")
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, params = params, files = file)

# extracting response text
panOS_response = r.text
print("The panOS response for uploading the chain was:%s"%panOS_response)

# ---------------------------------------------------------

print("\n\nNow attempting certificate upload\n")

# specify the file you want to upload - first upload chain
file = {'file': open('/Users/gbaileymcewa/Documents/nginxCerts/cert1.pem','rb')}

# for private key
params = { 'key': API_KEY, 'type': 'import', 'category': 'certificate', 'certificate-name': 'niftyshorts_cert_privKey', 'format': 'pem', 'passphrase': 'Tempest7!' }

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, params = params, files = file)

# extracting response text
panOS_response = r.text
print("The panOS response for uploading the privatekey was:%s"%panOS_response)


# ---------------------------------------------------------
print("\n\nNow attempting private key upload\n")

# specify the file you want to upload - first upload chain
file = {'file': open('/Users/gbaileymcewa/Documents/nginxCerts/newPrivKey.pem','rb')}

# for private key
params = { 'key': API_KEY, 'type': 'import', 'category': 'private-key', 'certificate-name': 'niftyshorts_cert_privKey', 'format': 'pem', 'passphrase': 'Tempest7!' }

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, verify=False, params = params, files = file)

# extracting response text
panOS_response = r.text
print("The panOS response for uploading the privatekey was:%s"%panOS_response)
