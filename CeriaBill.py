import os
import requests
from flask import Flask
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/bill')
def get_bill():
    username='ceria'
    password='Ceria123'
    hdr = {'Content-Type': 'application/json'}
    body = {
        "aggs": {
            "4": {
                "filters": {
                    "filters": {
                        "Bill - Send OTP Manual Payment": {
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
                                                        "query": "*\\/create\\-otp*"
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
                        "Bill - Resend OTP Manual Payment": {
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
                                                        "query": "*\\/resend\\-otp*"
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
                        "Bill - Confirm Manual Payment": {
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
                                                        "query": "*\\/payment*"
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
                        "Bill - Create Briva Payment": {
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
                                                        "query": "*\\/create\\/briva"
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
                        "Bill - Inquiry Briva Payment Status": {
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
                                                        "query": "*\\/detail\\?brivaPaymentId\\=*"
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
                        "Bill - Inquiry Bill Basic": {
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
                                                        "query": "*\\/basic"
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
                        "Bill - Inquiry Bill Detail": {
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
                                                        "query": "*\\/detail"
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
                        "Bill - Inquiry Bill History": {
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
                                                        "query": "*\\/history"
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
                        "Bill - Inquiry Bill History Detail": {
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
                                                        "query": "*\\/history\\/*"
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
                    "5": {
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
                    {"match_phrase": {"proxy.name.keyword": "ceria-bill"}},
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
    response = requests.get('http://172.18.216.251:9200/new-briapi-ext-prod-2*/_search', headers=hdr, json=body, auth=HTTPBasicAuth(username,password))
    data = response.json()
    msg = ''
    # print(data)
    # lihat semua key nya
    # for bucket in data ["aggregations"]["4"]["buckets"]:
    # print(bucket)

    # otpmanual
    listotpmanual = ''
    otpmanual1 = data["aggregations"]["4"]["buckets"]["Bill - Send OTP Manual Payment"]
    jumtotalotpmanual = otpmanual1['doc_count']
    otpmanual2 = data["aggregations"]["4"]["buckets"]["Bill - Send OTP Manual Payment"]["5"]["buckets"]
    for dataotpmanual in otpmanual2:
        namaotpmanual = "/otp-manual-payment"
        rcotpmanual = (dataotpmanual['key'])
        hitotpmanual1 = dataotpmanual['doc_count']
        hitotpmanual2 = (str(dataotpmanual['doc_count']))
        persenotpmanual = hitotpmanual1/jumtotalotpmanual * 100
        potpmanual = str((format(persenotpmanual, ".2f")))
        if (namaotpmanual == '/otp-manual-payment') and (rcotpmanual == '422'):
            text = ' Missing user data | User does not have facilities | PAYMENT_IN_PROGRESS | INVALID_AMOUNT ' + "|"
        else:
            text = ""

        otpmanual= namaotpmanual + " | " + rcotpmanual + " | " + hitotpmanual2 + " | " + potpmanual + '%' + " | " + text
        listotpmanual = listotpmanual + otpmanual + '\n'
    # resendotp
    listresendotp = ''
    resendotp1 = data["aggregations"]["4"]["buckets"]["Bill - Resend OTP Manual Payment"]
    jumtotalresendotp = resendotp1['doc_count']
    resendotp2 = data["aggregations"]["4"]["buckets"]["Bill - Resend OTP Manual Payment"]["5"]["buckets"]
    for dataresendotp in resendotp2:
        namaresendotp = "/resend-otp-manual-payment"
        rcresendotp = (dataresendotp['key'])
        hitresendotp1 = dataresendotp['doc_count']
        hitresendotp2 = (str(dataresendotp['doc_count']))
        persenresendotp = hitresendotp1/jumtotalresendotp * 100
        presendotp = str((format(persenresendotp, ".2f")))

        resendotp = namaresendotp + " | " + rcresendotp + " | " + hitresendotp2 + " | " + presendotp + '%' + " | "
        listresendotp = listresendotp + resendotp + '\n'

# confirm
    listconfirm = ''
    confirm1 = data["aggregations"]["4"]["buckets"]["Bill - Confirm Manual Payment"]
    jumtotalconfirm = confirm1['doc_count']
    confirm2 = data["aggregations"]["4"]["buckets"]["Bill - Confirm Manual Payment"]["5"]["buckets"]
    for dataconfirm in confirm2:
        namaconfirm = "/confirm-manual-payment"
        rcconfirm = (dataconfirm['key'])
        hitconfirm1 = dataconfirm['doc_count']
        hitconfirm2 = (str(dataconfirm['doc_count']))
        persenconfirm = hitconfirm1/jumtotalconfirm * 100
        pconfirm = str((format(persenconfirm, ".2f")))
        if (namaconfirm == '/confirm-manual-payment') and (rcconfirm == '403'):
            text = ' Invalid token format | Max Input OTP Has Been Reached | Transaction Failed | Wrong OTP ' + "|"
        else:
            text = ""

        confirm = namaconfirm + " | " + rcconfirm + " | " + hitconfirm2 + " | " + pconfirm + '%' + " | " + text
        listconfirm = listconfirm + confirm + '\n'
# briva
    listbriva = ''
    briva1 = data["aggregations"]["4"]["buckets"]["Bill - Create Briva Payment"]
    jumtotalbriva = briva1['doc_count']
    briva2 = data["aggregations"]["4"]["buckets"]["Bill - Create Briva Payment"]["5"]["buckets"]
    for databriva in briva2:
        namabriva = "/briva"
        rcbriva = (databriva['key'])
        hitbriva1 = databriva['doc_count']
        hitbriva2 = (str(databriva['doc_count']))
        persenbriva = hitbriva1/jumtotalbriva * 100
        pbriva = str((format(persenbriva, ".2f")))
        if (namabriva == '/briva') and (rcbriva == '409'):
            text = ' LAST_PAYMENT_PENDING ' + "|"
        else:
            text = ""

        briva = namabriva + " | " + rcbriva + " | " + hitbriva2 + " | " + pbriva + '%' + " | " + text
        listbriva = listbriva + briva + '\n'
# basic
    listbasic = ''
    basic1 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill Basic"]
    jumtotalbasic = basic1['doc_count']
    basic2 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill Basic"]["5"]["buckets"]
    for databasic in basic2:
        namabasic = "/basic"
        rcbasic = (databasic['key'])
        hitbasic1 = databasic['doc_count']
        hitbasic2 = (str(databasic['doc_count']))
        persenbasic = hitbasic1/jumtotalbasic * 100
        pbasic = str((format(persenbasic, ".2f")))
        if (namabasic == '/basic') and (rcbasic == '422'):
            text = ' Missing userdata | User does not have facilities |  Invalid id of 123. Please check your request payload ' + "|"
        else:
            text = ""

        basic = namabasic + " | " + rcbasic + " | " + hitbasic2 + " | " + pbasic + '%' + " | " + text
        listbasic = listbasic + basic + '\n'
# detail
    listdetail = ''
    detail1 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill Detail"]
    jumtotaldetail = detail1['doc_count']
    detail2 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill Detail"]["5"]["buckets"]
    for datadetail in detail2:
        namadetail = "/detail"
        rcdetail = (datadetail['key'])
        hitdetail1 = datadetail['doc_count']
        hitdetail2 = (str(datadetail['doc_count']))
        persendetail = hitdetail1/jumtotaldetail * 100
        pdetail = str((format(persendetail, ".2f")))
        if (namadetail == '/detail') and (rcdetail == '400'):
            text = ' Invalid id of 123. Please check your request payload ' + "|"
        else:
            text = ""

        detail = namadetail + " | " + rcdetail + " | " + hitdetail2 + " | " + pdetail + '%' + " | " + text
        listdetail = listdetail + detail + '\n'
# history
    listhistory = ''
    history1 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill History"]
    jumtotalhistory = history1['doc_count']
    history2 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill History"]["5"]["buckets"]
    for datahistory in history2:
        namahistory = "/history"
        rchistory = (datahistory['key'])
        hithistory1 = datahistory['doc_count']
        hithistory2 = (str(datahistory['doc_count']))
        persenhistory = hithistory1/jumtotalhistory * 100
        phistory = str((format(persenhistory, ".2f")))
        if (namahistory == '/history') and (rchistory == '400'):
            text = ' Invalid id of 123. Please check your request payload ' + "|"
        else:
            text = ""

        history = namahistory + " | " + rchistory + " | " + hithistory2 + " | " + phistory + '%' + " | " + text
        listhistory = listhistory + history + '\n'
# historydetail
    listhistorydetail = ''
    historydetail1 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill History Detail"]
    jumtotalhistorydetail = historydetail1['doc_count']
    historydetail2 = data["aggregations"]["4"]["buckets"]["Bill - Inquiry Bill History Detail"]["5"]["buckets"]
    for datahistorydetail in historydetail2:
        namahistorydetail = "/history-detail"
        rchistorydetail = (datahistorydetail['key'])
        hithistorydetail1 = datahistorydetail['doc_count']
        hithistorydetail2 = (str(datahistorydetail['doc_count']))
        persenhistorydetail = hithistorydetail1/jumtotalhistorydetail * 100
        phistorydetail = str((format(persenhistorydetail, ".2f")))
        if (namahistorydetail == '/history-detail') and (rchistorydetail == '400'):
            text = ' Invalid token format ' + "|"
        else:
            text = ""

        historydetail = namahistorydetail + " | " + rchistorydetail + " | " + hithistorydetail2 + " | " + phistorydetail + '%' + " | " + text
        listhistorydetail = listhistorydetail + historydetail + '\n'
# resend
    listresend= ''
    resend1 = data["aggregations"]["4"]["buckets"]["Bill - Resend OTP Manual Payment"]
    jumtotalresend = resend1['doc_count']
    resend2 = data["aggregations"]["4"]["buckets"]["Bill - Resend OTP Manual Payment"]["5"]["buckets"]
    for dataresend in resend2:
        namaresend = "/resend"
        rcresend = (dataresend['key'])
        hitresend1 = dataresend['doc_count']
        hitresend2 = (str(dataresend['doc_count']))
        persenresend = hitresend1/jumtotalresend * 100
        presend = str((format(persenresend, ".2f")))

        resend = namaresend + " | " + rcresend + " | " + hitresend2 + " | " + presend + '%' + " | "
        listresend= listresend + resend + '\n'

    msg = msg + '*6.Ceria-Bill*' + '\n' 
    msg = msg + listotpmanual
    msg = msg + listresendotp
    msg = msg + listconfirm
    msg = msg + listbriva
    msg = msg + listbasic
    msg = msg + listdetail
    msg = msg + listhistory
    msg = msg + listhistorydetail
    msg = msg + listresend

    return msg

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
