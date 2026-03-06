pip install databricks-cli 

databricks configure --token 

databricks secrets create-scope --scope <scopeName>

databricks secrets put --scope <scopeName> --key API_KEY

databricks secrets put --scope <scopeName> --key FILE_PATH

databricks secrets put --scope <scopeName> --key sender-email

databricks secrets put --scope <scopeName> --key receiver-email

databricks secrets put --scope <scopeName> --key sender-password
