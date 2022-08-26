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


@app.route('/install')
def get_installment():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "2": {
                "filters": {
                    "filters": {
                        "Installment - Inquiry Active Installment": {
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
                                                        "query": "*\\/active"
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
                        "Installment - Inquiry History Installment": {
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
                                                        "query": "*\\/history*"
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
                        "Installment - Inquiry Installment Detail": {
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
                                                        "query": "*\\/detail\\/*"
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
        "_source": {"excludes": []},
        "query": {
            "bool": {
                "must": [],
                "filter": [
                    {"match_all": {}},
                    {"match_phrase": {"meta.product.keyword": "ms-ceria-prod"}},
                    {"match_phrase": {"proxy.name.keyword": "ceria-loan-installment"}},
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
    # feedback
    # inquiry
    listinquiry = ''
    inquiry1 = data["aggregations"]["2"]["buckets"]["Installment - Inquiry Active Installment"]
    jumtotalinquiry = inquiry1['doc_count']
    inquiry2 = data["aggregations"]["2"]["buckets"]["Installment - Inquiry Active Installment"]["3"]["buckets"]
    for datainquiry in inquiry2:
        namainquiry = "/active"
        rcinquiry = (datainquiry['key'])
        hitinquiry1 = datainquiry['doc_count']
        hitinquiry2 = (str(datainquiry['doc_count']))
        perseninquiry = hitinquiry1/jumtotalinquiry * 100
        pinquiry = str((format(perseninquiry, ".2f")))
        if (namainquiry == '/active') and (rcinquiry == '401'):
            text = ' Invalid token format ' + "|"
        elif (namainquiry == '/active') and (rcinquiry == '422'):
            text = 'Missing user data | Missing ODA Account' + "|"
        else:
            text = ""

        inquiry = namainquiry + " | " + rcinquiry + " | " + hitinquiry2 + " | " + pinquiry + '%' + " | " + text
        listinquiry = listinquiry + inquiry + '\n'

    # history
    listhistory = ''
    history1 = data["aggregations"]["2"]["buckets"]["Installment - Inquiry History Installment"]
    jumtotalhistory = history1['doc_count']
    history2 = data["aggregations"]["2"]["buckets"]["Installment - Inquiry History Installment"]["3"]["buckets"]
    for datahistory in history2:
        namahistory = "/history"
        rchistory = (datahistory['key'])
        hithistory1 = datahistory['doc_count']
        hithistory2 = (str(datahistory['doc_count']))
        persenhistory = hithistory1/jumtotalhistory * 100
        phistory = str((format(persenhistory, ".2f")))

        history= namahistory + " | " + rchistory + " | " + hithistory2 + " | " + phistory + '%' + " | " + text
        listhistory = listhistory + history + '\n'

    msg = msg + '*7.Ceria-Installment*' + '\n' 
    msg = msg + listinquiry
    msg = msg + listhistory

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)