#import stuff
import streamlit as st
import pandas as pd
from datetime  import datetime
import numpy as np

#put an image??
st.image('cvent_logo_rgb-®.png')

#put heading on the webpage
st.markdown("The predictions below are based off of the monthly costs for each of the AWS Budget line items owned by Mike Tiffany, as well as cost predictions for each of the database services. They are meant to act as a guide for each month's budget estimate; if you are a budget manager and know there will be changes that you think will increase or decrease the expected cost, please adjust this number accordingly")
st.markdown("The numbers below will be updated with the predictions for the current month and the next 2 months before the 15th based on the costs from the last month")



# have a dropdown with all the budget line items I have models for
line_item_list = [
'Business Transient - App',
'Conference',
'Corporate Systems',
'Event Management - Couchbase',
'Oracle Financials',
'Passkey',
'Data Retention',
'Shared RDS',
'Shared DynamoDB',
'Shared SQL Server',
'Social Tables',
'Speed RFP',
'Wedding Spot']
line_item = st.selectbox('Choose a line item to see predictions',line_item_list)

#load in all the datasets
#Business Transient/App
BusinessTransient = pd.read_csv('bt_app_prophet_predictions1.csv')
BusinessTransientvalues = []
for i in BusinessTransient['yhat']:
    BusinessTransientvalues.append("${:,.2f}".format(i))

BusinessTransient[['yhat_vals']] = pd.DataFrame(BusinessTransientvalues)
BusinessTransient['Date'] = BusinessTransient['ds']
BusinessTransient['Predicted Value'] = BusinessTransient['yhat_vals']
bt_app_df = BusinessTransient[['Date','Predicted Value']]


#CSN
Conference = pd.read_csv('conference_prophet_predictions1.csv')
Conferencevalues = []
for i in Conference['yhat']:
    Conferencevalues.append("${:,.2f}".format(i))

Conference[['yhat_vals']] = pd.DataFrame(Conferencevalues)
Conference['Date'] = Conference['ds']
Conference['Predicted Value'] = Conference['yhat_vals']
conference_df = Conference[['Date','Predicted Value']]


Corporate_Systems = pd.read_csv('corporate_systems_prophet_predictions1.csv')
Corporate_Systemsvalues = []
for i in Corporate_Systems['yhat']:
    Corporate_Systemsvalues.append("${:,.2f}".format(i))

Corporate_Systems[['yhat_vals']] = pd.DataFrame(Corporate_Systemsvalues)
Corporate_Systems['Date'] = Corporate_Systems['ds']
Corporate_Systems['Predicted Value'] = Corporate_Systems['yhat_vals']
corporate_systems_df = Corporate_Systems[['Date','Predicted Value']]


EMCouch = pd.read_csv('em_couch_prophet_predictions1.csv')
EMCouchvalues = []
for i in EMCouch['yhat']:
    EMCouchvalues.append("${:,.2f}".format(i))

EMCouch[['yhat_vals']] = pd.DataFrame(EMCouchvalues)
EMCouch['Date'] = EMCouch['ds']
EMCouch['Predicted Value'] = EMCouch['yhat_vals']
em_couch_df = EMCouch[['Date','Predicted Value']]


Oracle_Financials = pd.read_csv('oracle_financials_prophet_predictions1.csv')
Oracle_Financialsvalues = []
for i in Oracle_Financials['yhat']:
    Oracle_Financialsvalues.append("${:,.2f}".format(i))

Oracle_Financials[['yhat_vals']] = pd.DataFrame(Oracle_Financialsvalues)
Oracle_Financials['Date'] = Oracle_Financials['ds']
Oracle_Financials['Predicted Value'] = Oracle_Financials['yhat_vals']
oracle_financials_df = Oracle_Financials[['Date','Predicted Value']]


Passkey = pd.read_csv('passkey_prophet_predictions1.csv')
Passkeyvalues = []
for i in Passkey['yhat']:
    Passkeyvalues.append("${:,.2f}".format(i))

Passkey[['yhat_vals']] = pd.DataFrame(Passkeyvalues)
Passkey['Date'] = Passkey['ds']
Passkey['Predicted Value'] = Passkey['yhat_vals']
passkey_df = Passkey[['Date','Predicted Value']]


Data_Retention = pd.read_csv('data_retention_prophet_predictions1.csv')
Data_Retentionvalues = []
for i in Data_Retention['yhat']:
    Data_Retentionvalues.append("${:,.2f}".format(i))

