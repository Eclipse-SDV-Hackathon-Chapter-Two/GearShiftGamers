from kuksa_client.grpc import Datapoint
from kuksa_client.grpc import DataEntry
from kuksa_client.grpc import DataType
from kuksa_client.grpc import EntryUpdate
from kuksa_client.grpc import Field
from kuksa_client.grpc import Metadata
from kuksa_client.grpc import VSSClient


# DATABROKER_HOST = '127.0.0.1'
databroker_host = '0.0.0.0'
databroker_port = '55555'
client = VSSClient(databroker_host, databroker_port)
client.connect()

import time

while True:
    current_values = client.get_current_values(['Vehicle.Acceleration.Lateral'])
    print(current_values)
    time.sleep(0.1)