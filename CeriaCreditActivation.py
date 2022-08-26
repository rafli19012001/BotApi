import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/activation')
def get_activation():
  username='ceria'
  password='Ceria123'
  hdr = {'Content-Type' : 'application/json'}
  body = {
   "aggs": {
    "2": {
      "filters": {
        "filters": {
          "1. Activation - Asliri Match Face with NIK (Selfie 1)": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/asliri*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "2. Activation - Privy Register": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/privy\\-register*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "3. Activation - Privy Get Session": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/privy\\-session*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "4. Activation - Privy Send OTP": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/privy\\-send\\-otp*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "5. Activation - Privy Verify OTP": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/privy\\-verify\\-otp*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "6. Activation - Privy Face Compare (Selfie 2)": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/privy\\-face\\-compare*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "7. Activation - (Optional) Retry if Account Creation Failed (if eKYC Status = SIGN_DOCUMENT)": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "query_string": {
                          "fields": [
                            "req.url.keyword"
                          ],
                          "query": "*\\/account\\-creation*"
                        }
                      }
                    ],
                    "minimum_should_match": 1
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          },
          "0. Activation - Inquiry by eKYC Id": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "filter": [
                      {
                        "bool": {
                          "must_not": {
                            "bool": {
                              "should": [
                                {
                                  "query_string": {
                                    "fields": [
                                      "req.url.keyword"
                                    ],
                                    "query": "*ekyc_id*"
                                  }
                                }
                              ],
                              "minimum_should_match": 1
                            }
                          }
                        }
                      },
                      {
                        "bool": {
                          "filter": [
                            {
                              "bool": {
                                "must_not": {
                                  "bool": {
                                    "should": [
                                      {
                                        "query_string": {
                                          "fields": [
                                            "req.url.keyword"
                                          ],
                                          "query": "*\\/facility\\-document*"
                                        }
                                      }
                                    ],
                                    "minimum_should_match": 1
                                  }
                                }
                              }
                            },
                            {
                              "bool": {
                                "filter": [
                                  {
                                    "bool": {
                                      "must_not": {
                                        "bool": {
                                          "should": [
                                            {
                                              "query_string": {
                                                "fields": [
                                                  "req.url.keyword"
                                                ],
                                                "query": "*\\/tnc*"
                                              }
                                            }
                                          ],
                                          "minimum_should_match": 1
                                        }
                                      }
                                    }
                                  },
                                  {
                                    "bool": {
                                      "filter": [
                                        {
                                          "bool": {
                                            "must_not": {
                                              "bool": {
                                                "should": [
                                                  {
                                                    "query_string": {
                                                      "fields": [
                                                        "req.url.keyword"
                                                      ],
                                                      "query": "*\\/asliri*"
                                                    }
                                                  }
                                                ],
                                                "minimum_should_match": 1
                                              }
                                            }
                                          }
                                        },
                                        {
                                          "bool": {
                                            "filter": [
                                              {
                                                "bool": {
                                                  "must_not": {
                                                    "bool": {
                                                      "should": [
                                                        {
                                                          "query_string": {
                                                            "fields": [
                                                              "req.url.keyword"
                                                            ],
                                                            "query": "*\\/privy\\-register*"
                                                          }
                                                        }
                                                      ],
                                                      "minimum_should_match": 1
                                                    }
                                                  }
                                                }
                                              },
                                              {
                                                "bool": {
                                                  "filter": [
                                                    {
                                                      "bool": {
                                                        "must_not": {
                                                          "bool": {
                                                            "should": [
                                                              {
                                                                "query_string": {
                                                                  "fields": [
                                                                    "req.url.keyword"
                                                                  ],
                                                                  "query": "*\\/privy\\-session*"
                                                                }
                                                              }
                                                            ],
                                                            "minimum_should_match": 1
                                                          }
                                                        }
                                                      }
                                                    },
                                                    {
                                                      "bool": {
                                                        "filter": [
                                                          {
                                                            "bool": {
                                                              "must_not": {
                                                                "bool": {
                                                                  "should": [
                                                                    {
                                                                      "query_string": {
                                                                        "fields": [
                                                                          "req.url.keyword"
                                                                        ],
                                                                        "query": "*\\/privy\\-send\\-otp*"
                                                                      }
                                                                    }
                                                                  ],
                                                                  "minimum_should_match": 1
                                                                }
                                                              }
                                                            }
                                                          },
                                                          {
                                                            "bool": {
                                                              "filter": [
                                                                {
                                                                  "bool": {
                                                                    "must_not": {
                                                                      "bool": {
                                                                        "should": [
                                                                          {
                                                                            "query_string": {
                                                                              "fields": [
                                                                                "req.url.keyword"
                                                                              ],
                                                                              "query": "*\\/privy\\-verify\\-otp*"
                                                                            }
                                                                          }
                                                                        ],
                                                                        "minimum_should_match": 1
                                                                      }
                                                                    }
                                                                  }
                                                                },
                                                                {
                                                                  "bool": {
                                                                    "filter": [
                                                                      {
                                                                        "bool": {
                                                                          "must_not": {
                                                                            "bool": {
                                                                              "should": [
                                                                                {
                                                                                  "query_string": {
                                                                                    "fields": [
                                                                                      "req.url.keyword"
                                                                                    ],
                                                                                    "query": "*\\/privy\\-face\\-compare*"
                                                                                  }
                                                                                }
                                                                              ],
                                                                              "minimum_should_match": 1
                                                                            }
                                                                          }
                                                                        }
                                                                      },
                                                                      {
                                                                        "bool": {
                                                                          "must_not": {
                                                                            "bool": {
                                                                              "should": [
                                                                                {
                                                                                  "query_string": {
                                                                                    "fields": [
                                                                                      "req.url.keyword"
                                                                                    ],
                                                                                    "query": "*\\/account\\-creation* and"
                                                                                  }
                                                                                }
                                                                              ],
                                                                              "minimum_should_match": 1
                                                                            }
                                                                          }
                                                                        }
                                                                      }
                                                                    ]
                                                                  }
                                                                }
                                                              ]
                                                            }
                                                          }
                                                        ]
                                                      }
                                                    }
                                                  ]
                                                }
                                              }
                                            ]
                                          }
                                        }
                                      ]
                                    }
                                  }
                                ]
                              }
                            }
                          ]
                        }
                      }
                    ]
                  }
                }
              ],
              "should": [],
              "must_not": []
            }
          }
        }
      },
      "aggs": {
        "3": {
          "terms": {
            "field": "statusCode.keyword",
            "order": {
              "_count": "desc"
            },
            "size": 10
          }
        }
      }
    }
  },
  "size": 0,
  "stored_fields": ["*"],
   "script_fields":{
   },
   "_source":{"excludes":[] }, 
   "query":{
      "bool":{
         "must":[],
         "filter":[
            {"match_all":{} }, 
            {"match_phrase":{"meta.product.keyword":"ms-ceria-prod"} }, 
            {"match_phrase":{"proxy.name.keyword":"ceria-ekyc"} }, 
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
  #Register
  listregister = ''
  register1= data ["aggregations"]["2"]["buckets"]["2. Activation - Privy Register"]
  jumtotalregister = register1['doc_count']
  register2 = data ["aggregations"]["2"]["buckets"]["2. Activation - Privy Register"]["3"]["buckets"]
  for dataregister in register2:
    namaregister = "/register"
    rcregister=(dataregister['key'])
    hitregister1 = dataregister['doc_count']
    hitregister2=(str(dataregister['doc_count']))
    persenregister= hitregister1/jumtotalregister *100
    pregister=str((format(persenregister, ".2f")))
    if (namaregister == '/register') and (rcregister == '422') :
           text = ' Missing user data | email data is missing | Invalid privy registration | Invalid privy body response | Invalid token format"' + "|"
    else:
      text = ""  

    register= namaregister + " | " + rcregister + " | " + hitregister2 + " | " + pregister + '%' + " | " + text
    listregister = listregister + register + '\n'
  
  #get
  listget = ''
  get1= data ["aggregations"]["2"]["buckets"]["3. Activation - Privy Get Session"]
  jumtotalget = get1['doc_count']
  get2= data ["aggregations"]["2"]["buckets"]["3. Activation - Privy Get Session"]["3"]["buckets"]
  for dataget in get2:
    namaget = "/get"
    rcget=(dataget['key'])
    hitget1 = dataget['doc_count']
    hitget2=(str(dataget['doc_count']))
    persenget= hitget1/jumtotalget *100
    pget=str((format(persenget, ".2f")))
    if (namaget == '/get') and (rcget == '422') :
           text = ' Invalid to get privy session' + "|"
    else:
      text = "" 

    get = namaget + " | " + rcget + " | " + hitget2 + " | " + pget + '%' + " | " + text
    listget = listget + get + '\n'

 #otp
  listotp = ''
  otp1= data ["aggregations"]["2"]["buckets"]["4. Activation - Privy Send OTP"]
  jumtotalotp = otp1['doc_count']
  otp2= data ["aggregations"]["2"]["buckets"]["4. Activation - Privy Send OTP"]["3"]["buckets"]
  for dataotp in otp2:
    namaotp = "/otp"
    rcotp=(dataotp['key'])
    hitotp1 = dataotp['doc_count']
    hitotp2=(str(dataotp['doc_count']))
    persenotp= hitotp1/jumtotalotp *100
    potp=str((format(persenotp, ".2f")))
    if (namaotp == '/otp') and (rcotp == '422') :
           text = ' Invalid privy session for this ekyc ' + "|"
    else:
      text = ""
    otp = namaotp + " | " + rcotp + " | " + hitotp2 + " | " + potp + '%' + " | " + text
    listotp = listotp + otp + '\n'

 #verify-otp
  listverivyotp= ''
  verifyotp1= data ["aggregations"]["2"]["buckets"]["5. Activation - Privy Verify OTP"]
  jumtotalverifyotp = verifyotp1['doc_count']
  verifyotp2= data ["aggregations"]["2"]["buckets"]["5. Activation - Privy Verify OTP"]["3"]["buckets"]
  for dataverifyotp in verifyotp2:
    namaverifyotp = "/verify-otp"
    rcverifyotp=(dataverifyotp['key'])
    hitverifyotp1 = dataverifyotp['doc_count']
    hitverifyotp2=(str(dataverifyotp['doc_count']))
    persenverifyotp= hitverifyotp1/jumtotalverifyotp *100
    pverifyotp=str((format(persenverifyotp, ".2f")))
    if (namaverifyotp == '/verify-otp') and (rcverifyotp == '422') :
           text = ' Invalid Privy OTP | Invalid privy session for this ekyc ' + "|"
    else:
      text = ""
    verivyotp = namaverifyotp + " | " + rcverifyotp + " | " + hitverifyotp2 + " | " + pverifyotp + '%' + " | " + text
    listverivyotp = listverivyotp + verivyotp + '\n'
 #id
  listid = ''
  id1= data ["aggregations"]["2"]["buckets"]["0. Activation - Inquiry by eKYC Id"]
  jumtotalid = id1['doc_count']
  id2= data ["aggregations"]["2"]["buckets"]["0. Activation - Inquiry by eKYC Id"]["3"]["buckets"]
  for dataid in id2:
    namaid = "/id"
    rcid=(dataid['key'])
    hitid1 = dataid['doc_count']
    hitid2=(str(dataid['doc_count']))
    persenid= hitid1/jumtotalid *100
    pid=str((format(persenid, ".2f")))
    
    id = namaid + " | " + rcid + " | " + hitid2 + " | " + pid + '%' + " | "
    listid = listid + id + '\n'

  msg = msg + '*4.Ceria-Credit-Activation*' + '\n' 
  msg = msg + listregister
  msg = msg + listget
  msg = msg + listotp
  msg = msg + listverivyotp
  msg = msg + listid
  
  return msg 

#get_activation()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

    
  #print("--------------")
  #b= (a ["0. Activation - Inquiry by eKYC Id"])
  #print(type(a))
  #print(type(get))
  #print((get))


   #print(type(bucket))

   #print(type(bucket))
   #print(bucket[0])
   
 


    #print(bucket)
      
     #print(bct)
      
  
