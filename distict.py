import pandas  as pd
d={"success":True,"code":"SUCCESS","data":{"states":[{"entityName":"maharashtra","metric":{"type":"TOTAL","count":16387034,"amount":2.1711613257725674E10}},{"entityName":"uttar pradesh","metric":{"type":"TOTAL","count":12537805,"amount":1.3939970923223106E10}},{"entityName":"karnataka","metric":{"type":"TOTAL","count":12016899,"amount":1.9217895314012802E10}},{"entityName":"west bengal","metric":{"type":"TOTAL","count":11710225,"amount":1.0625978552140453E10}},{"entityName":"andhra pradesh","metric":{"type":"TOTAL","count":9039585,"amount":1.1996276391823706E10}},{"entityName":"telangana","metric":{"type":"TOTAL","count":8522766,"amount":1.3308204118542435E10}},{"entityName":"madhya pradesh","metric":{"type":"TOTAL","count":8025395,"amount":8.681603403446348E9}},{"entityName":"rajasthan","metric":{"type":"TOTAL","count":7591690,"amount":8.92629313072684E9}},{"entityName":"delhi","metric":{"type":"TOTAL","count":7122754,"amount":1.121150380691996E10}},{"entityName":"tamil nadu","metric":{"type":"TOTAL","count":6726622,"amount":1.1261557697516891E10}}],"districts":[{"entityName":"bengaluru urban","metric":{"type":"TOTAL","count":8306513,"amount":1.416275030306484E10}},{"entityName":"pune","metric":{"type":"TOTAL","count":3842929,"amount":5.378982326835919E9}},{"entityName":"central delhi","metric":{"type":"TOTAL","count":2997714,"amount":4.312145216274474E9}},{"entityName":"mumbai","metric":{"type":"TOTAL","count":2671029,"amount":3.923116793952079E9}},{"entityName":"chennai","metric":{"type":"TOTAL","count":2656230,"amount":4.281137762522443E9}},{"entityName":"hyderabad","metric":{"type":"TOTAL","count":2545507,"amount":4.28722378976588E9}},{"entityName":"jaipur","metric":{"type":"TOTAL","count":2417174,"amount":2.9530869601413727E9}},{"entityName":"birbhum","metric":{"type":"TOTAL","count":2125816,"amount":2.520486412452376E9}},{"entityName":"kolkata","metric":{"type":"TOTAL","count":2043129,"amount":2.7533476601429114E9}},{"entityName":"bhopal","metric":{"type":"TOTAL","count":1704495,"amount":1.9054738748326716E9}}],"pincodes":[{"entityName":"560001","metric":{"type":"TOTAL","count":2917356,"amount":4.684262246184548E9}},{"entityName":"110006","metric":{"type":"TOTAL","count":2636324,"amount":3.714139312238586E9}},{"entityName":"400008","metric":{"type":"TOTAL","count":2227885,"amount":3.105208723475169E9}},{"entityName":"600003","metric":{"type":"TOTAL","count":2010196,"amount":2.997847000265506E9}},{"entityName":"731101","metric":{"type":"TOTAL","count":1764956,"amount":2.3667712857278423E9}},{"entityName":"700009","metric":{"type":"TOTAL","count":1390629,"amount":1.8511453744001179E9}},{"entityName":"411001","metric":{"type":"TOTAL","count":1055656,"amount":1.4135236055956619E9}},{"entityName":"500012","metric":{"type":"TOTAL","count":933013,"amount":1.6430619764262943E9}},{"entityName":"462001","metric":{"type":"TOTAL","count":832846,"amount":8.98730606684653E8}},{"entityName":"201301","metric":{"type":"TOTAL","count":690196,"amount":9.876134389540119E8}}]},"responseTimestamp":1630501481910}


def capital():
    names=[]
    counts=[]
    amounts=[]

    for i in range(0,10):
        name = d['data']['states'][i]['entityName']
        count = d['data']['states'][i]['metric']['count']
        amount = d['data']['states'][i]['metric']['amount']
        names.append(name)
        counts.append(count)
        amounts.append(amount)

    captials=pd.DataFrame(names)
    captials['Count']=counts
    captials['Amount']=amounts
    captials.rename(columns={0:'Names'},inplace=True)
    #print('district wise Transaction')
    return captials

c=capital()
#print(c)


c={"success":True,"code":"SUCCESS","data":{"states":[{"name":"maharashtra","registeredUsers":6106994},{"name":"uttar pradesh","registeredUsers":4694250},{"name":"karnataka","registeredUsers":3717763},{"name":"andhra pradesh","registeredUsers":3336450},{"name":"telangana","registeredUsers":3315560},{"name":"rajasthan","registeredUsers":3158202},{"name":"gujarat","registeredUsers":2690048},{"name":"west bengal","registeredUsers":2604789},{"name":"madhya pradesh","registeredUsers":2553603},{"name":"bihar","registeredUsers":2133804}],"districts":[{"name":"bengaluru urban","registeredUsers":1922368},{"name":"pune","registeredUsers":1211643},{"name":"jaipur","registeredUsers":900773},{"name":"mumbai suburban","registeredUsers":719300},{"name":"hyderabad","registeredUsers":655175},{"name":"rangareddy","registeredUsers":635175},{"name":"thane","registeredUsers":631864},{"name":"ahmadabad","registeredUsers":572811},{"name":"medchal malkajgiri","registeredUsers":549429},{"name":"visakhapatnam","registeredUsers":497187}],"pincodes":[{"name":"201301","registeredUsers":114625},{"name":"500072","registeredUsers":105012},{"name":"560068","registeredUsers":98487},{"name":"110059","registeredUsers":95496},{"name":"110092","registeredUsers":83600},{"name":"122001","registeredUsers":82656},{"name":"560037","registeredUsers":75304},{"name":"395006","registeredUsers":72275},{"name":"800001","registeredUsers":71092},{"name":"302012","registeredUsers":68098}]},"responseTimestamp":1630501482414}


def city():
    names=[]
    users=[]
    for i in range(0,10):
         name=c['data']['states'][i]['name']
         user=c['data']['states'][i]['registeredUsers']
         names.append(name)
         users.append(user)
    
    cities=pd.DataFrame(names)
    cities['users']=users
    cities.rename(columns={0:'Names'},inplace=True)
    #print('city wise Transaction')
    return cities

p=city()

#print(p)
