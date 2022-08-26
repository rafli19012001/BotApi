import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/loan')
def get_loan():
  username='monitoring_team'
  password='Monitoring123'
  hdr = {'Content-Type' : 'application/json'}
  body = {
  "aggs": {
    "2": {
      "filters": {
        "filters": {
          "0. Apply - Inquiry by Loan App Id": {
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
                                  "match": {
                                    "req.url": "whitelist"
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
                                        "match": {
                                          "req.url": "ektp-google-vision"
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
                                              "match": {
                                                "req.url": "ocr-google-vision"
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
                                                    "match": {
                                                      "req.url": "ektp-thumbnail"
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
                                                          "match": {
                                                            "req.url": "personal"
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
                                                                "match": {
                                                                  "req.url": "family"
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
                                                                      "match": {
                                                                        "req.url": "employment"
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
                                                                            "match": {
                                                                              "req.url": "non-payroll"
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
                                                                                  "match": {
                                                                                    "req.url": "submit"
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
                                                                                        "match": {
                                                                                          "req.url": "resend-email"
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
                                                                                              "match": {
                                                                                                "req.url": "email"
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
                                                                                              "match": {
                                                                                                "req.url": "offer"
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
          },
          "1. Apply - Input NIK and ATM data (Whitelist)": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "whitelist"
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
          "2. Apply - Take KTP Photo (Upload KTP)": {
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
                          "query": "*ektp\\-google\\-vision*"
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
          "2.1. Apply - Check OCR KTP Progress": {
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
                          "query": "*ocr\\-google\\-vision*"
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
          "2.2. Apply - Get KTP Thumbnail": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url.keyword": "ektp-thumbnail"
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
          "3. Apply - Submit Personal Data": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "personal"
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
          "4. Apply - Submit Family Data": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "family"
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
          "5. Apply - Submit Employment Data": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "employment"
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
          "6. Apply - (Optional, Only for Non Payroll) Upload Slip Gaji": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "non-payroll"
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
          "7. Apply - Submit Credit Scoring": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "submit"
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
          "8. Apply - Resend Email": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "resend"
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
          "9. Apply - Trigger Verify Email (Check email_token on received email) Copy": {
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
                          "query": "*\\/email\\/*"
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
          "10. Apply - Accept or Reject Credit Offer": {
            "bool": {
              "must": [],
              "filter": [
                {
                  "bool": {
                    "should": [
                      {
                        "match": {
                          "req.url": "offer"
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
            {"match_phrase":{"proxy.name.keyword":"ceria-loan-application"} }, 
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
  msg = ''
  #lihat semua key nya 
  #for bucket in data ["aggregations"]["2"]["buckets"]:
   #print(bucket)
  
  
  #whitelist
  listwhitelist = ''
  whitelist1= data ["aggregations"]["2"]["buckets"]["1. Apply - Input NIK and ATM data (Whitelist)"]
  jumtotalwhitelist = whitelist1['doc_count']
  whitelist2= data ["aggregations"]["2"]["buckets"]["1. Apply - Input NIK and ATM data (Whitelist)"]["3"]["buckets"]
  for datawhitelist in whitelist2:
    namawhitelist = "/whitelist"
    rcwhitelist=(datawhitelist['key'])
    hitwhitelist1 = datawhitelist['doc_count']
    hitwhitelist2=(str(datawhitelist['doc_count']))
    persenwhitelist= hitwhitelist1/jumtotalwhitelist *100
    pwhitelist=str((format(persenwhitelist, ".2f")))
    if (namawhitelist == '/whitelist') and (rcwhitelist == '422') :
           text = ' KTP already used | ERROR_CUSTOM_DIALOG (fraud checking) ' + "|"
    elif (namawhitelist == '/whitelist') and (rcwhitelist == '400' ):
         text= 'Invalid loan application status to perform whitelist | Whitelist service is busy | bad card data | freeze' + "|"      
    else:
      text = ""
    
    whitelist = namawhitelist + " | " + rcwhitelist + " | " + hitwhitelist2 + " | " + pwhitelist + '%' + " | " + text
    listwhitelist= listwhitelist + whitelist + '\n'

#ocr
  listocr = ''
  ocr1= data ["aggregations"]["2"]["buckets"]["2.1. Apply - Check OCR KTP Progress"]
  jumtotalocr = ocr1['doc_count']
  ocr2= data ["aggregations"]["2"]["buckets"]["2.1. Apply - Check OCR KTP Progress"]["3"]["buckets"]
  for dataocr in ocr2:
    namaocr = "/ocr"
    rcocr=(dataocr['key'])
    hitocr1 = dataocr['doc_count']
    hitocr2=(str(dataocr['doc_count']))
    persenocr= hitocr1/jumtotalocr *100
    pocr=str((format(persenocr, ".2f")))
    if (namaocr == '/ocr') and (rcocr == '422') :
           text = ' image file type not allowed ' + "|"
    elif (namaocr == '/ocr') and (rcocr == '400' ):
         text= 'Invalid loan application status to perform whitelist' + "|"      
    else:
      text = ""
    
    ocr = namaocr + " | " + rcocr + " | " + hitocr2 + " | " + pocr + '%' + " | " + text
    listocr = listocr + ocr + '\n'


#personal
  listpersonal = ''
  personal1= data ["aggregations"]["2"]["buckets"]["3. Apply - Submit Personal Data"]
  jumtotalpersonal = personal1['doc_count']
  personal2= data ["aggregations"]["2"]["buckets"]["3. Apply - Submit Personal Data"]["3"]["buckets"]
  for datapersonal in personal2:
    namapersonal = "/personal"
    rcpersonal=(datapersonal['key'])
    hitpersonal1 = datapersonal['doc_count']
    hitpersonal2=(str(datapersonal['doc_count']))
    persenpersonal= hitpersonal1/jumtotalpersonal *100
    ppersonal=str((format(persenpersonal, ".2f")))
    if (namapersonal == '/personal') and (rcpersonal == '422') :
           text = ' Address Not Valid ' + "|"
    elif (namapersonal =='/personal') and (rcpersonal == '409' ):
         text= 'Email has been used. Please change email' + "|"      
    else:
      text = ""
    
    personal = namapersonal + " | " + rcpersonal + " | " + hitpersonal2 + " | " + ppersonal + '%' + " | " + text
    listpersonal = listpersonal + personal + '\n'

#family
  listfamily = ''
  family1= data ["aggregations"]["2"]["buckets"]["4. Apply - Submit Family Data"]
  jumtotalfamily = family1['doc_count']
  family2= data ["aggregations"]["2"]["buckets"]["4. Apply - Submit Family Data"]["3"]["buckets"]
  for datafamily in family2:
    namafamily = "/family"
    rcfamily=(datafamily['key'])
    hitfamily1 = datafamily['doc_count']
    hitfamily2=(str(datafamily['doc_count']))
    persenfamily= hitfamily1/jumtotalfamily *100
    pfamily=str((format(persenfamily, ".2f")))
    if (namafamily == '/family') and (rcfamily == '422') :
           text = 'Phone Number Emergency Contact Same With Phone Number User | cifdetail payload is not valid | mother name is not equal with cifdetail mother name | ADDRESS_SIMILARITY with emergency contact ' + "|"
    elif (namafamily =='/family') and (rcfamily == '400' ):
         text= 'child \"emergency_contact\" fails because [child \"zip_code\" fails because [\"zip_code\" length must be less than or equal to 5 characters long (invalid payload)' + "|"      
    else:
      text = ""
    
    family = namafamily + " | " + rcfamily + " | " + hitfamily2 + " | " + pfamily + '%' + " | " + text
    listfamily = listfamily + family + '\n'

#employment
  listemployment = ''
  employment1= data ["aggregations"]["2"]["buckets"]["5. Apply - Submit Employment Data"]
  jumtotalemployment = employment1['doc_count']
  employment2= data ["aggregations"]["2"]["buckets"]["5. Apply - Submit Employment Data"]["3"]["buckets"]
  for dataemployment in employment2:
    namaemployment = "/employment"
    rcemployment=(dataemployment['key'])
    hitemployment1 = dataemployment['doc_count']
    hitemployment2=(str(dataemployment['doc_count']))
    persenemployment= hitemployment1/jumtotalemployment *100
    pemployment=str((format(persenemployment, ".2f")))
    if (namaemployment == '/employment') and (rcemployment == '400') :
           text = ' Invalid token format ' + "|"
    elif (namaemployment =='/employment') and (rcemployment == '403' ):
         text='npwp is not valid | npwp already used' + "|"      
    else:
      text = ""
    
    employment = namaemployment + " | " + rcemployment + " | " + hitemployment2 + " | " + pemployment + '%' + " | " + text
    listemployment= listemployment + employment + '\n'
#submit-Credit-Scoring
  listsubmit = ''
  submit1= data ["aggregations"]["2"]["buckets"]["7. Apply - Submit Credit Scoring"]
  jumtotalsubmit = submit1['doc_count']
  submit2= data ["aggregations"]["2"]["buckets"]["7. Apply - Submit Credit Scoring"]["3"]["buckets"]
  for datasubmit in submit2:
    namasubmit = "/submit-credit-scoring"
    rcsubmit=(datasubmit['key'])
    hitsubmit1 = datasubmit['doc_count']
    hitsubmit2=(str(datasubmit['doc_count']))
    persensubmit= hitsubmit1/jumtotalsubmit *100
    psubmit=str((format(persensubmit, ".2f")))
    if (namasubmit == '/submit-credit-scoring') and (rcsubmit == '400') :
           text = ' Loan application data is not completed to submit. Please check again ' + "|"
    elif (namasubmit =='/submit-credit-scoringt') and (rcsubmit == '422' ):
         text= 'credit scoring service is busy' + "|"      
    else:
      text = ""
    
    submit = namasubmit + " | " + rcsubmit + " | " + hitsubmit2 + " | " + psubmit + '%' + " | " + text
    listsubmit = listsubmit + submit + '\n'
#resend
  listresend = ''
  resend1= data ["aggregations"]["2"]["buckets"]["8. Apply - Resend Email"]
  jumtotalresend = resend1['doc_count']
  resend2= data ["aggregations"]["2"]["buckets"]["8. Apply - Resend Email"]["3"]["buckets"]
  for dataresend in resend2:
    namaresend = "/resend"
    rcresend=(dataresend['key'])
    hitresend1 = dataresend['doc_count']
    hitresend2=(str(dataresend['doc_count']))
    persenresend= hitresend1/jumtotalresend *100
    presend=str((format(persenresend, ".2f")))
    
    resend = namaresend + " | " + rcresend + " | " + hitresend2 + " | " + presend + '%' + " | " + text
    listresend = listresend + resend + '\n'
#email
  listemail = ''
  email1= data ["aggregations"]["2"]["buckets"]["9. Apply - Trigger Verify Email (Check email_token on received email) Copy"]
  jumtotalemail = email1['doc_count']
  email2= data ["aggregations"]["2"]["buckets"]["9. Apply - Trigger Verify Email (Check email_token on received email) Copy"]["3"]["buckets"]
  for dataemail in email2:
    namaemail = "/email"
    rcemail=(dataemail['key'])
    hitemail1 = dataemail['doc_count']
    hitemail2=(str(dataemail['doc_count']))
    persenemail= hitemail1/jumtotalemail *100
    pemail=str((format(persenemail, ".2f")))

    email = namaemail + " | " + rcemail + " | " + hitemail2 + " | " + pemail + '%' + " | " + text
    listemail = listemail + email + '\n'

#accept
  listaccept = ''
  accept1= data ["aggregations"]["2"]["buckets"]["10. Apply - Accept or Reject Credit Offer"]
  jumtotalaccept = accept1['doc_count']
  accept2= data ["aggregations"]["2"]["buckets"]["10. Apply - Accept or Reject Credit Offer"]["3"]["buckets"]
  for dataaccept in accept2:
    namaaccept = "/accept"
    rcaccept=(dataaccept['key'])
    hitaccept1 = dataaccept['doc_count']
    hitaccept2=(str(dataaccept['doc_count']))
    persenaccept= hitaccept1/jumtotalaccept *100
    paccept=str((format(persenaccept, ".2f")))
    if (namaaccept == '/accept') and (rcaccept == '422') :
           text = ' Missing user data | User email has not been verified | Loan offer already expired | You must agree to tnc if you want to accept loan offer ' + "|"      
    else:
      text = ""
    
    accept = namaaccept + " | " + rcaccept + " | " + hitaccept2 + " | " + paccept + '%' + " | " + text
    listaccept = listaccept + accept + '\n'

  msg = msg + '*3.Ceria-Apply-loan*' + '\n' 
  msg = msg + listwhitelist
  msg = msg + listocr
  msg = msg + listpersonal
  msg = msg + listfamily
  msg = msg + listemployment
  msg = msg + listsubmit
  msg = msg + listresend
  msg = msg + listemail
  msg = msg + listaccept 

  return msg


#get_loan()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)