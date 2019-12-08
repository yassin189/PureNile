import urllib3, json, requests
import get_IAM_token

ml_instance_id = "809f3173-4753-401e-a9c7-95155f6b93f2"

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + get_IAM_token.iam_token, 'ML-Instance-ID': ml_instance_id}

payload_scoring = {"input_data": [{"fields": ["ID", "Gender", "Status", "Children", "Est Income", "Car Owner", "Age", "LongDistance", "International", "Local", "Dropped", "Paymethod", "LocalBilltype", "LongDistanceBilltype", "Usage", "RatePlan"], "values": [[1,'F','S',1.0,38000.0,'N',24.393333,23.56,0.0,206.08,0.0,'CC','Budget','Intnl_discount',229.64,3.0], [6,'M','M',2.0,29616.0,'N',49.426667,29.78,0.0,45.5,0.0,  'CH','FreeLocal','Standard',75.29,2.0]]}]}

response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/v4/deployments/a621f965-3e02-45e2-90b4-962c858d1f83/predictions', json=payload_scoring, headers=header)
print("Scoring response")
predictions=json.loads(response_scoring.text)


for prediction in predictions['predictions'] :
    for result in prediction['values'] :
        print('Prediction: ' + str(result[0]) + ", probability: [" + 
              str(result[1][0]) + ', ' +  str(result[1][1]) + "]" )

