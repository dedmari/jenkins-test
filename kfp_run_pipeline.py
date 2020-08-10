import kfp

experiment_id = '3a556a1f-6629-4b84-948c-79e4a6d95283'
pipeline_id = '89b7a571-10d3-4ca7-9922-e8a847adfd12'
run_name = 'testjenkinsrunpikfp'

client = kfp.Client()

run = client.run_pipeline(experiment_id = experiment_id, pipeline_id = pipeline_id, job_name = run_name)
print(‘Run link: %s/#/runs/details/%s’ % (client._get_url_prefix(), run.id))
