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


@app.route('/merchant')
def get_merchant():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "2": {
                "filters": {
                    "filters": {
                        "Inquiry Whitelist": {
                            "bool": {
                                "must": [],
                                "filter": [
                                    {
                                        "bool": {
                                            "should": [
                                                {
                                                    "query_string": {
                                                        "fields": [
                                                            "proxy.suffix.keyword"
                                                        ],
                                                        "query": "*\\/whitelist\\/inquiry"
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
                        "Request Charges": {
                            "bool": {
                                "must": [],
                                "filter": [
                                    {
                                        "bool": {
                                            "should": [
                                                {
                                                    "match": {
                                                        "proxy.suffix.keyword": "/charges"
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
                        "Inquiry Charges": {
                            "bool": {
                                "must": [],
                                "filter": [
                                    {
                                        "bool": {
                                            "should": [
                                                {
                                                    "query_string": {
                                                        "fields": [
                                                            "proxy.suffix.keyword"
                                                        ],
                                                        "query": "\\/charges\\/*"
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
                        "Request Refund": {
                            "bool": {
                                "must": [],
                                "filter": [
                                    {
                                        "bool": {
                                            "should": [
                                                {
                                                    "query_string": {
                                                        "fields": [
                                                            "proxy.suffix.keyword"
                                                        ],
                                                        "query": "*\\/refund"
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
                            "proxy.name.keyword": "ceria-merchant"
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
# whitelist
    listwhitelist = ''
    whitelist1 = data["aggregations"]["2"]["buckets"]["Inquiry Whitelist"]
    jumtotalwhitelist = whitelist1['doc_count']
    whitelist2 = data["aggregations"]["2"]["buckets"]["Inquiry Whitelist"]["3"]["buckets"]
    for datawhitelist in whitelist2:
        namawhitelist = "/whitelist"
        rcwhitelist = (datawhitelist['key'])
        hitwhitelist1 = datawhitelist['doc_count']
        hitwhitelist2 = (str(datawhitelist['doc_count']))
        persenwhitelist = hitwhitelist1/jumtotalwhitelist * 100
        pwhitelist = str((format(persenwhitelist, ".2f")))

        whitelist = namawhitelist + " | " + rcwhitelist + " | " + hitwhitelist2 + " | " + pwhitelist + '%' + " | "
        listwhitelist = listwhitelist + whitelist + '\n'

# requestcharges
    listrequestcharges = ''
    requestcharges1 = data["aggregations"]["2"]["buckets"]["Request Charges"]
    jumtotalrequestcharges = requestcharges1['doc_count']
    requestcharges2 = data["aggregations"]["2"]["buckets"]["Request Charges"]["3"]["buckets"]
    for datarequestcharges in requestcharges2:
        namarequestcharges = "/request-charges"
        rcrequestcharges = (datarequestcharges['key'])
        hitrequestcharges1 = datarequestcharges['doc_count']
        hitrequestcharges2 = (str(datarequestcharges['doc_count']))
        persenrequestcharges = hitrequestcharges1/jumtotalrequestcharges * 100
        prequestcharges = str((format(persenrequestcharges, ".2f")))
        if (namarequestcharges == '/request-charges') and (rcrequestcharges == '400'):
            text = ' Invalid merchant | Transaction amount is less than ' + "|"
        else:
            text = ""

        requestcharges = namarequestcharges + " | " + rcrequestcharges + " | " + hitrequestcharges2 + " | " + prequestcharges + '%' + " | " + text
        listrequestcharges = listrequestcharges + requestcharges + '\n'

# charges
    listcharges = ''
    charges1 = data["aggregations"]["2"]["buckets"]["Inquiry Charges"]
    jumtotalcharges = charges1['doc_count']
    charges2 = data["aggregations"]["2"]["buckets"]["Inquiry Charges"]["3"]["buckets"]
    for datacharges in charges2:
        namacharges = "/charges"
        rccharges = (datacharges['key'])
        hitcharges1 = datacharges['doc_count']
        hitcharges2 = (str(datacharges['doc_count']))
        persencharges = hitcharges1/jumtotalcharges * 100
        pcharges = str((format(persencharges, ".2f")))

        charges = namacharges + " | " + rccharges + " | " + hitcharges2 + " | " + pcharges + '%' + " | "
        listcharges = listcharges + charges + '\n'

# requestrefund
    listrequestrefund = ''
    requestrefund1 = data["aggregations"]["2"]["buckets"]["Request Refund"]
    jumtotalrequestrefund = requestrefund1['doc_count']
    requestrefund2 = data["aggregations"]["2"]["buckets"]["Request Refund"]["3"]["buckets"]
    for datarequestrefund in requestrefund2:
        namarequestrefund = "/request-refund"
        rcrequestrefund = (datarequestrefund['key'])
        hitrequestrefund1 = datarequestrefund['doc_count']
        hitrequestrefund2 = (str(datarequestrefund['doc_count']))
        persenrequestrefund = hitrequestrefund1/jumtotalrequestrefund * 100
        prequestrefund = str((format(persenrequestrefund, ".2f")))
        if (namarequestrefund == '/request-refund') and (rcrequestrefund == '400'):
            text = ' Refund Failed from finacle ' + "|"
        else:
            text = ""

        requestrefund = namarequestrefund + " | " + rcrequestrefund + " | " + hitrequestrefund2 + " | " + prequestrefund + '%' + " | " + text
        listrequestrefund = listrequestrefund + requestrefund +  '\n'


    msg = msg + '*8.Ceria-Merchant-Payment*' + '\n' 
    msg = msg + listwhitelist
    msg = msg + listrequestcharges
    msg = msg + listcharges
    msg = msg + listrequestrefund

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)