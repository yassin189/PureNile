#!/usr/bin/env python
# coding: utf-8

# # Accessing an AutoAI Model
# In this notebook, we use the Watson Machine Learning (WML) API to find the available models available, and find the availablr deployments.
# 
# We then score some records using a Churn model.
# 
# Finally, we show how a deployment could be removed.
# 
# See:<br/>https://wml-api-pyclient-dev-v4.mybluemix.net/<br/>
# https://watson-ml-v4-api.mybluemix.net/<br/>
# https://wml-api-pyclient.mybluemix.net/

#from IPython import get_ipython
#import ipython_genutils
from watson_machine_learning_client import WatsonMachineLearningAPIClient

# In[1]:


# Install the Watson Machine Learning API client
#get_ipython().sys('pip install watson-machine-learning-client-v4')


# In[4]:


wml_credentials = {
  "apikey": "RHc6pM4RDb22TeaARZ8fvRmGTjtPM3i8lRNRWy1uqJQM",
  "instance_id": "809f3173-4753-401e-a9c7-95155f6b93f2",
  "url": "https://eu-gb.ml.cloud.ibm.com"
}


# In[5]:




client = WatsonMachineLearningAPIClient(wml_credentials)


# In[6]:


# List models already in the repository
client.repository.list_models()


# ## Accessing the deployed model
# We extract the information on deployed models and find the deployment for **`Churn model deployment`**.

# In[7]:


# List the deployed models
client.deployments.list()


# In[10]:


# Extract the information for "Churn model deployment" 
deployments_details = client.deployments.get_details()
#print(deployments_details)
deployed_uid = next(item for item in deployments_details['resources'] 
                    if item['entity']["name"] == "Churn model deployment")['metadata']['guid']
#print(deployed_uid)


# ### Score a record

# In[11]:


# Execute the model
scoring_payload = {client.deployments.ScoringMetaNames.INPUT_DATA: 
                   [{
                     'fields': ['ID','Gender','Status','Children','Est Income','Car Owner',
                                'Age','LongDistance','International','Local','Dropped',
                                'Paymethod','LocalBilltype','LongDistanceBilltype',
                                'Usage','RatePlan'], 
                     'values': [[1,'F','S',1.0,38000.0,'N',24.393333,23.56,0.0,206.08,0.0,'CC','Budget','Intnl_discount',229.64,3.0],                      
                                [6,'M','M',2.0,29616.0,'N',49.426667,29.78,0.0,45.5,0.0,  'CH','FreeLocal','Standard',75.29,2.0]
                               ]
                    }]
                  }
predictions = client.deployments.score(deployed_uid, scoring_payload)


# In[13]:


predictions


# In[14]:


for prediction in predictions['predictions'] :
    for result in prediction['values'] :
        print('Prediction: ' + str(result[0]) + ", probability: [" + 
              str(result[1][0]) + ', ' +  str(result[1][1]) + "]" )


# ## Removing a deployed model
# We can remove a model from the repository using the remove method.
# In the example below, we remove the deployed model we just used since we already have the uid.
# We could look over like we did before and remove all the deployed models.
# 
# A similar delete operation can be used to remove the saved models.

# In[ ]:


# Display the list first
#client.deployments.list()


# In[ ]:


# Remove the deployment
#client.deployments.delete(deployed_uid)


# In[ ]:


#client.deployments.list()


# In[ ]:




