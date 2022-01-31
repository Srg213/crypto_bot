# Crypto_Bot


This bot has been created using [Bot Framework](https://dev.botframework.com).
## Edit
Added azure commands file as a [batch file](https://github.com/Srg213/crypto_bot/blob/main/azurecommands.bat)
The deployment ARM templates are also added. These steps will deploy the bot to a new resource group and new service plan. If you want to deploy to an existing resource group, refer to the [documentation](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-deploy-basic-bot?view=azure-bot-service-4.0&tabs=python%2Cuserassigned#deploy-via-arm-template-with-existing-resource-group).
Added a demo video.(https://csg1003200057a8951f.blob.core.windows.net/crypto-bot-demo/WhatsApp%20Video%202022-01-31%20at%205.09.48%20PM.mp4?sp=r&st=2022-01-31T11:50:22Z&se=2022-01-31T19:50:22Z&spr=https&sv=2020-08-04&sr=b&sig=RNZpcdgb9RMO%2F9J91GLESCp6THIUDEC55HO9%2BWr9Bfo%3D).

### Telegram Channel
I have created channel on telegram (https://telegram.me/Crypto_alerts1_bot). Download telegram app before using the bot.

## Prerequisites

This sample **requires** prerequisites in order to run. 
### Install Python 3.6


## Description
The core idea of the project is to alert the user of drastic price changes and provide real-time market data. The alerts set by the user can help him to enter or close a trade based on his trading margins. These alerts can be set by the user on simple messaging platform like Telegram. The bot is developed using Bot Framework SDK and deployed on Azure Bot Service. 


## Downloading and Running the sample
- Run `pip install -r requirements.txt` to install all dependencies
- Check that the cookiecutter package was installed correctly by running cookiecutter --help
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
