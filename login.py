import json
import os
from flask import session
#from dotenv import load_dotenv

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

serviceUsername="10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix"
servicePassword="8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3"
serviceURL="https://10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix:8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3@10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix.cloudantnosqldb.appdomain.cloud"


#create cloudant client
cloudantClient = Cloudant(serviceUsername,servicePassword , url=serviceURL)

def check_account(username, password):
    
    databaseName = "authority_accounts"

    #connect to Cloudant database and retrieve data for the database
    cloudantClient.connect()
    endPoint = '{0}/{1}'.format(serviceURL, databaseName + "/_all_docs")
    params = {'include_docs': 'true'}
    response = cloudantClient.r_session.get(endPoint, params=params)
    data = response.json()
    
    authority_name = " "
    
    for x in range(0,len(data["rows"])):
       
        if (data["rows"][x]["doc"]["data"]["username"] == username) and (data["rows"][x]["doc"]["data"]["password"] == password):
            authority_name = data["rows"][x]["doc"]["data"]["name"]
            cloudantClient.disconnect()
            print(authority_name)
            return authority_name
        
        elif (data["rows"][x]["doc"]["data"]["username"] == username) and (data["rows"][x]["doc"]["data"]["password"] != password):
            cloudantClient.disconnect()
            return authority_name
        
        elif (data["rows"][x]["doc"]["data"]["username"] != username) and (data["rows"][x]["doc"]["data"]["password"] == password):
            cloudantClient.disconnect()
            return authority_name

    
    cloudantClient.disconnect()
    return authority_name
            
      

