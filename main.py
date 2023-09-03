from country import *
from state import *
from distict import *

import pandas as pd
import mysql.connector
import  streamlit as st
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go

import json
indian_state = json.load(open("./india_state_geo.json",'r'))

st.set_page_config(page_title="Phonepe",
                   page_icon='📲')

st.title("PhonePe Transaction Data Visualization")

  

#Total Transaction
users_2018=users_2018()
total_Transaction_2018=total_trans_2018()

#state
state_2018=for_state()

#city
city_2018=capital()
cit_2018=city()



mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='1234',
    database='project'
)
 
cursor=mydb.cursor()
print('connection established')



engine = create_engine("mysql+mysqldb://root:1234@127.0.0.1:3306/project")

conn=engine.connect()

Trans=pd.DataFrame(data=total_Transaction_2018)
Users=pd.DataFrame(data=users_2018)
state=pd.DataFrame(data=state_2018)
District=pd.DataFrame(data=city_2018)
citi=pd.DataFrame(data=cit_2018)

# storing the data in mysql
Trans.to_sql('transactions',engine,index=False,if_exists='replace')
Users.to_sql('user',engine,index=False,if_exists='replace')
state.to_sql('states',engine,index=False,if_exists='replace')
District.to_sql('districts',engine,index=False,if_exists='replace')
citi.to_sql('city',engine,index=False,if_exists='replace')

# importing data from mysql
read = "select * from transactions" 
r_user = "select * from user" 
r_states = "select * from states" 
r_districts = "select * from districts" 
r_city = "select * from city" 


r_Transaction = pd.read_sql(read, conn)
r_user = pd.read_sql(r_user, conn)
r_states = pd.read_sql(r_states, conn)
r_districts = pd.read_sql(r_districts, conn)
r_city = pd.read_sql(r_city, conn)



conn.commit()
#print('Data inserted sucessfully')
#print(r_Transaction)
#print(r_user)
#print(r_states)
#print(r_districts)
#print(r_city)




fig1=px.bar(r_Transaction , x='Names',y='Payments',color='Amounts',title='Total Transactions of the India')

fig2=px.bar(r_user , x='Brands',y='count',title='Mobile',barmode='group')

names=[]
for i in indian_state['features']:
    name=i['properties']['NAME_1']
    names.append(name) 

na=[]
for n in names:
    if n == r_states['States']:
        na.append(n)

fig=px.choropleth(
      r_states,
      geojson=indian_state,
      locations=na,
      color=['count','Amount'],
      scope='asia')

fig.update_geos(fitbonds='locations',visible=False)

 

st.plotly_chart(fig)

options= st.sidebar._selectbox('select the following',["Total_Transactions","Mobile_users"])


if options == "Total_Transactions":
    st.subheader(
        st.plotly_chart(fig1)
    )
    
elif options == 'Mobile_users':
    st.subheader(st.plotly_chart(fig2))












    


    
    










