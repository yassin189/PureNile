from cloudant.client import Cloudant
from flask import Flask, jsonify, render_template, request,json


serviceUsername="10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix"
servicePassword="8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3"
serviceURL="https://10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix:8fda4f0c4d5823a274e6d500933f2f6cbe71ed6ae7a1ba3cb23d2f48befd32e3@10c858b4-ffff-4ce2-a8a7-fe09116a0519-bluemix.cloudantnosqldb.appdomain.cloud"


#create cloudant client
cloudantClient = Cloudant(serviceUsername,servicePassword , url=serviceURL)

#getting an array like this [lattiude, longitude]
latlong =["latitude","longitude"]


#getting the lattitude and longitude for all sensoor owned by a specified company
def GetData(companyName):

    #update database name with the dataname
    databaseName = "pure_nile_locations"
    #The to be returned array of lat and long arrays
    ArrayofLatLong = []
    #connect to Cloudant database and retrieve data for the database
    cloudantClient.connect()

    endPoint = '{0}/{1}'.format(serviceURL, databaseName + "/_all_docs")
    params = {'include_docs': 'true'}
    response = cloudantClient.r_session.get(endPoint, params=params)
    data = response.json()
    # print(companyName)
    #print(data)

    #initalize lattitudeArray and longitudeArray
    # latitude = []
    # longitude=[]

    # get length of rows
    rowsLength = len(data["rows"])

    #loop through data
    for x in range(0, rowsLength):

        #if the companyName exists
        if(companyName in data["rows"][x]["doc"]["data"]["authority"]):            
            latitude = data["rows"][x]["doc"]["data"]["lat"]
            latlong[0] = latitude
            longitude = data["rows"][x]["doc"]["data"]["long"]
            latlong[1] = longitude
            latlongcopy = latlong.copy()
            #a.insert(len(a), x)
            ArrayofLatLong.append(latlongcopy)
            #print(latlong)
            # latlong.clear()
            #print(ArrayofLatLong)

    # pyArray = list(latlong)
    # pyjson = json.dumps(latlong)
    # #disconnect from cloudant db
    cloudantClient.disconnect()

    #return lattitudeArray and longitudeArray        
    return ArrayofLatLong

# pyArray = json.dumps(GetData("Company_3"))
# print(pyArray)

#////