Data_Retention[['yhat_vals']] = pd.DataFrame(Data_Retentionvalues)
Data_Retention['Date'] = Data_Retention['ds']
Data_Retention['Predicted Value'] = Data_Retention['yhat_vals']
data_retention_df = Data_Retention[['Date','Predicted Value']]


#Shared_Couchbase = pd.read_csv('shared_couchbase_prophet_predictions.csv')
Shared_DynamoDB = pd.read_csv('shared_dynamodb_prophet_predictions1.csv')
Shared_DynamoDBvalues = []
for i in Shared_DynamoDB['yhat']:
    Shared_DynamoDBvalues.append("${:,.2f}".format(i))

Shared_DynamoDB[['yhat_vals']] = pd.DataFrame(Shared_DynamoDBvalues)
Shared_DynamoDB['Date'] = Shared_DynamoDB['ds']
Shared_DynamoDB['Predicted Value'] = Shared_DynamoDB['yhat_vals']
shared_dynamodb_df = Shared_DynamoDB[['Date','Predicted Value']]


Shared_RDS = pd.read_csv('shared_rds_prophet_predictions1.csv')
Shared_RDSvalues = []
for i in Shared_RDS['yhat']:
    Shared_RDSvalues.append("${:,.2f}".format(i))

Shared_RDS[['yhat_vals']] = pd.DataFrame(Shared_RDSvalues)
Shared_RDS['Date'] = Shared_RDS['ds']
Shared_RDS['Predicted Value'] = Shared_RDS['yhat_vals']
shared_rds_df = Shared_RDS[['Date','Predicted Value']]


Shared_SQL_Server = pd.read_csv('shared_sqlserver_prophet_predictions1.csv')
Shared_SQL_Servervalues = []
for i in Shared_SQL_Server['yhat']:
    Shared_SQL_Servervalues.append("${:,.2f}".format(i))

Shared_SQL_Server[['yhat_vals']] = pd.DataFrame(Shared_SQL_Servervalues)
Shared_SQL_Server['Date'] = Shared_SQL_Server['ds']
Shared_SQL_Server['Predicted Value'] = Shared_SQL_Server['yhat_vals']
shared_sql_server_df = Shared_SQL_Server[['Date','Predicted Value']]


Social_Tables = pd.read_csv('socialtables_prophet_predictions1.csv')
Social_Tablesvalues = []
for i in Social_Tables['yhat']:
    Social_Tablesvalues.append("${:,.2f}".format(i))

Social_Tables[['yhat_vals']] = pd.DataFrame(Social_Tablesvalues)
Social_Tables['Date'] = Social_Tables['ds']
Social_Tables['Predicted Value'] = Social_Tables['yhat_vals']
socialtables_df = Social_Tables[['Date','Predicted Value']]


SpeedRFP = pd.read_csv('speedrfp_prophet_predictions1.csv')
SpeedRFPvalues = []
for i in SpeedRFP['yhat']:
    SpeedRFPvalues.append("${:,.2f}".format(i))

SpeedRFP[['yhat_vals']] = pd.DataFrame(SpeedRFPvalues)
SpeedRFP['Date'] = SpeedRFP['ds']
SpeedRFP['Predicted Value'] = SpeedRFP['yhat_vals']
speedrfp_df = SpeedRFP[['Date','Predicted Value']]


Wedding_Spot = pd.read_csv('weddingspot_prophet_predictions1.csv')
Wedding_Spotvalues = []
for i in Wedding_Spot['yhat']:
    Wedding_Spotvalues.append("${:,.2f}".format(np.absolute(i)))

Wedding_Spot[['yhat_vals']] = pd.DataFrame(Wedding_Spotvalues)
Wedding_Spot['Date'] = Wedding_Spot['ds']
Wedding_Spot['Predicted Value'] = Wedding_Spot['yhat_vals']
weddingspot_df = Wedding_Spot[['Date','Predicted Value']]


#make varible to hold them

# have a table that updates dynamically with the model being displayed and the predictions for the next 3 months (rolling?)
#Passkey['ds'][5:7] == datetime.now().strftime("%m")
#Passkey['ds'][10][5:7]
    #Return Conference df
