import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/cashout')
def get_cashout():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "2": {
                "filters": {
                    "filters": {
                        "Cashout - Inquiry List Merchant Support Cashout": {
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
                                                        "query": "*\\/list\\-merchant"
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
                        "Cashout - Request Charge for Cashout Rek BRI": {
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
                                                        "query": "*\\/charges*"
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
        "script_fields": {
        },
        "_source": {
            "excludes": []
        },
        "query": {
            "bool": {
                "must": [],
                "filter": [
                    {
                        "match_all": {}
                    },
                    {
                        "match_phrase": {
                            "proxy.name.keyword": "ceria-cashout"
                        }
                    },
                    {
                        "range": {
                            "@timestamp": {
                                "gte": "now-2h",
                                "lte": "now",
                                "format": "strict_date_optional_time"
                            }
                        }
                    }
                ],
                "should": [],
                "must_not": []
            }
        }
    }
    response = requests.get('http://172.18.216.251:9200/new-briapi-ext-prod-2*/_search', headers=hdr, json=body,auth=HTTPBasicAuth(username,password))
    data = response.json()
    msg = ''
    # print(data)
    # lihat semua key nya
    # for bucket in data ["aggregations"]["2"]["buckets"]:
    # print(bucket)

    # listmerchant
    listmerchant = ''
    listmerchant1 = data["aggregations"]["2"]["buckets"]["Cashout - Inquiry List Merchant Support Cashout"]
    jumtotallistmerchant = listmerchant1['doc_count']
    listmerchant2 = data["aggregations"]["2"]["buckets"]["Cashout - Inquiry List Merchant Support Cashout"]["3"]["buckets"]
    for datalistmerchant in listmerchant2:
        namalistmerchant = "/list-merchant"
        rclistmerchant = (datalistmerchant['key'])
        hitlistmerchant1 = datalistmerchant['doc_count']
        hitlistmerchant2 = (str(datalistmerchant['doc_count']))
        persenlistmerchant = hitlistmerchant1/jumtotallistmerchant * 100
        plistmerchant = str((format(persenlistmerchant, ".2f")))
        if (namalistmerchant == '/list-merchant') and (rclistmerchant == '400'):
            text = ' cashout more than 3 times this month ' + "|"
        else:
            text = ""

        merchant = namalistmerchant + " | " + rclistmerchant + " | " + hitlistmerchant2 + " | " + plistmerchant + '%' + " | " + text
        listmerchant = listmerchant + merchant + '\n'

# cashoutbri
    listcashout = ''
    cashoutbri1 = data["aggregations"]["2"]["buckets"]["Cashout - Request Charge for Cashout Rek BRI"]
    jumtotalcashoutbri = cashoutbri1['doc_count']
    cashoutbri2 = data["aggregations"]["2"]["buckets"]["Cashout - Request Charge for Cashout Rek BRI"]["3"]["buckets"]
    for datacashoutbri in cashoutbri2:
        namacashoutbri = "/cashout-BRI"
        rccashoutbri = (datacashoutbri['key'])
        hitcashoutbri1 = datacashoutbri['doc_count']
        hitcashoutbri2 = (str(datacashoutbri['doc_count']))
        persencashoutbri = hitcashoutbri1/jumtotalcashoutbri * 100
        pcashoutbri = str((format(persencashoutbri, ".2f")))

        cashout = namacashoutbri + " | " + rccashoutbri + " | " + hitcashoutbri2 + " | " + pcashoutbri + '%' + " | "
        listcashout = listcashout + cashout + '\n'
    
    msg = msg + '*9.Ceria-Cashout*' + '\n' 
    msg = msg + listmerchant
    msg = msg + listcashout

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

