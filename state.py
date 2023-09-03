import pandas as pd

m={"success":True,"code":"SUCCESS","data":{"hoverDataList":[{"name":"puducherry","metric":[{"type":"TOTAL","count":104212,"amount":1.6582597136983618E8}]},{"name":"tamil nadu","metric":[{"type":"TOTAL","count":6726622,"amount":1.1261557697516891E10}]},{"name":"uttar pradesh","metric":[{"type":"TOTAL","count":12537805,"amount":1.3939970923223106E10}]},{"name":"madhya pradesh","metric":[{"type":"TOTAL","count":8025395,"amount":8.681603403446348E9}]},{"name":"andhra pradesh","metric":[{"type":"TOTAL","count":9039585,"amount":1.1996276391823706E10}]},{"name":"tripura","metric":[{"type":"TOTAL","count":148157,"amount":1.3797891453062224E8}]},{"name":"lakshadweep","metric":[{"type":"TOTAL","count":778,"amount":1928611.1808777403}]},{"name":"manipur","metric":[{"type":"TOTAL","count":84069,"amount":1.2804617393020926E8}]},{"name":"maharashtra","metric":[{"type":"TOTAL","count":16387034,"amount":2.1711613257725674E10}]},{"name":"dadra & nagar haveli & daman & diu","metric":[{"type":"TOTAL","count":148549,"amount":1.7565838410921687E8}]},{"name":"meghalaya","metric":[{"type":"TOTAL","count":49571,"amount":6.625025978990036E7}]},{"name":"andaman & nicobar islands","metric":[{"type":"TOTAL","count":6658,"amount":1.463176122198579E7}]},{"name":"haryana","metric":[{"type":"TOTAL","count":4480770,"amount":6.793511514660528E9}]},{"name":"rajasthan","metric":[{"type":"TOTAL","count":7591690,"amount":8.926293130726837E9}]},{"name":"ladakh","metric":[{"type":"TOTAL","count":6089,"amount":1.2532857771114783E7}]},{"name":"punjab","metric":[{"type":"TOTAL","count":1870433,"amount":2.780758224854389E9}]},{"name":"assam","metric":[{"type":"TOTAL","count":1056881,"amount":1.157804456212469E9}]},{"name":"jharkhand","metric":[{"type":"TOTAL","count":2178921,"amount":2.3741863899194E9}]},{"name":"odisha","metric":[{"type":"TOTAL","count":5809821,"amount":4.627632210887628E9}]},{"name":"bihar","metric":[{"type":"TOTAL","count":5824302,"amount":6.045758172017314E9}]},{"name":"kerala","metric":[{"type":"TOTAL","count":1771380,"amount":2.402674753100502E9}]},{"name":"karnataka","metric":[{"type":"TOTAL","count":12016899,"amount":1.9217895314012802E10}]},{"name":"chandigarh","metric":[{"type":"TOTAL","count":381895,"amount":6.134354208676233E8}]},{"name":"telangana","metric":[{"type":"TOTAL","count":8522766,"amount":1.3308204118542435E10}]},{"name":"himachal pradesh","metric":[{"type":"TOTAL","count":481918,"amount":6.287378063723404E8}]},{"name":"west bengal","metric":[{"type":"TOTAL","count":11710225,"amount":1.0625978552140453E10}]},{"name":"gujarat","metric":[{"type":"TOTAL","count":5948775,"amount":7.577982255034092E9}]},{"name":"sikkim","metric":[{"type":"TOTAL","count":44078,"amount":6.465093894036834E7}]},{"name":"nagaland","metric":[{"type":"TOTAL","count":42845,"amount":7.800589108612517E7}]},{"name":"mizoram","metric":[{"type":"TOTAL","count":18561,"amount":4.5227219975790836E7}]},{"name":"chhattisgarh","metric":[{"type":"TOTAL","count":1891514,"amount":2.1491555572367463E9}]},{"name":"jammu & kashmir","metric":[{"type":"TOTAL","count":941568,"amount":1.0053712392561305E9}]},{"name":"goa","metric":[{"type":"TOTAL","count":160897,"amount":3.0385674234308386E8}]},{"name":"arunachal pradesh","metric":[{"type":"TOTAL","count":45497,"amount":9.238733600940911E7}]},{"name":"delhi","metric":[{"type":"TOTAL","count":7122754,"amount":1.121150380691996E10}]},{"name":"uttarakhand","metric":[{"type":"TOTAL","count":1246685,"amount":1.5085453585238864E9}]}]},"responseTimestamp":1630502909426}

import pandas as pd

def for_state():
    region_names=[]
    counts=[]
    amounts=[]
    for i in range(0, 11):
        region_name = m['data']['hoverDataList'][i]['name']
        count = m['data']['hoverDataList'][i]['metric'][0]['count']
        amount = m['data']['hoverDataList'][i]['metric'][0]['amount']
        region_names.append(region_name)
        counts.append(count)
        amounts.append(amount)


    state =pd.DataFrame(region_names)
    state.rename(columns={0:'States'},inplace=True)
    state['count']=counts
    state['Amount']=amounts
    return state

s=for_state()

#print(s)