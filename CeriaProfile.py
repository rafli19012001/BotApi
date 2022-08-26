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


@app.route('/profile')
def get_profile():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "2": {
                "filters": {
                    "filters": {
                        "Change username - 1. Initiate( For user with no limit)": {
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
                                                        "query": "*\\/initiate"
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
                        "Change username - 1. Initiate( For user with active limit)": {
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
                                                        "query": "*\\/initiate\\-with\\-facility"
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
                        "Change username - 2. Confirm": {
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
                                                        "query": "*\\/confirm"
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
                        "Notification - Inquiry": {
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
                                                        "query": "*\\/notification"
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
                        "Notification - Inquiry detail by ID": {
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
                                                        "query": "*\\/notification\\/*"
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
                        "Change Email": {
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
                                                        "query": "*\\/change\\-email"
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
                        "Send Customer Feedback": {
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
                                                        "query": "*\\/customer\\-feedback"
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
                        "Profile - Inquiry": {
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
                                                        "query": "*\\/profile"
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
                    {"match_phrase": {"proxy.name.keyword": "ceria-user-profile"}},
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
    response = requests.get(
        'http://172.18.216.251:9200/new-briapi-ext-prod-2*/_search', headers=hdr, json=body, auth=HTTPBasicAuth(username,password))
    data = response.json()
    msg = ''
    # lihat semua key nya
    # for bucket in data ["aggregations"]["2"]["buckets"]:
    # print(bucket)
    # feedback
    listfeedback = ''
    feedback1 = data["aggregations"]["2"]["buckets"]["Send Customer Feedback"]
    jumtotalfeedback = feedback1['doc_count']
    feedback2 = data["aggregations"]["2"]["buckets"]["Send Customer Feedback"]["3"]["buckets"]
    for datafeedback in feedback2:
        namafeedback = "/feedback"
        rcfeedback = (datafeedback['key'])
        hitfeedback1 = datafeedback['doc_count']
        hitfeedback2 = (str(datafeedback['doc_count']))
        persenfeedback = hitfeedback1/jumtotalfeedback * 100
        pfeedback = str((format(persenfeedback, ".2f")))
        if (namafeedback == '/feedback') and (rcfeedback == '422'):
            text = ' Address Not Valid ' + "|"
        elif (namafeedback == '/feedback') and (rcfeedback == '409'):
            text = 'Email has been used. Please change feedback' + "|"
        else:
            text = ""

        feedback = namafeedback + " | " + rcfeedback + " | " + hitfeedback2 + " | " + pfeedback + '%' + " | " + text
        listfeedback = listfeedback + feedback + '\n'
    # inquiry
    listinqury = ''
    inquiry1 = data["aggregations"]["2"]["buckets"]["Profile - Inquiry"]
    jumtotalinquiry = inquiry1['doc_count']
    inquiry2 = data["aggregations"]["2"]["buckets"]["Profile - Inquiry"]["3"]["buckets"]
    for datainquiry in inquiry2:
        namainquiry = "/inquiry"
        rcinquiry = (datainquiry['key'])
        hitinquiry1 = datainquiry['doc_count']
        hitinquiry2 = (str(datainquiry['doc_count']))
        perseninquiry = hitinquiry1/jumtotalinquiry * 100
        pinquiry = str((format(perseninquiry, ".2f")))
        if (namainquiry == '/inquiry') and (rcinquiry == '422'):
            text = ' Address Not Valid ' + "|"
        elif (namainquiry == '/inquiry') and (rcinquiry == '409'):
            text = 'Email has been used. Please change inquiry' + "|"
        else:
            text = ""

        inquiry =namainquiry + " | " + rcinquiry + " | " + hitinquiry2 + " | " + pinquiry + '%' + " | " + text
        listinqury = listinqury + inquiry +  '\n'

    msg = msg + '*5.1.Ceria-Profile*' + '\n' 
    msg = msg + listfeedback
    msg = msg + listinqury

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
 