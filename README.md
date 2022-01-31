# Crypto_Bot


This bot has been created using [Bot Framework](https://dev.botframework.com).
## Edit
Added azure commands file as a batch file. (./azurecommands.bat).
The deployment templates are also added. These steps will deploy the bot to a new resource group. If you want to deploy to an existing resource group, refer to the [documentation].(https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-deploy-basic-bot?view=azure-bot-service-4.0&tabs=python%2Cuserassigned#deploy-via-arm-template-with-existing-resource-group)

### Telegram Channel
I have created channel on telegram (https://telegram.me/Crypto_alerts1_bot). Download telegram app before using the bot.

## Prerequisites

This sample **requires** prerequisites in order to run. 
### Install Python 3.6


## Description
The core idea of the project is to alert the user of drastic price changes and provide real-time market data. The alerts set by the user can help him to enter or close a trade based on his trading margins. These alerts can be set by the user on simple messaging platform like Telegram. The bot is developed using Bot Framework SDK and deployed on Azure Bot Service. 


## Downloading and Running the sample
- Run `pip install -r requirements.txt` to install all dependencies
- Run `python app.py`


## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- Enter a Bot URL of `http://localhost:3978/api/messages`


## References

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
