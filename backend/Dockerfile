FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY backend/requirements.txt /
RUN pip install -r /requirements.txt

COPY backend/ /home/site/wwwroot
