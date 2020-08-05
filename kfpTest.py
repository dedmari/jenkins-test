import kfp.components as comp
import kfp.dsl as dsl
import kfp

client = kfp.Client()

print(client.list_experiments())
