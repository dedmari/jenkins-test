import kfp
import json

experiment_id = '3a556a1f-6629-4b84-948c-79e4a6d95283'
pipeline_id = '89b7a571-10d3-4ca7-9922-e8a847adfd12'
run_name = 'testjenkinsrunpikfp'

kubeflow_host = ''
with open('./config/kubeflow.json') as kf_config:
  data = json.load(kf_config)
  kubeflow_host =  data['kubeflow'][0]['host']

pipeline_run_params = {}
with open('./config/pipeline.json') as pipeline_config):
  data = json.load(pipeline_config)
  pipeline_run_params = data['pipeline_run_params']
 

client = kfp.Client()

run = client.run_pipeline(experiment_id = experiment_id, pipeline_id = pipeline_id, job_name = run_name, params = pipeline_run_params)
print('Run link: %s%s/#/runs/details/%s' % (kubeflow_host, client._get_url_prefix(), run.id))
