# Q.1 Use the Google Trends API to retrieve 3 years of data from 5 different keywords 
# and deliver the data to Cloud Storage.

########### Importing Necessary Libraries  ####################

import pandas as pd 
import matplotlib.dates as mdates
import matplotlib.gridspec as grid_spec
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import plotly.express as px
import csv
import io
import json
import os
import google.cloud.logging
import plotly.express as px
from pandas.testing import assert_frame_equal                      
from pytrends.request import TrendReq
pytrend = TrendReq(hl='en-US', geo= 'GER')
from pytrends.request import TrendReq
plt.style.use('bmh')
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from datetime import date
from IPython.display import display
from google.cloud import storage


########################## PACKAGES RETRIEVED ##################################
#pytrend = TrendReq()

KEYWORDS=['machine learning','covid','Donald Trump','Apple','Merkel'] 
KEYWORDS_CODES=[pytrend.suggestions(keyword=i)[0] for i in KEYWORDS] 
df_CODES= pd.DataFrame(KEYWORDS_CODES)
df_CODES

EXACT_KEYWORDS=df_CODES['mid'].to_list()
DATE_INTERVAL='2019-07-20 2022-07-20'
COUNTRY=["US","DE"]
CATEGORY=0 
SEARCH_TYPE='youtube' # We can take in News, Youtube, Gerneral search for the SEARCH_TYPE

Individual_EXACT_KEYWORD = list(zip(*[iter(EXACT_KEYWORDS)]*1))
Individual_EXACT_KEYWORD = [list(x) for x in Individual_EXACT_KEYWORD]
dicti= {}
i = 1
for Country in COUNTRY:
    for keyword in Individual_EXACT_KEYWORD:
        pytrend.build_payload(kw_list=keyword, 
                              timeframe = DATE_INTERVAL, 
                              geo = Country, 
                              cat=CATEGORY,
                              gprop=SEARCH_TYPE) 
        dicti[i] = pytrend.interest_over_time()
        i+=1
df_trends = pd.concat(dicti, axis=1)

df_trends.columns = df_trends.columns.droplevel(0) #drop outside header
df_trends = df_trends.drop('isPartial', axis = 1) #drop "isPartial"
df_trends.reset_index(level=0,inplace=True) #reset_index
df_trends.columns=['date','Machine learning-US','covid-US','Donald Trump-US','Apple-US','Merkel-US',
'Machine learning-Germany','covid-Germany','Donald Trump-Germany','Apple-Germany','Merkel-Germany'] 

df_trends.head(10)
# Note: Values for Covid-US and Covid-Germany is 0 because covid became popular in Jan 2020.


fig = px.line(df_trends, x="date", y= ['Machine learning-US','Machine learning-Germany','covid-US',
                                       'covid-Germany'], 
              title='Keywords Comparison Over Time and Region')
fig.show() 

df_trends.to_csv('df_trends.csv', sep=',', encoding='utf-8', index=False)
plt.savefig('keywords.png')

credential_path = "integral-tensor-307421-01d7f5c42a18.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

storage_client=storage.Client()

bucket = storage_client.get_bucket("code_test-bucket")
filename = "%s/%s" % ('','df_trends.csv')
blob=bucket.blob(filename)
blob.upload_from_filename('df_trends.csv')
