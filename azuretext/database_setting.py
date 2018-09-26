# all the parameters to connect to sql

import pyodbc
import urllib.parse

server = 'tahsin.database.windows.net'
database = 'AzureML'
username = 'tahsinsql'
password = 'Excellence1!'
driver= '{ODBC Driver 13 for SQL Server}'



# Configure Database URI: 
params = urllib.parse.quote_plus('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password)

params = 'DRIVER%3D%7BODBC+Driver+13+for+SQL+Server%7D%3BSERVER%3Dtahsin.database.windows.net%3BDATABASE%3DAzureML%3BUID%3Dtahsinsql%3BPWD%3DExcellence1%21'