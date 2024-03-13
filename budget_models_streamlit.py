#import stuff
import streamlit as st
import pandas as pd
from datetime  import datetime
import numpy as np

################################################
def data_prep(file_name):
    #replace column names
    file_name[['year']] = file_name[['year_number']]
    file_name[['month']] = file_name[['month_number']]
    file_name[['y']] = file_name[['cost']]
    
    #concat the month and year column and add an arbitrary day value (in this case the 1st of every date entry) 
    year_mon = []
    for i in range(len(file_name)):
        if len(file_name['month'][i].astype(str)) == 2:
            year_mon.append(file_name['year'][i].astype(str) + '-' + file_name['month'][i].astype(str) + '-01')
        else:
            year_mon.append(file_name['year'][i].astype(str) + '-0' + file_name['month'][i].astype(str) + '-01')
        
    year_mon = pd.DataFrame(year_mon, columns = ['dates'])
    file_name[['ds']] = year_mon

    #extract relevant columns
    file_name = file_name.loc[ : , ['ds','y']]

    #drop last value
    file_name = file_name.drop([len(file_name)-1]).reset_index()
    del file_name['index']

    return file_name
################################################



#put an image??
st.image('cvent_logo_rgb-®.png')

#put heading on the webpage
st.markdown("The predictions below are based off of the monthly costs for each of the AWS Budget line items owned by Mike Tiffany, as well as cost predictions for each of the database services. They are meant to act as a guide for each month's budget estimate; if you are a budget manager and know there will be changes that you think will increase or decrease the expected cost, please adjust this number accordingly.")
st.markdown("The numbers below will be updated with the predictions for the current month and the next 2 months before the 15th based on the costs from the last month. For now, this will be done manually, but in the next iterations of this dashboard the goal is to have it update automatically every month.")


st.header('AWS Budget line items')
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
BusinessTransient['yhat'] = BusinessTransient['yhat'].map(lambda i: "${:,.2f}".format(i))
BusinessTransient['Date'] = BusinessTransient['ds']
BusinessTransient['Predicted Value'] = BusinessTransient['yhat']
bt_app_df = BusinessTransient[['Date','Predicted Value']]
BusinessTransient.set_index("Date", inplace = True)

BTActual = pd.read_csv('costs_bt_app.csv')
BTActual = data_prep(BTActual)
BTActual['Actual Value'] = BTActual['y'].map(lambda i: "${:,.2f}".format(i))
BTActual.set_index("ds", inplace = True)

bt_app_preds_act = []
bt_app_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),BusinessTransient.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],BTActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
bt_app_preds_act = pd.DataFrame(bt_app_preds_act,columns=['Date','Predicted Value','Actual Value'])



#CSN
Conference = pd.read_csv('conference_prophet_predictions1.csv')
Conference['yhat'] = Conference['yhat'].map(lambda i: "${:,.2f}".format(i))
Conference['Date'] = Conference['ds']
Conference['Predicted Value'] = Conference['yhat']
conference_df = Conference[['Date','Predicted Value']]
Conference.set_index("Date", inplace = True)

ConferenceActual = pd.read_csv('costs_conference.csv')
ConferenceActual = data_prep(ConferenceActual)
ConferenceActual['Actual Value'] = ConferenceActual['y'].map(lambda i: "${:,.2f}".format(i))
ConferenceActual.set_index("ds", inplace = True)

conference_preds_act = []
conference_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Conference.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],ConferenceActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
conference_preds_act = pd.DataFrame(conference_preds_act,columns=['Date','Predicted Value','Actual Value'])



Corporate_Systems = pd.read_csv('corporate_systems_prophet_predictions1.csv')
Corporate_Systems['yhat'] = Corporate_Systems['yhat'].map(lambda i: "${:,.2f}".format(i))
Corporate_Systems['Date'] = Corporate_Systems['ds']
Corporate_Systems['Predicted Value'] = Corporate_Systems['yhat']
corporate_systems_df = Corporate_Systems[['Date','Predicted Value']]
Corporate_Systems.set_index("ds", inplace = True)

