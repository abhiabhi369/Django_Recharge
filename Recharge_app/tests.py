from django.test import TestCase

import datetime
from datetime import date,datetime
# present = datetime.datetime.now()
# print(present)
# future = datetime.datetime(2022,1,10)
# print(future)
# if present<future:
#     print('ok')

month_formate = {
    '01':1,
    '02':2,
    '03':3,
    '04':4,
    '05':5,
    '06':6,
    '07':7,
    '08':8,
    '09':9,
    '10':10,
    '11':11,
    '12':12
}

future_date = '2022-01-10'
fyear = future_date[0:4]
fmonth = future_date[5:7]
fdate = future_date[-2:]
print(int(fdate),month_formate[fmonth],int(fyear))
present = datetime.now()
future = datetime(int(fyear),month_formate[fmonth],int(fdate))
if present > future:
    print('greater')
else:
    print('less than future')

