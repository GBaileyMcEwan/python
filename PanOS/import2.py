#!/usr/bin/python3

import requests
from termcolor import colored
import subprocess

# defining the api-endpoint
API_ENDPOINT = "https://192.168.10.1/api"

# your API key here
API_KEY = "LUFRPT1sdmZnZUtNR2t6ejhmNTRCR0hsUTVjZUpka0k9U1dNSTBJbjc2QnRyMzd2am1GWkpwRnFDWGdoQ1JwVHJ6bXJza09NN3Baem9IbXp5V294bkdQbEs2ZnlpM09TVg=="

def sendCommandToFirewall(defparams, defmsg):
    print(colored(defmsg, 'red'))
    r = requests.post(url = API_ENDPOINT, verify=False, params = defparams)
    panOS_response = r.text
    print(colored("The panOS response was:%s"%panOS_response, 'green'))
    print("\n")

def importCertificateFunction(deffile, defparams, defmsg):
    # open file in binary format for reading
    file = {'file': open(deffile,'rb')}
    print(colored(defmsg, 'red'))
    r = requests.post(url = API_ENDPOINT, verify=False, params = defparams, files = file)
    # extracting response text
    panOS_response = r.text
    print(colored("The panOS response was:%s"%panOS_response, 'green'))
    print("\n")

# Allow internet access into our NGINX webserver for LetsEncrypt certificate generation
sendCommandToFirewall({ 'key': API_KEY, 'cmd': '<uid-message><type>update</type><payload><register><entry ip="102.132.173.71"><tag><member>LetsEncryptWebServer</member></tag></entry></register></payload></uid-message>', 'type': 'user-id'}, "Adding IP to Dynamic Address Group")

# Request certificates from LetsEncrypt sudo certbot certonly --nginx -n -d niftyshorts.ddns.net -m niftyshorts@gmail.com --agree-tos
proc = subprocess.run(["sudo","certbot","certonly","--nginx","-n","-d","niftyshorts.ddns.net","-m","niftyshorts@gmail.com","--agree-tos"])
print(f"Got the following output from CertBot: {proc}")

# Allow internet access into our NGINX webserver for LetsEncrypt certificate generation
sendCommandToFirewall({ 'key': API_KEY, 'cmd': '<uid-message><type>update</type><payload><unregister><entry ip="102.132.173.71"><tag><member>LetsEncryptWebServer</member></tag></entry></unregister></payload></uid-message>', 'type': 'user-id'}, "Removing IP from Dynamic Address Group")

# Import the chain certificate
importCertificateFunction("/Users/gbaileymcewa/Documents/nginxCerts/chain1.pem",{ 'key': API_KEY, 'type': 'import', 'category': 'certificate', 'certificate-name': 'niftyshorts_chain', 'format': 'pem' },"Importing Chain")

# Import the LetsEncrypt domain certificate
importCertificateFunction("/Users/gbaileymcewa/Documents/nginxCerts/cert1.pem",{ 'key': API_KEY, 'type': 'import', 'category': 'certificate', 'certificate-name': 'niftyshorts_cert_privKey', 'format': 'pem', 'passphrase': 'Tempest7!' },"Importing Certificate")

# Import the LetsEncrypt private key
importCertificateFunction("/Users/gbaileymcewa/Documents/nginxCerts/newPrivKey.pem",{ 'key': API_KEY, 'type': 'import', 'category': 'private-key', 'certificate-name': 'niftyshorts_cert_privKey', 'format': 'pem', 'passphrase': 'Tempest7!' },"Importing Private Key")

#Commit config to firewall
sendCommandToFirewall({ 'key': API_KEY, 'cmd': '<commit></commit>', 'type': 'commit'}, "Committing config to NGFW")
