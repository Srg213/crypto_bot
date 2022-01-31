
::Have the Azure CLI installed
::Login to Azure: 
az login

::Save your Azure subscription id from the output of the login command, or use 
az account listaz login

::Set the subscription to use for deploying the bot
az account set --subscription "<azure-subscription-id>"

::Create an application registration: 
az ad app create --display-name "crypto_bot" --password "AtLeastSixteenCharacters_0" --available-to-other-tenants

az identity create --group "resourceGroupName"\
                     --name "userAssignedManagedIdentityName"

::To deploy via ARM template with new resource group
az deployment sub create --template-file "<path/to/deploymentTemplates/template-with-new-rg.json>" \
                        --location eastus2\
                        --parameters appId="<app-id-from-previous-step>"\
                        appSecret="<password-from-previous-step>"\
                        botId="<id or bot-app-service-name>"\
                        botSku=F0 \
                        newAppServicePlanName="<new-service-plan-name>"\
                        newWebAppName="<bot-app-service-name>"\
                        groupName="<new-group-name>"\
                        groupLocation="<region-location-name>"\
                        newAppServicePlanLocation="<region-location-name>"\
                        --name "<bot-app-service-name>"

::Create a zip file of your bot: Select all the files under the folder that contains the app.py file and package them.
::This also includes the .env file.
az webapp deployment source config-zip --resource-group "<resource-group-name>"\
                        --name "<name-of-web-app>"\
                        --src "<project-zip-path>"

::If you want to check the deployment logs, run 
az webapp log deployment show -n <name-of-web-app> -g <resource-group-name>




