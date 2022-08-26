import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from requests.api import get
from requests.structures import CaseInsensitiveDict
from requests.auth import HTTPBasicAuth
import pytz
import json

app = Flask(__name__)

@app.route('/login')
def get_login():
  username='monitoring_team'
  password='Monitoring123'
  hdr = {'Content-Type' : 'application/json'}
  body = {
   "aggs":{
      "2":{
         "terms":{"field":"proxy.suffix.keyword", "order":{"_count":"desc"}, "size":100 }, 
         "aggs":{"3":{"terms":{"field":"statusCode.keyword", "order":{"_count":"desc"}, "size":100 } } } }
   },
   "size":0,
   "stored_fields":["*"], 
   "script_fields":{
   },
   "_source":{"excludes":[] }, 
   "query":{
      "bool":{
         "must":[],
         "filter":[
            {"match_all":{} }, 
            {"match_phrase":{"meta.product.keyword":"ms-ceria-prod"} }, 
            {"match_phrase":{"proxy.name.keyword":"ceria-user-mobile-auth"} }, 
            {
               "range":{
                  "@timestamp":{
                     "gte":"now-2h",
                     "lte":"now",
                     "format":"strict_date_optional_time"
                  }
               }
            }
         ],
         "should":[],
         "must_not":[]
      }
   }
}
  response = requests.get('http://172.18.216.251:9200/new-briapi-ext-prod-2*/_search', headers=hdr, json=body, auth=HTTPBasicAuth(username,password))
  data = response.json()
  msg=''
  msg = msg + '*2.Ceria-Login*' + '\n'
  for bucket in data ["aggregations"]["2"]["buckets"]:
      a =str((bucket["key"]))
      c =(bucket['doc_count'])

      for bct in bucket["3"]["buckets"]:
       e = str(bct['key'])
       d = (bct['doc_count'])
       persen= d/c * 100
       p=str((format(persen, ".2f")))
       rc=str(d)
       if (a == '/login') and (e == '400') :
           text = ' Not Found' + "|"
       elif (a == '/login') and (e == '401' ):
         text= ' Unauthorized' + "|"
       elif (a == '/login') and (e == '403' ):
         text= ' User is locked. Please reset the password | Verify OTP Required' + "|"
       elif (a == '/login') and (e == '422' ):
         text= ' user not found (missing user data) | FRAUD INDICATED' + "|"
       elif (a == '/initiate') and (e == '400' ):
         text= 'Not Found' + "|"
       elif (a == '/initiate') and (e == '403' ):
         text= 'User is locked. Please reset the password' + "|"
       elif (a == '/initiate') and (e == '422' ):
         text= 'user not found (missing user data)' + "|"
       elif (a == '/verify otp') and (e == '400' ):
         text= 'Device id does not match with previous registration device id | INVALID_OTP | Invalid verify login id' + "|"
       elif (a == '/logout') and (e == '401' ):
         text= 'Invalid token format' + "|"
       else:
         text = ""  
         
       login = a + " | " + e + " | " + rc + " | " + p +'%'+ " | " + text
       msg = msg + login + "\n"
  return msg  

#get_login()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
      
      