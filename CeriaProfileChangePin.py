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


@app.route('/changepin')
def get_changepin():
    username='ceria'
    password='Ceria123'
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
            {"match_phrase":{"proxy.name.keyword":"ceria-changepin"} }, 
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
    msg = ''
    msg = '*5.2.Ceria-Profil-Changepin*' + '\n'
    for bucket in data ["aggregations"]["2"]["buckets"]:
      a = '/changepin'
      c =(bucket['doc_count'])

      for bct in bucket["3"]["buckets"]:
       e = str(bct['key'])
       d = (bct['doc_count'])
       persen= d/c * 100
       p=str((format(persen, ".2f")))
       rc=str(d)
       if (a == '/changepin') and (e == '401') :
           text = ' Invalid token format ' + "|"
       elif (a == '/changepin') and (e == '400' ):
         text= ' PIN must be the same with confirmed PIN | INVALID_OTP_AUTH | ' + "|"
       else:
         text = ""  

       changepin = (a + " | " + e + " | " + rc + " | " + p +'%'+ " | " + text ) 
       msg = msg + changepin + '\n'

      return msg
      
#get_changepin()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

