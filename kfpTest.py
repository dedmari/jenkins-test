import kfp

print(str(kfp.__version__))
#cookie_xsrf = "_xsrf=2|8ae5c4fb|72dfaf6152e6ec46122fb784c421578c|1596544754"
#cookie_authservice = "authservice_session=MTU5OTEyOTk0M3xOd3dBTkZnelVrWklURTlhVmxOWVFscE9WbEpMU1VNMVNrTk9OVkJGVnpSVFUxbFdWMHBJTlZwSE4wVlNRa1pDVVVKQ1ZVcEdUbEU9fILxlm8-tsJdO7tJJyuH8y6kAuKSPDDUJHLWIkytSAS1"
#combined_cookies = cookie_xsrf + "; " + cookie_authservice
#client = kfp.Client(namespace="admin", cookies=cookie_authservice)
host = "https://172.30.92.10:443/pipeline"
client = kfp.Client(host=host)
print(client.list_pipelines())
