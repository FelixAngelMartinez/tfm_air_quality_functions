# tfm_air_quality_functions
Azure Functions

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Pandas)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/FelixAngelMartinez/tfm_air_quality_functions)
![GitHub last commit](https://img.shields.io/github/last-commit/FelixAngelMartinez/tfm_air_quality_functions)
![GitHub all releases](https://img.shields.io/github/downloads/FelixAngelMartinez/test_1/tfm_air_quality_functions)
![GitHub issues](https://img.shields.io/github/issues-raw/FelixAngelMartinez/tfm_air_quality_functions)
![GitHub contributors](https://img.shields.io/github/contributors/FelixAngelMartinez/tfm_air_quality_functions)
![GitHub followers](https://img.shields.io/github/followers/FelixAngelMartinez?style=social)

## Description
Repository belonging to the development of the Master Thesis entitled "Intelligent system for monitoring indoor air quality and fight against COVID-19", which develops a system to monitor air quality in enclosed spaces using IoT devices and Machine Learning algorithms. All this developed with a Cloud approach.

This Master's Thesis has been developed within the framework of the "Master in Computer Engineering" of the University of Castilla la Mancha.

## Repository elements
In this respository there are 2 Azure functions:
* **ServiceBusQueueToCosmos**: it forward data from the Service Bus Queue to the CosmosDB
* **CosmosToThingSpeak**: it send the device dato direct from the CosmosDB to the [Thing Speak](https://thingspeak.com/)

## Requirements
It is mandatory to have installed [Visual Studio Code](https://code.visualstudio.com/) and the plugin Azure Function.

## Commands
Once it is already sign in, you can launch the following commands:
```console
  $func azure functionapp publish airq-fun2 --build local
```

## Master's thesis
The report of the project will be published in the university repository.
[UCLM Repository](https://ruidera.uclm.es/)

## License:
Project under license [LICENSE](LICENSE)

---
_Project carried out by:_
* **Félix Ángel Martínez Muela** - [Félix Ángel Martínez](https://github.com/FelixAngelMartinez)