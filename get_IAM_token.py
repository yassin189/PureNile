import  requests

# Paste your Watson Machine Learning service apikey here
# Use the rest of the code sample as written
apikey = "RHc6pM4RDb22TeaARZ8fvRmGTjtPM3i8lRNRWy1uqJQM"

# Get an IAM token from IBM Cloud
url     = "https://iam.bluemix.net/oidc/token"
headers = { "Content-Type" : "application/x-www-form-urlencoded" }
data    = "apikey=" + apikey + "&grant_type=urn:ibm:params:oauth:grant-type:apikey"
IBM_cloud_IAM_uid = "bx"
IBM_cloud_IAM_pwd = "bx"
response  = requests.post( url, headers=headers, data=data, auth=( IBM_cloud_IAM_uid, IBM_cloud_IAM_pwd ) )
iam_token = response.json()["access_token"]
#print(response.json())
#print(iam_token)