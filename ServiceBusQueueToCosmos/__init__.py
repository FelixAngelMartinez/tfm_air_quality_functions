import logging

import azure.functions as func
from  azure.cosmos import cosmos_client

def main(msg: func.ServiceBusMessage, cosmos: func.Out[func.Document]):
    logging.info('Function: ServiceBusQueueToCosmos, Version: 1.0')
    logging.info('Python ServiceBus queue trigger processed message: %s',
                 msg.get_body().decode('utf-8'))

    cosmos.set(func.Document.from_json(msg.get_body().decode('utf-8')))