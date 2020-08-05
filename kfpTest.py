import kfp

client = kfp.Client()

print(client.list_experiments())
