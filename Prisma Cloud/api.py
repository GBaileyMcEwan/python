import requests
import json
#from requests_toolbelt.utils import dump


def sendPostToPrismaCloud(headers, payload):
    apiReq = requests.post(
        "https://console-master-gbaileymcewa1430.gbaileymcewa.demo.twistlock.com/api/v1/authenticate", verify=False, json=payload, headers=headers)
    return({apiReq.text})


username = input("Please enter your Prisma Cloud username: ")
password = input("Please enter your Prisma Cloud password: ")
myPayload = {"username": username, "password": password}
myHeaders = {"Content-Type": "application/json"}
myToken = sendPostToPrismaCloud(myHeaders, myPayload)
print(type(myToken))
print(myToken)

for element in myToken:
    print(f"Element: {element}")
    myDict = json.loads(element)

print(myDict["token"])
#data = dump.dump_all(apiReq)

#print(f"\r\n\r\nData: {data}")