Corporate_SystemsActual = pd.read_csv('costs_corporate_systems.csv')
Corporate_SystemsActual = data_prep(Corporate_SystemsActual)
Corporate_SystemsActual['Actual Value'] = Corporate_SystemsActual['y'].map(lambda i: "${:,.2f}".format(i))
Corporate_SystemsActual.set_index("ds", inplace = True)

corporate_systems_preds_act = []
corporate_systems_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Corporate_Systems.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Corporate_SystemsActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
corporate_systems_preds_act = pd.DataFrame(corporate_systems_preds_act,columns=['Date','Predicted Value','Actual Value'])



EMCouch = pd.read_csv('em_couch_prophet_predictions1.csv')
EMCouch['yhat'] = EMCouch['yhat'].map(lambda i: "${:,.2f}".format(i))
EMCouch['Date'] = EMCouch['ds']
EMCouch['Predicted Value'] = EMCouch['yhat']
em_couch_df = EMCouch[['Date','Predicted Value']]
EMCouch.set_index("ds", inplace = True)

EMCouchActual = pd.read_csv('costs_em_couchbase.csv')
EMCouchActual = data_prep(EMCouchActual)
EMCouchActual['Actual Value'] = EMCouchActual['y'].map(lambda i: "${:,.2f}".format(i))
EMCouchActual.set_index("ds", inplace = True)

em_couch_preds_act = []
em_couch_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),EMCouch.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],EMCouchActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
em_couch_preds_act = pd.DataFrame(em_couch_preds_act,columns=['Date','Predicted Value','Actual Value'])



Oracle_Financials = pd.read_csv('oracle_financials_prophet_predictions1.csv')
Oracle_Financials['yhat'] = Oracle_Financials['yhat'].map(lambda i: "${:,.2f}".format(i))
Oracle_Financials['Date'] = Oracle_Financials['ds']
Oracle_Financials['Predicted Value'] = Oracle_Financials['yhat']
oracle_financials_df = Oracle_Financials[['Date','Predicted Value']]
Oracle_Financials.set_index("ds", inplace = True)

Oracle_FinancialsActual = pd.read_csv('costs_oracle_financials.csv')
Oracle_FinancialsActual = data_prep(Oracle_FinancialsActual)
Oracle_FinancialsActual['Actual Value'] = Oracle_FinancialsActual['y'].map(lambda i: "${:,.2f}".format(i))
Oracle_FinancialsActual.set_index("ds", inplace = True)

orc_fin_preds_act = []
orc_fin_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Oracle_Financials.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Oracle_FinancialsActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
orc_fin_preds_act = pd.DataFrame(orc_fin_preds_act,columns=['Date','Predicted Value','Actual Value'])



Passkey = pd.read_csv('passkey_prophet_predictions1.csv')
Passkey['yhat'] = Passkey['yhat'].map(lambda i: "${:,.2f}".format(i))
Passkey['Date'] = Passkey['ds']
Passkey['Predicted Value'] = Passkey['yhat']
passkey_df = Passkey[['Date','Predicted Value']]
Passkey.set_index("ds", inplace = True)

PasskeyActual = pd.read_csv('costs_passkey.csv')
PasskeyActual = data_prep(PasskeyActual)
PasskeyActual['Actual Value'] = PasskeyActual['y'].map(lambda i: "${:,.2f}".format(i))
PasskeyActual.set_index("ds", inplace = True)

passkey_preds_act = []
passkey_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Passkey.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],PasskeyActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
passkey_preds_act = pd.DataFrame(passkey_preds_act,columns=['Date','Predicted Value','Actual Value'])



