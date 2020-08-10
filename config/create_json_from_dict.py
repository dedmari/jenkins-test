import json 

data = {}
data['kubeflow'] = []
data['kubeflow'].append({ 'host': 'https://172.30.92.10'})

with open('kubeflow.json', 'w') as kubeflow_config:
  json.dump(data, kubeflow_config)
