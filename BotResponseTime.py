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


@app.route('/responsetime')
def get_response_time():
    print("execute get_response_time")
    url = "http://172.18.216.251:5601/s/briapi-ext/api/metrics/vis/data"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["kbn-version"] = "7.10.1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "http://localhost:55"
    headers["Referer"] = "http://localhost:55/s/briapi-ext/app/visualize"
    headers["Accept-Language"] = "id-ID,id;q=0.9"
    UTC = pytz.utc
    t_end = datetime.now(UTC)
    t_start = t_end + timedelta(hours=-1)
    end = (t_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")  
    start = (t_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z") 
    data = '{"timerange":{"timezone":"Asia/Jakarta","min":"$start","max":"$end"},"query":[{"query":"","language":"kuery"}],"filters":[],"panels":[{"id":"61ca57f0-469d-11e7-af02-69e470af7417","type":"metric","series":[{"id":"61ca57f1-469d-11e7-af02-69e470af7417","color":"#68BC00","split_mode":"terms","split_color_mode":"kibana","metrics":[{"id":"61ca57f2-469d-11e7-af02-69e470af7417","type":"avg","field":"elapsedTime","numerator":{"query":"elapsedTime > 3000","language":"kuery"},"denominator":{"query":"elapsedTime : * ","language":"kuery"}}],"separate_axis":0,"axis_position":"right","formatter":"\'0,0\'","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","label":"Response Time","terms_field":"proxy.name.keyword","terms_exclude":"","terms_size":"20"}],"time_field":"@timestamp","index_pattern":"","interval":"30m","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"show_grid":1,"tooltip_mode":"show_all","default_index_pattern":"new-briapi-ext-prod-v2-2021-*","default_timefield":"@timestamp","isModelInvalid":false,"background_color_rules":[{"value":3000,"id":"216d6990-d3fc-11eb-ae2c-05a738296b43","background_color":"","color":"rgba(248,236,2,1)","operator":"gt"},{"value":3000,"id":"711fde80-d3fe-11eb-ae2c-05a738296b43","color":"rgba(0,255,55,1)","operator":"lt"},{"value":5000,"id":"01e3b430-dfa5-11eb-a62e-c72791dfaee0","color":"rgba(244,6,6,1)","operator":"gt"}],"filter":{"query":"proxy.name.keyword : *ceria*","language":"kuery"},"ignore_global_filter":0,"gauge_color_rules":[{"value":3000,"id":"55d445b0-d4eb-11eb-9ae8-cbc7edf1f923","gauge":"rgba(255,247,0,1)","operator":"gt"},{"value":3000,"id":"8efb1a60-d989-11eb-b995-55a648def6ee","operator":"lt","gauge":"rgba(8,252,73,1)"},{"value":5000,"id":"a1c48550-d989-11eb-b995-55a648def6ee","operator":"gt","gauge":"rgba(254,0,0,1)"}],"gauge_width":10,"gauge_inner_width":10,"gauge_style":"circle","gauge_max":""}],"state":{},"savedObjectId":"unsaved"}'
    data = data.replace("$start", start)
    data = data.replace("$end", end)
    resp = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('monitoring_team','Monitoring123'))
    data2 = resp.content
    #print(data2)
    data3 = json.loads(data2.decode('utf-8'))
    #print(data2)

    time= datetime.now()
    waktu = time.strftime("%H:%M")
    time2 = time + timedelta(hours=-1)
    waktu2 = time2.strftime("%H:%M")
    msg = "*Berikut Terlampir Data Response Time Ceria pada jam " + waktu2 + "-" + waktu + "*" + '\n'
    msg = msg + '\n'

    for bucket in data3['61ca57f0-469d-11e7-af02-69e470af7417']['series']:
        label= bucket['label']
        count= ((bucket['data'][1][1]))
        if  (type(count)== 'NoneType') and (count=='None'):
            count=''
        else:
            count2=count 
            hit = str(count2)
     
        if(label=='finacle-ceria'):
            label=''
        elif(label=='ceria-ms-email-prod-v1_0'):
            label=''
        elif(label=='credit-scoring-callback-ceria'):
            label=''
        elif(label=='whitelist-ceria'):
            label=''
        elif(hit=='None'):
            hit=''
        else:
            hit2=float(hit)
            hit3=round(hit2)
            hit4=str(hit3)
            if (hit3>=3000 and hit3<10000):
                text= '\U0001F7E1'
                msg = msg + text +' '+ label + ' : ' + hit4 + ' ms' + '\n'
            elif (hit3>=10000):
                text= '\U0001F534'
                msg = msg + text +' '+ label + ' : ' + hit4 + ' ms ' + '\n'
            else: 
                text= '\U0001F7E2'
                msg = msg + text +' '+label + ' : ' + hit4 + ' ms ' + '\n'
    msg = msg + '\n'
    #msg = msg + '*Untuk' + ' \U0001F7E1 '+ 'sedang di follow up*'
    return msg
    

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

#print(get_response_time())