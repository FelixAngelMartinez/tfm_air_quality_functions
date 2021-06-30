import logging
import os
import requests
import azure.functions as func

# https://docs.microsoft.com/en-us/python/api/azure-functions/azure.functions.document?view=azure-python#to-json------str
def main(documents: func.DocumentList) -> str:
    logging.info('Function: CosmosToThingSpeak, Version: 1.0')
    url = 'https://api.thingspeak.com/update'
    api_key = os.environ["ThingSpeakAPIKEY"]
    device = os.environ["deviceToThingSpeak"]
    if documents:
        logging.info('Nº Documents: %d',len(documents))
        for i in range(len(documents)):
            logging.info('Document id: %s', documents[i]['id'])
            logging.info('Device id: %s',documents[i]['deviceid'])
            logging.info('Time: %s',documents[i]['time'])
            if documents[i]['deviceid'] == device:                
                logging.info(documents[i].to_json())
                query = {'api_key': api_key,'field1':documents[i]['temperature'] ,'field2': documents[i]['humidity'],'field3': documents[i]['co2'],'field4': documents[i]['pm25'],'field5': documents[i]['pm10'],'field6': documents[i]['tvoc'],'field7': documents[i]['eco2'],'field8': documents[i]['lux']}
                response = requests.get(url, params=query)
                logging.info(response)