import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/register')
def get_register():
  
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
            {"match_phrase":{"proxy.name.keyword":"ceria-user-registration"} }, 
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
  response = requests.get('http://172.18.216.251:9200/new-briapi-ext-prod-2*/_search', headers=hdr, json=body , auth=HTTPBasicAuth(username,password))
  data = response.json()
  #print(data)
  time= datetime.now()
  waktu = time.strftime("%H:%M")
  time2 = time + timedelta(hours=-2)
  waktu2 = time2.strftime("%H:%M")
  tgl = time.strftime("%d %B %Y")
  msg = ''
  msg = msg + "*Berikut Terlampir Report Ceria Api tanggal " + tgl + " " + " pada jam " + waktu2 + "-" + waktu + "* \n" 
  msg = msg + '\n'
  msg = msg + '\n'
  msg = msg + '*1.Ceria-Register*' + '\n'
  for bucket in data ["aggregations"]["2"]["buckets"]:
      a =str((bucket["key"]))
      c =(bucket['doc_count'])

      for bct in bucket["3"]["buckets"]:
       e = str(bct['key'])
       d = (bct['doc_count'])
       persen= d/c * 100
       p=str((format(persen, ".2f")))
       rc=str(d)
       if (a == '/initiate') and (e == '409') :
           text = ' Phone number already registered' + "|"
       elif (a == '/initiate') and (e == '400' ):
         text= ' Please agree to Bank BRI Term and Conditions to start register' + "|"
       elif (a == '/otp') and (e == '400' ):
         text= ' Wrong registration id | device id does not match with previous registration device id | INVALID_OTP' + "|"
       elif (a == '/pin') and (e == '400' ):
         text= ' Wrong registration id | PIN must be the same with confirmed PIN' + "|"
       elif (a == '/pin') and (e == '422' ):
         text= 'Invalid Registration Status' + "|"
       else:
         text = ""  
      
       register = a + " | " + e + " | " + rc + " | " + p +'%'+ " | " + text
       msg = msg + register + "\n"
        
  return msg
#get_register()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
      
  