Data_Retention = pd.read_csv('data_retention_prophet_predictions1.csv')
Data_Retention['yhat'] = Data_Retention['yhat'].map(lambda i: "${:,.2f}".format(i))
Data_Retention['Date'] = Data_Retention['ds']
Data_Retention['Predicted Value'] = Data_Retention['yhat']
data_retention_df = Data_Retention[['Date','Predicted Value']]
Data_Retention.set_index("ds", inplace = True)

Data_RetentionActual = pd.read_csv('costs_data_retention.csv')
Data_RetentionActual = data_prep(Data_RetentionActual)
Data_RetentionActual['Actual Value'] = Data_RetentionActual['y'].map(lambda i: "${:,.2f}".format(i))
Data_RetentionActual.set_index("ds", inplace = True)

dat_ret_preds_act = []
dat_ret_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Data_Retention.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Data_RetentionActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
dat_ret_preds_act = pd.DataFrame(dat_ret_preds_act,columns=['Date','Predicted Value','Actual Value'])



#Shared_Couchbase = pd.read_csv('shared_couchbase_prophet_predictions.csv')
Shared_DynamoDB = pd.read_csv('shared_dynamodb_prophet_predictions1.csv')
Shared_DynamoDB['yhat'] = Shared_DynamoDB['yhat'].map(lambda i: "${:,.2f}".format(i))
Shared_DynamoDB['Date'] = Shared_DynamoDB['ds']
Shared_DynamoDB['Predicted Value'] = Shared_DynamoDB['yhat']
shared_dynamodb_df = Shared_DynamoDB[['Date','Predicted Value']]
Shared_DynamoDB.set_index("ds", inplace = True)

Shared_DynamoDBActual = pd.read_csv('costs_shared_dynamodb.csv')
Shared_DynamoDBActual = data_prep(Shared_DynamoDBActual)
Shared_DynamoDBActual['Actual Value'] = Shared_DynamoDBActual['y'].map(lambda i: "${:,.2f}".format(i))
Shared_DynamoDBActual.set_index("ds", inplace = True)

shared_dynamo_preds_act = []
shared_dynamo_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Shared_DynamoDB.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Shared_DynamoDBActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
shared_dynamo_preds_act = pd.DataFrame(shared_dynamo_preds_act,columns=['Date','Predicted Value','Actual Value'])



Shared_RDS = pd.read_csv('shared_rds_prophet_predictions1.csv')
Shared_RDS['yhat'] = Shared_RDS['yhat'].map(lambda i: "${:,.2f}".format(i))
Shared_RDS['Date'] = Shared_RDS['ds']
Shared_RDS['Predicted Value'] = Shared_RDS['yhat']
shared_rds_df = Shared_RDS[['Date','Predicted Value']]
Shared_RDS.set_index("ds", inplace = True)

Shared_RDSActual = pd.read_csv('costs_shared_rds.csv')
Shared_RDSActual = data_prep(Shared_RDSActual)
Shared_RDSActual['Actual Value'] = Shared_RDSActual['y'].map(lambda i: "${:,.2f}".format(i))
Shared_RDSActual.set_index("ds", inplace = True)

shared_rds_preds_act = []
shared_rds_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Shared_RDS.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Shared_RDSActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
shared_rds_preds_act = pd.DataFrame(shared_rds_preds_act,columns=['Date','Predicted Value','Actual Value'])



Shared_SQL_Server = pd.read_csv('shared_sqlserver_prophet_predictions1.csv')
Shared_SQL_Server['yhat'] = Shared_SQL_Server['yhat'].map(lambda i: "${:,.2f}".format(i))
Shared_SQL_Server['Date'] = Shared_SQL_Server['ds']
Shared_SQL_Server['Predicted Value'] = Shared_SQL_Server['yhat']
shared_sql_server_df = Shared_SQL_Server[['Date','Predicted Value']]
Shared_SQL_Server.set_index("ds", inplace = True)

