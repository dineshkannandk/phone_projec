

c={
    "success": True,
    "code": "SUCCESS",
    "data": {
        "from": 1514745000000,
        "to": 1522175400000,
        "transactionData": [
            {
                "name": "Recharge & bill payments",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 72550406,
                        "amount": 1.4472713558652578E10
                    }
                ]
            },
            {
                "name": "Peer-to-peer payments",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 46982705,
                        "amount": 1.4724588354277402E11
                    }
                ]
            },
            {
                "name": "Merchant payments",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 5368669,
                        "amount": 4.656678915140091E9
                    }
                ]
            },
            {
                "name": "Financial Services",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 3762820,
                        "amount": 8.158531051000277E8
                    }
                ]
            },
            {
                "name": "Others",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 5761576,
                        "amount": 4.643217301269438E9
                    }
                ]
            }
        ]
    },
    "responseTimestamp": 1630346628866
}

#Total Transactions of the country 2018_q1

import pandas as pd

def  total_trans_2018():

    Trans_name = []
    Trans_counts = []
    Trans_amounts=[]
     
    for i in range(0,len(c['data']['transactionData'])):

        name = c['data']['transactionData'][i]['name']
        count = c['data']['transactionData'][i]['paymentInstruments'][0]['count']
        amount=c['data']['transactionData'][i]['paymentInstruments'][0]['amount']
        Trans_name.append(name)
        Trans_counts.append(count)
        Trans_amounts.append(amount)


    
    df = pd.DataFrame(data=Trans_name)
    df.rename(columns={0:'Names'},inplace=True)
    df['Payments'] = Trans_counts
    df['Amounts']=Trans_amounts
    Total_Transactions = df
    #print("Total Transactions in India 2018")
    return    Total_Transactions


t=total_trans_2018()
#print(t)



#No of registered users

us={"success":True,"code":"SUCCESS","data":{"aggregated":{"registeredUsers":46877867,"appOpens":0},"usersByDevice":[{"brand":"Xiaomi","count":11926334,"percentage":0.25441289809538475},{"brand":"Samsung","count":9609401,"percentage":0.204988017052909},{"brand":"Vivo","count":5894293,"percentage":0.1257372269092363},{"brand":"Oppo","count":4479351,"percentage":0.09555364368434255},{"brand":"Realme","count":2376866,"percentage":0.05070337351313361},{"brand":"Apple","count":1825153,"percentage":0.03893421601285741},{"brand":"Motorola","count":1593250,"percentage":0.033987254582210406},{"brand":"OnePlus","count":1536418,"percentage":0.03277491273227086},{"brand":"Lenovo","count":1246507,"percentage":0.026590522986039446},{"brand":"Huawei","count":808774,"percentage":0.01725279010668297},{"brand":"Others","count":5581520,"percentage":0.1190651443249327}]},"responseTimestamp":1630501482414}

def users_2018():
    users_brand = []
    users_count = []
    for u in us['data']['usersByDevice']:
        p = (u['brand'])
        ur = (u['count'])
        users_brand.append((p))
        users_count.append(ur)

    df_user =pd.DataFrame(data=users_brand)
    df_user.rename(columns={0:'Brands'},inplace=True)
    df_user['count']=[i for i in users_count]
    #print('mobile users  2018')

    return  df_user

u=users_2018()
#print(u)










