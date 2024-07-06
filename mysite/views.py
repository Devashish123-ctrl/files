from django.shortcuts import render
import requests
import random
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse


encryption_key = "FtmJ7frzTyWOzintybbqIWzwwclcPtaI"
access_token = "0e186445-0647-417c-ae27-8098533f1914"
campaign_id = "6a0fa162-fb4c-4074-a6d4-402744e3590b"
endpoint = "https://d3398n96t5wqx9.cloudfront.net/UsersAquisition/"

def fine(request): 
       

        # Headers for the request
        headers = {
            'accesstoken': access_token,
            'Content-Type': 'application/json',
        

        }

        # Payload with the required filters
        payload = {
            'campaign_id': campaign_id,
            'country': 'IRAQ'
        }




        payload ={
        "DeviceInfo": {
            "PackageName": "com.test.com",
            "LangCode": "en",
            "DeviceID": "test_dev_doc",
        },
        "Referrer": {
            "Affiliate": {
            "Campaign": "6a0fa162-fb4c-4074-a6d4-402744e3590b",
            "ClickID": "1",
            "Pub_ID": "your pub id",
            "Aff_ID": "your aff id",
            "extra": "",
            "extra1": "",
            "firstPageButtonID": "msisdn-entry",
            "secondPageButtonID": "pin-entry",
            "Country": "IRAQ"
            }
        },
        "Request": {
            "Action": "1",
            "TransactionID": f'{random.randint(0, 111111111111111111111111111111111111111111111111111111111111111111111111111111111)}',
            "SessionID": "",
            "Scheme": "",
            "MSISDN": "",
            "PinCode": ""
        }
        }
        
        response = requests.post(endpoint, headers=headers, json=payload)
        data = response.json()["SessionID"]
        message = response.json()['MessageToShow']
        return render(request,"index.html",{
              "SessionID":data,
              "message":message
        })











@csrf_exempt          
def submit(request):
        SessionID = request.POST.get('SessionID')
     # Headers for the request
        headers = {
            'accesstoken': access_token,
            'Content-Type': 'application/json',
        

        }

        # Payload with the required filters
        payload = {
            'campaign_id': campaign_id,
            'country': 'IRAQ'
        }




        payload ={
        "DeviceInfo": {
            "PackageName": "com.test.com",
            "LangCode": "en",
            "DeviceID": "test_dev_doc",
        },
        "Referrer": {
            "Affiliate": {
            "Campaign": "6a0fa162-fb4c-4074-a6d4-402744e3590b",
            "ClickID": "1",
            "Pub_ID": "your pub id",
            "Aff_ID": "your aff id",
            "extra": "",
            "extra1": "",
            "firstPageButtonID": "msisdn-entry",
            "secondPageButtonID": "pin-entry",
            "Country": "IRAQ"
            }
        },
        "Request": {
            "Action": "2",
            "TransactionID": f'{random.randint(0, 111111111111111111111111111111111111111111111111111111111111111111111111111111111)}',
            "SessionID": SessionID,
            "Scheme": "",
            "MSISDN": "",
            "PinCode": ""
        }
        }
        response = requests.post(endpoint, headers=headers, json=payload)
        data = response.json()["SessionID"]
        message = response.json()['MessageToShow']
        return HttpResponse(json.dumps({
              "SessionID":data,
              "message":message}))

    