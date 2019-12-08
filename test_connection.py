import json
import os
import time
from datetime import timedelta, date
from dotenv import load_dotenv

import dataset

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


serviceUsername="10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix"
servicePassword="8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3"
serviceURL="https://10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix:8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3@10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix.cloudantnosqldb.appdomain.cloud"

cloudantClient = Cloudant(serviceUsername,servicePassword , url=serviceURL)


def Device_data_per_day(inputDeviceId, inputDate):
    """
    Retrieve data for a day for a device per user input
    """
    #update database name with the dataname
    databaseName = "iotp_j1kovt_all_li_events_"+ inputDate

    #connect to Cloudant database and retrieve data for the database
    cloudantClient.connect()
    endPoint = '{0}/{1}'.format(serviceURL, databaseName + "/_all_docs")
    params = {'include_docs': 'true'}
    response = cloudantClient.r_session.get(endPoint, params=params)
    data = response.json()

    #initalize dataArray
    dataArray = []

    #get length of rows
    rowsLength = len(data["rows"])

    #loop through data
    for x in range(0, rowsLength):

        #if device id exists
        if("deviceId" in data["rows"][x]["doc"]):
            deviceID = data["rows"][x]["doc"]["deviceId"]

            #if deivceId matches user provided device ID, append data to dataArray
            if deviceID == inputDeviceId:
                timeStamp = data["rows"][x]["doc"]["timestamp"]
                if data["rows"][x]["doc"]["deviceType"] == "Temperature_Sensors":
                    temperature = data["rows"][x]["doc"]["data"]["temperature"]
                    jsonData = {"deviceID": deviceID, "timeStamp": timeStamp, "temperature": temperature}
                    dataArray.append(jsonData)
                elif data["rows"][x]["doc"]["deviceType"] == "pH_Sensors":
                    pH = data["rows"][x]["doc"]["data"]["pH"]
                    jsonData = {"deviceID": deviceID, "timeStamp": timeStamp, "pH": pH}
                    dataArray.append(jsonData)


    #disconnect from cloudant db
    cloudantClient.disconnect()

    #return dataArray
    return dataArray