Shared_SQL_ServerActual = pd.read_csv('costs_shared_sql_server.csv')
Shared_SQL_ServerActual = data_prep(Shared_SQL_ServerActual)
Shared_SQL_ServerActual['Actual Value'] = Shared_SQL_ServerActual['y'].map(lambda i: "${:,.2f}".format(i))
Shared_SQL_ServerActual.set_index("ds", inplace = True)

shared_sql_preds_act = []
shared_sql_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Shared_SQL_Server.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Shared_SQL_ServerActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
shared_sql_preds_act = pd.DataFrame(shared_sql_preds_act,columns=['Date','Predicted Value','Actual Value'])



Social_Tables = pd.read_csv('socialtables_prophet_predictions1.csv')
Social_Tables['yhat'] = Social_Tables['yhat'].map(lambda i: "${:,.2f}".format(i))
Social_Tables['Date'] = Social_Tables['ds']
Social_Tables['Predicted Value'] = Social_Tables['yhat']
socialtables_df = Social_Tables[['Date','Predicted Value']]
Social_Tables.set_index("ds", inplace = True)

Social_TablesActual = pd.read_csv('costs_socialtables.csv')
Social_TablesActual = data_prep(Social_TablesActual)
Social_TablesActual['Actual Value'] = Social_TablesActual['y'].map(lambda i: "${:,.2f}".format(i))
Social_TablesActual.set_index("ds", inplace = True)

soc_tabs_preds_act = []
soc_tabs_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Social_Tables.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Social_TablesActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
soc_tabs_preds_act = pd.DataFrame(soc_tabs_preds_act,columns=['Date','Predicted Value','Actual Value'])



SpeedRFP = pd.read_csv('speedrfp_prophet_predictions1.csv')
SpeedRFP['yhat'] = SpeedRFP['yhat'].map(lambda i: "${:,.2f}".format(i))
SpeedRFP['Date'] = SpeedRFP['ds']
SpeedRFP['Predicted Value'] = SpeedRFP['yhat']
speedrfp_df = SpeedRFP[['Date','Predicted Value']]
SpeedRFP.set_index("ds", inplace = True)

SpeedRFPActual = pd.read_csv('costs_speedrfp.csv')
SpeedRFPActual = data_prep(SpeedRFPActual)
SpeedRFPActual['Actual Value'] = SpeedRFPActual['y'].map(lambda i: "${:,.2f}".format(i))
SpeedRFPActual.set_index("ds", inplace = True)

speedrfp_preds_act = []
speedrfp_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),SpeedRFP.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],SpeedRFPActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
speedrfp_preds_act = pd.DataFrame(speedrfp_preds_act,columns=['Date','Predicted Value','Actual Value'])



Wedding_Spot = pd.read_csv('weddingspot_prophet_predictions1.csv')
Wedding_Spot['yhat'] = Wedding_Spot['yhat'].map(lambda i: "${:,.2f}".format(np.absolute(i)))
Wedding_Spot['Date'] = Wedding_Spot['ds']
Wedding_Spot['Predicted Value'] = Wedding_Spot['yhat']
weddingspot_df = Wedding_Spot[['Date','Predicted Value']]
Wedding_Spot.set_index("ds", inplace = True)

Wedding_SpotActual = pd.read_csv('costs_weddingspot.csv')
Wedding_SpotActual = data_prep(Wedding_SpotActual)
Wedding_SpotActual['Actual Value'] = Wedding_SpotActual['y'].map(lambda i: "${:,.2f}".format(i))
Wedding_SpotActual.set_index("ds", inplace = True)

wedd_spot_preds_act = []
wedd_spot_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Wedding_Spot.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],Wedding_SpotActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
wedd_spot_preds_act = pd.DataFrame(wedd_spot_preds_act,columns=['Date','Predicted Value','Actual Value'])


#make varible to hold them

# have a table that updates dynamically with the model being displayed and the predictions for the next 3 months (rolling?)
#Passkey['ds'][5:7] == datetime.now().strftime("%m")
#Passkey['ds'][10][5:7]
    #Return Conference df
