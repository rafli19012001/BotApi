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


@app.route('/forgot')
def get_forgotpin():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "2": {
                "filters": {
                    "filters": {
                        "Forgot PIN - 1. Initiate": {
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
                                                        "query": "*\\/phone\\-initiate"
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
                        "Forgot PIN - 2. Verify OTP": {
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
                                                        "query": "*\\/verfiy\\-otp"
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
                        "Forgot PIN - 3. Confirm": {
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
                                                        "query": "*\\/change\\-pin"
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
                            "proxy.name.keyword": "ceria-forgot-pin"
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

    # initiate
    listinitiate = ''
    initiate1 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 1. Initiate"]
    jumtotalinitiate = initiate1['doc_count']
    initiate2 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 1. Initiate"]["3"]["buckets"]
    for datainitiate in initiate2:
        namainitiate = "/initiate"
        rcinitiate = (datainitiate['key'])
        hitinitiate1 = datainitiate['doc_count']
        hitinitiate2 = (str(datainitiate['doc_count']))
        perseninitiate = hitinitiate1/jumtotalinitiate * 100
        pinitiate = str((format(perseninitiate, ".2f")))
        if (namainitiate == '/initiate') and (rcinitiate == '401'):
            text = ' not authenticate ' + "|"
        elif (namainitiate == '/initiate') and (rcinitiate == '400'):
            text = ' You have reached maximum OTP resent ' + "|"
        elif (namainitiate == '/initiate') and (rcinitiate == '422'):
            text = ' Missing user ' + "|"
        else:
            text = ""

        initiate = namainitiate + " | " + rcinitiate + " | " + hitinitiate2 + " | " + pinitiate + '%' + " | " + text
        listinitiate = listinitiate + initiate + '\n'

    # verify-otp
    listverifyotp= ''
    verifyotp1 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 2. Verify OTP"]
    jumtotalverifyotp = verifyotp1['doc_count']
    verifyotp2 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 2. Verify OTP"]["3"]["buckets"]
    for dataverifyotp in verifyotp2:
        namaverifyotp = "/verify-otp"
        rcverifyotp = (dataverifyotp['key'])
        hitverifyotp1 = dataverifyotp['doc_count']
        hitverifyotp2 = (str(dataverifyotp['doc_count']))
        persenverifyotp = hitverifyotp1/jumtotalverifyotp * 100
        pverifyotp = str((format(persenverifyotp, ".2f")))
        if (namaverifyotp == '/verify-otp') and (rcverifyotp == '400'):
            text = ' MAX_OTP_INPUT_REACHED | INVALID_OTP | Device id does not match with previous registration device id ' + "|"
        else:
            text = ""

        verivyotp = namaverifyotp + " | " + rcverifyotp + " | " + hitverifyotp2 + " | " + pverifyotp + '%' + " | " + text
        listverifyotp  = listverifyotp + verivyotp + '\n'
# confirm
    listconfirm = ''
    confirm1 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 3. Confirm"]
    jumtotalconfirm = confirm1['doc_count']
    confirm2 = data["aggregations"]["2"]["buckets"]["Forgot PIN - 3. Confirm"]["3"]["buckets"]
    for dataconfirm in confirm2:
        namaconfirm = "/confirm"
        rcconfirm = (dataconfirm['key'])
        hitconfirm1 = dataconfirm['doc_count']
        hitconfirm2 = (str(dataconfirm['doc_count']))
        persenconfirm = hitconfirm1/jumtotalconfirm * 100
        pconfirm = str((format(persenconfirm, ".2f")))
        if (namaconfirm == '/confirm') and (rcconfirm == '400'):
            text = ' Invalid id of 123. Please check your request payload ' + "|"
        else:
            text = ""
        confirm = namaconfirm + " | " + rcconfirm + " | " + hitconfirm2 + " | " + pconfirm + '%' + " | " + text
        listconfirm = listconfirm + confirm + '\n'
    msg = msg + '*5.3.Ceria-Profil-Forgot-Pin*' + '\n' 
    msg = msg + listinitiate
    msg = msg + listverifyotp
    msg = msg + listconfirm

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