if line_item == 'Business Transient - App':
    line_item + " Costs"
    st.dataframe(bt_app_df.loc[(bt_app_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (bt_app_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Conference df
elif line_item == 'Conference':
    line_item + " Costs"
    st.dataframe(conference_df.loc[(conference_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (conference_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Corporate Services df
elif line_item == 'Corporate Systems':
    line_item + " Costs"
    st.dataframe(corporate_systems_df.loc[(corporate_systems_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (corporate_systems_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return EM Couch df
elif line_item == 'Event Management - Couchbase':
    line_item + " Costs"
    st.dataframe(em_couch_df.loc[(em_couch_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (em_couch_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Oracle Financials df
elif line_item == 'Oracle Financials':
    line_item + " Costs"
    st.dataframe(oracle_financials_df.loc[(oracle_financials_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (oracle_financials_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Passkey df
elif line_item == 'Passkey':
    line_item + " Costs"
    st.dataframe(passkey_df.loc[(passkey_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (passkey_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Data Retention df
elif line_item == 'Data Retention':
    line_item + " Costs"
    st.dataframe(data_retention_df.loc[(data_retention_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (data_retention_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))]) 
    #Return Shared RDS df
elif line_item == 'Shared RDS':
    line_item + " Costs"
    st.dataframe(data_retention_df.loc[(data_retention_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (data_retention_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Shared DynamoDB df
elif line_item == 'Shared DynamoDB':
    line_item + " Costs"
    st.dataframe(shared_dynamodb_df.loc[(shared_dynamodb_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (shared_dynamodb_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Shared SQL Server df
elif line_item == 'Shared SQL Server':
    line_item + " Costs"
    st.dataframe(shared_sql_server_df.loc[(shared_sql_server_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (shared_sql_server_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Social Tables df
elif line_item == 'Social Tables':
    line_item + " Costs"
    st.dataframe(socialtables_df.loc[(socialtables_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (socialtables_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Speed RFP df
elif line_item == 'Speed RFP':
    line_item + " Costs"
    st.dataframe(speedrfp_df.loc[(speedrfp_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (speedrfp_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Wedding Spot df
elif line_item == 'Wedding Spot':
    line_item + " Costs"
    st.dataframe(weddingspot_df.loc[(weddingspot_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (weddingspot_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])


st.markdown('--------------------------------------------------------------------')

# have a dropdown with all the budget line items I have models for
database_service_list = [
'RDS PostgreSQL',
#'RDS MySQL',
'Opensearch',
'ElastiCache',
'Redshift',
#'DynamoDB',
'Couchbase',
'Oracle',
'SQL Server']
database_service = st.selectbox('Choose a database service to see predictions',database_service_list)

#load in all the datasets
#RDS Postgres
Postgres = pd.read_csv('postgres_prophet_predictions1.csv')
Postgresvalues = []
for i in Postgres['yhat']:
    Postgresvalues.append("${:,.2f}".format(i))

Postgres[['yhat_vals']] = pd.DataFrame(Postgresvalues)
Postgres['Date'] = Postgres['ds']
Postgres['Predicted Value'] = Postgres['yhat_vals']
postgres_df = Postgres[['Date','Predicted Value']]
## do one for actual too

#RDS Mysql
# Mysql = pd.read_csv('mysql_prophet_predictions1.csv')
# Mysqlvalues = []
# for i in Mysql['yhat']:
#     Mysqlvalues.append("${:,.2f}".format(i))

# Mysql[['yhat_vals']] = pd.DataFrame(Mysqlvalues)
# Mysql['Date'] = Mysql['ds']
# Mysql['Predicted Value'] = Mysql['yhat_vals']
# mysql_df = Mysql[['Date','Predicted Value']]
## do one for actual too

#opensearch
Opensearch = pd.read_csv('opensearch_prophet_predictions1.csv')
Opensearchvalues = []
for i in Opensearch['yhat']:
    Opensearchvalues.append("${:,.2f}".format(i))

Opensearch[['yhat_vals']] = pd.DataFrame(Opensearchvalues)
Opensearch['Date'] = Opensearch['ds']
Opensearch['Predicted Value'] = Opensearch['yhat_vals']
opensearch_df = Opensearch[['Date','Predicted Value']]
## do one for actual too

#elasticache
Elasticache = pd.read_csv('elasticache_prophet_predictions1.csv')
Elasticachevalues = []
for i in Elasticache['yhat']:
    Elasticachevalues.append("${:,.2f}".format(i))

Elasticache[['yhat_vals']] = pd.DataFrame(Elasticachevalues)
Elasticache['Date'] = Elasticache['ds']
Elasticache['Predicted Value'] = Elasticache['yhat_vals']
elasticache_df = Elasticache[['Date','Predicted Value']]
## do one for actual too

#redshift
Redshift = pd.read_csv('redshift_prophet_predictions1.csv')
Redshiftvalues = []
for i in Redshift['yhat']:
    Redshiftvalues.append("${:,.2f}".format(i))

Redshift[['yhat_vals']] = pd.DataFrame(Redshiftvalues)
Redshift['Date'] = Redshift['ds']
Redshift['Predicted Value'] = Redshift['yhat_vals']
redshift_df = Redshift[['Date','Predicted Value']]
## do one for actual too

#dynamodb
# Dynamodb = pd.read_csv('dynamodb_prophet_predictions1.csv')
# Dynamodbvalues = []
# for i in Dynamodb['yhat']:
#     Dynamodbvalues.append("${:,.2f}".format(i))

# Dynamodb[['yhat_vals']] = pd.DataFrame(Dynamodbvalues)
# Dynamodb['Date'] = Dynamodb['ds']
# Dynamodb['Predicted Value'] = Dynamodb['yhat_vals']
# dynamodb_df = Dynamodb[['Date','Predicted Value']]
## do one for actual too

#couchbase
Couchbase = pd.read_csv('couchbase_prophet_predictions1.csv')
Couchbasevalues = []
for i in Couchbase['yhat']:
    Couchbasevalues.append("${:,.2f}".format(i))

Couchbase[['yhat_vals']] = pd.DataFrame(Couchbasevalues)
Couchbase['Date'] = Couchbase['ds']
Couchbase['Predicted Value'] = Couchbase['yhat_vals']
couchbase_df = Couchbase[['Date','Predicted Value']]
## do one for actual too

#oracle
Oracle = pd.read_csv('oracle_prophet_predictions1.csv')
Oraclevalues = []
for i in Oracle['yhat']:
    Oraclevalues.append("${:,.2f}".format(i))

Oracle[['yhat_vals']] = pd.DataFrame(Oraclevalues)
Oracle['Date'] = Oracle['ds']
Oracle['Predicted Value'] = Oracle['yhat_vals']
oracle_df = Oracle[['Date','Predicted Value']]
## do one for actual too

#sql server
SQLServer = pd.read_csv('sqlserver_prophet_predictions1.csv')
SQLServervalues = []
for i in SQLServer['yhat']:
    SQLServervalues.append("${:,.2f}".format(i))

SQLServer[['yhat_vals']] = pd.DataFrame(SQLServervalues)
SQLServer['Date'] = SQLServer['ds']
SQLServer['Predicted Value'] = SQLServer['yhat_vals']
sqlserver_df = SQLServer[['Date','Predicted Value']]
## do one for actual too
#not doing memorydb

#make varible to hold them

# have a table that updates dynamically with the model being displayed and the predictions for the next 3 months (rolling?)
    #Return Postgres df
if database_service == 'RDS PostgreSQL':
    database_service + " Costs"
    st.dataframe(postgres_df.loc[(postgres_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (postgres_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Mysql df
# elif database_service == 'RDS MySQL':
#     database_service + " Costs"
#     st.dataframe(mysql_df.loc[(mysql_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (mysql_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Opensearch df
elif database_service == 'Opensearch':
    database_service + " Costs"
    st.dataframe(opensearch_df.loc[(opensearch_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (opensearch_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Elasticache df
elif database_service == 'ElastiCache':
    database_service + " Costs"
    st.dataframe(elasticache_df.loc[(elasticache_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (elasticache_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Redshift df
elif database_service == 'Redshift':
    database_service + " Costs"
    st.dataframe(redshift_df.loc[(redshift_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (redshift_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Dynamodb df
# elif database_service == 'DynamoDB':
#     database_service + " Costs"
#     st.dataframe(dynamodb_df.loc[(dynamodb_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (dynamodb_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Couchbase df
elif database_service == 'Couchbase':
    database_service + " Costs"
    st.dataframe(couchbase_df.loc[(couchbase_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (couchbase_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Oracle df
elif database_service == 'Oracle':
    database_service + " Costs"
    st.dataframe(oracle_df.loc[(oracle_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (oracle_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))]) 
    #Return SQL Server df
elif database_service == 'SQL Server':
    database_service + " Costs"
    st.dataframe(sqlserver_df.loc[(sqlserver_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (sqlserver_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])