if line_item == 'Business Transient - App':
    line_item + " Costs"
    st.dataframe(bt_app_df.loc[(bt_app_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (bt_app_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(bt_app_preds_act)
    #Return Conference df
elif line_item == 'Conference':
    line_item + " Costs"
    st.dataframe(conference_df.loc[(conference_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (conference_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(conference_preds_act)
    #Return Corporate Services df
elif line_item == 'Corporate Systems':
    line_item + " Costs"
    st.dataframe(corporate_systems_df.loc[(corporate_systems_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (corporate_systems_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(corporate_systems_preds_act)
    #Return EM Couch df
elif line_item == 'Event Management - Couchbase':
    line_item + " Costs"
    st.dataframe(em_couch_df.loc[(em_couch_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (em_couch_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(em_couch_preds_act)
    #Return Oracle Financials df
elif line_item == 'Oracle Financials':
    line_item + " Costs"
    st.dataframe(oracle_financials_df.loc[(oracle_financials_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (oracle_financials_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(orc_fin_preds_act)
    #Return Passkey df
elif line_item == 'Passkey':
    line_item + " Costs"
    st.dataframe(passkey_df.loc[(passkey_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (passkey_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(passkey_preds_act)
    #Return Data Retention df
elif line_item == 'Data Retention':
    line_item + " Costs"
    st.dataframe(data_retention_df.loc[(data_retention_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (data_retention_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))]) 
    "Predictions vs Actual for the previous month"
    st.dataframe(dat_ret_preds_act)
    #Return Shared RDS df
elif line_item == 'Shared RDS':
    line_item + " Costs"
    st.dataframe(shared_rds_df.loc[(shared_rds_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (shared_rds_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(shared_rds_preds_act)
    #Return Shared DynamoDB df
elif line_item == 'Shared DynamoDB':
    line_item + " Costs"
    st.dataframe(shared_dynamodb_df.loc[(shared_dynamodb_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (shared_dynamodb_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(shared_dynamo_preds_act)
    #Return Shared SQL Server df
elif line_item == 'Shared SQL Server':
    line_item + " Costs"
    st.dataframe(shared_sql_server_df.loc[(shared_sql_server_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (shared_sql_server_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(shared_sql_preds_act)
    #Return Social Tables df
elif line_item == 'Social Tables':
    line_item + " Costs"
    st.dataframe(socialtables_df.loc[(socialtables_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (socialtables_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(soc_tabs_preds_act)
    #Return Speed RFP df
elif line_item == 'Speed RFP':
    line_item + " Costs"
    st.dataframe(speedrfp_df.loc[(speedrfp_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (speedrfp_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(speedrfp_preds_act)
    #Return Wedding Spot df
elif line_item == 'Wedding Spot':
    line_item + " Costs"
    st.dataframe(weddingspot_df.loc[(weddingspot_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (weddingspot_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(wedd_spot_preds_act)

st.markdown('--------------------------------------------------------------------')
st.header('Database Services')

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
Postgres['yhat'] = Postgres['yhat'].map(lambda i: "${:,.2f}".format(i))
Postgres['Date'] = Postgres['ds']
Postgres['Predicted Value'] = Postgres['yhat']
postgres_df = Postgres[['Date','Predicted Value']]
Postgres.set_index("ds", inplace = True)

PostgresActual = pd.read_csv('costs_postgres.csv')
PostgresActual = data_prep(PostgresActual)
PostgresActual['Actual Value'] = PostgresActual['y'].map(lambda i: "${:,.2f}".format(i))
PostgresActual.set_index("ds", inplace = True)

postgres_preds_act = []
postgres_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Postgres.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],PostgresActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
postgres_preds_act = pd.DataFrame(postgres_preds_act,columns=['Date','Predicted Value','Actual Value'])



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
Opensearch['yhat'] = Opensearch['yhat'].map(lambda i: "${:,.2f}".format(i))
Opensearch['Date'] = Opensearch['ds']
Opensearch['Predicted Value'] = Opensearch['yhat']
opensearch_df = Opensearch[['Date','Predicted Value']]
Opensearch.set_index("ds", inplace = True)

OpensearchActual = pd.read_csv('costs_es.csv')
OpensearchActual = data_prep(OpensearchActual)
OpensearchActual['Actual Value'] = OpensearchActual['y'].map(lambda i: "${:,.2f}".format(i))
OpensearchActual.set_index("ds", inplace = True)

opensearch_preds_act = []
opensearch_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Opensearch.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],OpensearchActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
opensearch_preds_act = pd.DataFrame(opensearch_preds_act,columns=['Date','Predicted Value','Actual Value'])



#elasticache
Elasticache = pd.read_csv('elasticache_prophet_predictions1.csv')
Elasticache['yhat'] = Elasticache['yhat'].map(lambda i: "${:,.2f}".format(i))
Elasticache['Date'] = Elasticache['ds']
Elasticache['Predicted Value'] = Elasticache['yhat']
elasticache_df = Elasticache[['Date','Predicted Value']]
Elasticache.set_index("ds", inplace = True)

ElasticacheActual = pd.read_csv('costs_elasticache.csv')
ElasticacheActual = data_prep(ElasticacheActual)
ElasticacheActual['Actual Value'] = ElasticacheActual['y'].map(lambda i: "${:,.2f}".format(i))
ElasticacheActual.set_index("ds", inplace = True)

elasticache_preds_act = []
elasticache_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Elasticache.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],ElasticacheActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
elasticache_preds_act = pd.DataFrame(elasticache_preds_act,columns=['Date','Predicted Value','Actual Value'])



#redshift
Redshift = pd.read_csv('redshift_prophet_predictions1.csv')
Redshift['yhat'] = Redshift['yhat'].map(lambda i: "${:,.2f}".format(i))
Redshift['Date'] = Redshift['ds']
Redshift['Predicted Value'] = Redshift['yhat']
redshift_df = Redshift[['Date','Predicted Value']]
Redshift.set_index("ds", inplace = True)

RedshiftActual = pd.read_csv('costs_redshift.csv')
RedshiftActual = data_prep(RedshiftActual)
RedshiftActual['Actual Value'] = RedshiftActual['y'].map(lambda i: "${:,.2f}".format(i))
RedshiftActual.set_index("ds", inplace = True)

redshift_preds_act = []
redshift_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Redshift.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],RedshiftActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
redshift_preds_act = pd.DataFrame(redshift_preds_act,columns=['Date','Predicted Value','Actual Value'])

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
Couchbase['yhat'] = Couchbase['yhat'].map(lambda i: "${:,.2f}".format(i))
Couchbase['Date'] = Couchbase['ds']
Couchbase['Predicted Value'] = Couchbase['yhat']
couchbase_df = Couchbase[['Date','Predicted Value']]
Couchbase.set_index("ds", inplace = True)

CouchbaseActual = pd.read_csv('costs_couchbase.csv')
CouchbaseActual = data_prep(CouchbaseActual)
CouchbaseActual['Actual Value'] = CouchbaseActual['y'].map(lambda i: "${:,.2f}".format(i))
CouchbaseActual.set_index("ds", inplace = True)

couchbase_preds_act = []
couchbase_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Couchbase.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],CouchbaseActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
couchbase_preds_act = pd.DataFrame(couchbase_preds_act,columns=['Date','Predicted Value','Actual Value'])



#oracle
Oracle = pd.read_csv('oracle_prophet_predictions1.csv')
Oracle['yhat'] = Oracle['yhat'].map(lambda i: "${:,.2f}".format(i))
Oracle['Date'] = Oracle['ds']
Oracle['Predicted Value'] = Oracle['yhat']
oracle_df = Oracle[['Date','Predicted Value']]
Oracle.set_index("ds", inplace = True)

OracleActual = pd.read_csv('costs_oracle.csv')
OracleActual = data_prep(OracleActual)
OracleActual['Actual Value'] = OracleActual['y'].map(lambda i: "${:,.2f}".format(i))
OracleActual.set_index("ds", inplace = True)

oracle_preds_act = []
oracle_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),Oracle.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],OracleActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
oracle_preds_act = pd.DataFrame(oracle_preds_act,columns=['Date','Predicted Value','Actual Value'])



#sql server
SQLServer = pd.read_csv('sqlserver_prophet_predictions1.csv')
SQLServer['yhat'] = SQLServer['yhat'].map(lambda i: "${:,.2f}".format(i))
SQLServer['Date'] = SQLServer['ds']
SQLServer['Predicted Value'] = SQLServer['yhat']
sqlserver_df = SQLServer[['Date','Predicted Value']]
SQLServer.set_index("ds", inplace = True)

SQLServerActual = pd.read_csv('costs_sql_server.csv')
SQLServerActual = data_prep(SQLServerActual)
SQLServerActual['Actual Value'] = SQLServerActual['y'].map(lambda i: "${:,.2f}".format(i))
SQLServerActual.set_index("ds", inplace = True)

sqlserver_preds_act = []
sqlserver_preds_act.append([datetime.now().replace(month=int(datetime.now().month)-1).strftime("%Y-%m"),SQLServer.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['yhat'],SQLServerActual.loc[datetime.now().replace(month=int(datetime.now().month)-1,day=1).strftime("%Y-%m-%d")]['Actual Value']])
sqlserver_preds_act = pd.DataFrame(sqlserver_preds_act,columns=['Date','Predicted Value','Actual Value'])
#not doing memorydb


#make varible to hold them

# have a table that updates dynamically with the model being displayed and the predictions for the next 3 months (rolling?)
    #Return Postgres df
if database_service == 'RDS PostgreSQL':
    database_service + " Costs"
    st.dataframe(postgres_df.loc[(postgres_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (postgres_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(postgres_preds_act)
    #Return Mysql df
# elif database_service == 'RDS MySQL':
#     database_service + " Costs"
#     st.dataframe(mysql_df.loc[(mysql_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (mysql_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Elasticache df
elif database_service == 'Opensearch':
    database_service + " Costs"
    st.dataframe(opensearch_df.loc[(opensearch_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (opensearch_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(opensearch_preds_act)
    #Return Elasticache df
elif database_service == 'ElastiCache':
    database_service + " Costs"
    st.dataframe(elasticache_df.loc[(elasticache_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (elasticache_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(elasticache_preds_act)
    #Return Redshift df
elif database_service == 'Redshift':
    database_service + " Costs"
    st.dataframe(redshift_df.loc[(redshift_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (redshift_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(redshift_preds_act)
    #Return Dynamodb df
# elif database_service == 'DynamoDB':
#     database_service + " Costs"
#     st.dataframe(dynamodb_df.loc[(dynamodb_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (dynamodb_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    #Return Couchbase df
elif database_service == 'Couchbase':
    database_service + " Costs"
    st.dataframe(couchbase_df.loc[(couchbase_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (couchbase_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(couchbase_preds_act)
    #Return Oracle df
elif database_service == 'Oracle':
    database_service + " Costs"
    st.dataframe(oracle_df.loc[(oracle_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (oracle_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))]) 
    "Predictions vs Actual for the previous month"
    st.dataframe(oracle_preds_act)
    #Return SQL Server df
elif database_service == 'SQL Server':
    database_service + " Costs"
    st.dataframe(sqlserver_df.loc[(sqlserver_df['Date']>=datetime.now().strftime("%Y-%m-%d")) & (sqlserver_df['Date']<=datetime.now().replace(month=(int(datetime.now().month)+3)).strftime("%Y-%m-%d"))])
    "Predictions vs Actual for the previous month"
    st.dataframe(sqlserver_preds_act)