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



def get_pengajuan():
    url = "http://172.18.216.251:5601/s/briapi-ext/api/metrics/vis/data"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["kbn-version"] = "7.10.1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "http://172.18.216.251:5601"
    headers["Referer"] = "http://172.18.216.251:5601/s/briapi-ext/app/visualize"
    headers["Accept-Language"] = "id-ID,id;q=0.9"
#headers["Cookie"] = "sid=Fe26.2**b4b763925a344763979608ad9a9013528f63509bc601a6099c6ddcf4e93560ba*SL9ssYYck_ZG7s0WMYrnRg*wgqw1NvAyVNvM6aNUMqeSDQGfMHxojrDds7-zAJUFgFTGWBf8fsgkfFoatj5gMRpP9uk4enqtfOzwIUQDt_xAJ6D-4MAtgHqmXYriHYlMF1KgzfE-_Pw1mdVtRS9LVfci8I7flQ6L_wdb9br6ER-hAhACiAgPzxDgXAYGy3HufCZIFHPlbFHZJlFGPbdmmp-j_ME0Z4kYp5IPr1a49j5cluTsrt-Kvw8UsxR-zEqEYyp7Yxf0xevyxJPjWCftK5R**06cd27b5f2bf9eed90ab9ffa106237cce15a9d2669a30365b9183b8d47dc056b*e83m8v6FuESkH7gB7FF7rvUSFAayPS-6EIl6BHQBAdU"
    UTC = pytz.utc
    t_end = datetime.now(UTC)
    t_start = t_end + timedelta(hours=-1)
    end = (t_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")  
    start = (t_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z") 
    data = '{"timerange":{"timezone":"Asia/Jakarta","min":"$start","max":"$end"},"query":[{"language":"kuery","query":""}],"filters":[],"panels":[{"id":"61ca57f0-469d-11e7-af02-69e470af7417","type":"gauge","series":[{"id":"61ca57f1-469d-11e7-af02-69e470af7417","color":"#68BC00","split_mode":"everything","split_color_mode":"kibana","metrics":[{"id":"61ca57f2-469d-11e7-af02-69e470af7417","type":"filter_ratio","numerator":{"query":"statusCode.keyword : 2*","language":"kuery"},"denominator":{"query":"statusCode.keyword : *","language":"kuery"}}],"separate_axis":0,"axis_position":"right","formatter":"percent","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","label":"","type":"timeseries"}],"time_field":"@timestamp","index_pattern":"new-briapi-ext-prod*","interval":"30m","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"show_grid":1,"tooltip_mode":"show_all","default_index_pattern":"new-briapi-ext-prod*","default_timefield":"@timestamp","isModelInvalid":false,"background_color_rules":[{"id":"ad59e4e0-ce4f-11eb-9975-612f9e282e60"}],"bar_color_rules":[{"id":"377a7590-ce50-11eb-9975-612f9e282e60"}],"gauge_color_rules":[{"value":0.9,"id":"65dd7590-ce50-11eb-9975-612f9e282e60","text":"rgba(253,17,17,1)","gauge":"rgba(253,17,17,1)","operator":"lt"},{"value":0.99,"id":"f6f62a20-ce52-11eb-8c31-35a66a1c5565","operator":"gte","text":"rgba(7,255,53,1)","gauge":"rgba(7,255,53,1)"},{"value":0.99,"id":"f81df840-d98a-11eb-b995-55a648def6ee","operator":"lt","gauge":"rgba(220,249,1,1)"}],"gauge_width":10,"gauge_inner_width":10,"gauge_style":"half","filter":{"query":"proxy.name.keyword : ceria-ekyc or proxy.name.keyword : ceria-loan-application","language":"kuery"},"gauge_max":""}],"state":{},"savedObjectId":"unsaved"}'
    data = data.replace("$start", start)
    data = data.replace("$end", end)
    resp = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('monitoring_team','Monitoring123'))
    data2 = resp.content
    data3 = json.loads(data2.decode('utf-8'))
    for bucket in data3['61ca57f0-469d-11e7-af02-69e470af7417']['series']:
        count= (bucket['data'][1][1])
        persen = count*100
        p=str((format(persen, ".3f"))).replace('.',',')
        if(persen>90):
           text='\U0001F7E2'
        else:
           text='\U0001F7E1'
        msg= text + ' '+ 'Pengajuan-sukses' + ' : ' + p + '%' + '\n'
    return msg 
        #print(t_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")  
        #print(t_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")

def get_merchant():
    url = "http://172.18.216.251:5601/s/briapi-ext/api/metrics/vis/data"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["kbn-version"] = "7.10.1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "http://172.18.216.251:5601"
    headers["Referer"] = "http://172.18.216.251:5601/s/briapi-ext/app/visualize"
    headers["Accept-Language"] = "id-ID,id;q=0.9"
#headers["Cookie"] = "sid=Fe26.2**b4b763925a344763979608ad9a9013528f63509bc601a6099c6ddcf4e93560ba*SL9ssYYck_ZG7s0WMYrnRg*wgqw1NvAyVNvM6aNUMqeSDQGfMHxojrDds7-zAJUFgFTGWBf8fsgkfFoatj5gMRpP9uk4enqtfOzwIUQDt_xAJ6D-4MAtgHqmXYriHYlMF1KgzfE-_Pw1mdVtRS9LVfci8I7flQ6L_wdb9br6ER-hAhACiAgPzxDgXAYGy3HufCZIFHPlbFHZJlFGPbdmmp-j_ME0Z4kYp5IPr1a49j5cluTsrt-Kvw8UsxR-zEqEYyp7Yxf0xevyxJPjWCftK5R**06cd27b5f2bf9eed90ab9ffa106237cce15a9d2669a30365b9183b8d47dc056b*e83m8v6FuESkH7gB7FF7rvUSFAayPS-6EIl6BHQBAdU"
    UTC = pytz.utc
    t_end = datetime.now(UTC)
    t_start = t_end + timedelta(hours=-1)
    end = (t_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")  
    start = (t_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")
    data = '{"timerange":{"timezone":"Asia/Jakarta","min":"$start","max":"$end"},"query":[{"query":"","language":"kuery"}],"filters":[],"panels":[{"id":"61ca57f0-469d-11e7-af02-69e470af7417","type":"gauge","series":[{"id":"61ca57f1-469d-11e7-af02-69e470af7417","color":"#68BC00","split_mode":"terms","split_color_mode":"kibana","metrics":[{"id":"b7e8e7f0-ce4d-11eb-b992-8fbdc88bf5c8","type":"filter_ratio","numerator":{"query":"statusCode.keyword : 2*","language":"kuery"},"denominator":{"query":"statusCode.keyword: * ","language":"kuery"}}],"separate_axis":0,"axis_position":"right","formatter":"percent","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","label":"","terms_field":"proxy.name.keyword","terms_include":"","terms_size":"100","terms_order_by":"_key"}],"time_field":"@timestamp","index_pattern":"new-briapi-ext-prod*","interval":"30m","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"show_grid":1,"tooltip_mode":"show_all","default_index_pattern":"new-briapi-ext-prod-v2-2021-*","default_timefield":"@timestamp","isModelInvalid":false,"background_color_rules":[{"id":"a4434dd0-ce4d-11eb-b992-8fbdc88bf5c8"}],"gauge_color_rules":[{"value":0.9,"id":"a4958c80-ce4d-11eb-b992-8fbdc88bf5c8","operator":"lt","text":"rgba(227,0,0,1)","gauge":"rgba(227,0,0,1)"},{"value":0.99,"id":"611a3310-ce4e-11eb-b992-8fbdc88bf5c8","operator":"gte","text":"rgba(0,255,55,1)","gauge":"rgba(0,255,55,1)"},{"value":0.99,"id":"c11e3a30-d98a-11eb-b995-55a648def6ee","operator":"lt","gauge":"rgba(222,251,3,1)"}],"gauge_width":10,"gauge_inner_width":10,"gauge_style":"half","filter":{"query":"proxy.name.keyword : *ceria*","language":"kuery"},"gauge_max":"","bar_color_rules":[{"id":"eef7cbc0-ce4e-11eb-9975-612f9e282e60"}]}],"state":{},"savedObjectId":"unsaved"}'
    data = data.replace("$start", start)
    data = data.replace("$end", end)
    resp = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('monitoring_team','Monitoring123'))
    data2 = resp.content
    data3 = json.loads(data2.decode('utf-8'))
    for bucket in data3['61ca57f0-469d-11e7-af02-69e470af7417']['series']:
        label= bucket['label']
        count= (bucket['data'][1][1])
        if (label== 'ceria-merchant'):
            label='Merchant-payment-SR'
            persen = count*100
            p= str((format(persen, ".3f"))).replace('.',',')
            if (persen>90):
                status='\U0001F7E2'
            elif(label =='ceria-changepin' and persen==0):
                status='\U0001F7E2'
            else:
                status='\U0001F7E1'
            msg= status + ' ' + label + ' : ' + p + '%' + '\n' 
    return msg

def get_suffix_succes_rate():
    url = "http://172.18.216.251:5601/s/briapi-ext/api/metrics/vis/data"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["kbn-version"] = "7.10.1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "http://172.18.216.251:5601"
    headers["Referer"] = "http://172.18.216.251:5601/s/briapi-ext/app/visualize"
    headers["Accept-Language"] = "id-ID,id;q=0.9"
#headers["Cookie"] = "sid=Fe26.2**b4b763925a344763979608ad9a9013528f63509bc601a6099c6ddcf4e93560ba*SL9ssYYck_ZG7s0WMYrnRg*wgqw1NvAyVNvM6aNUMqeSDQGfMHxojrDds7-zAJUFgFTGWBf8fsgkfFoatj5gMRpP9uk4enqtfOzwIUQDt_xAJ6D-4MAtgHqmXYriHYlMF1KgzfE-_Pw1mdVtRS9LVfci8I7flQ6L_wdb9br6ER-hAhACiAgPzxDgXAYGy3HufCZIFHPlbFHZJlFGPbdmmp-j_ME0Z4kYp5IPr1a49j5cluTsrt-Kvw8UsxR-zEqEYyp7Yxf0xevyxJPjWCftK5R**06cd27b5f2bf9eed90ab9ffa106237cce15a9d2669a30365b9183b8d47dc056b*e83m8v6FuESkH7gB7FF7rvUSFAayPS-6EIl6BHQBAdU"
    UTC = pytz.utc
    t_end = datetime.now(UTC)
    t_start = t_end + timedelta(hours=-1)
    end = (t_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")  
    start = (t_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z") 
    data = '{"timerange":{"timezone":"Asia/Jakarta","min":"$start","max":"$end"},"query":[{"query":"","language":"kuery"}],"filters":[],"panels":[{"id":"61ca57f0-469d-11e7-af02-69e470af7417","type":"gauge","series":[{"id":"61ca57f1-469d-11e7-af02-69e470af7417","color":"#68BC00","split_mode":"terms","split_color_mode":"kibana","metrics":[{"id":"b7e8e7f0-ce4d-11eb-b992-8fbdc88bf5c8","type":"filter_ratio","numerator":{"query":"statusCode.keyword : 2*","language":"kuery"},"denominator":{"query":"statusCode.keyword: * ","language":"kuery"}}],"separate_axis":0,"axis_position":"right","formatter":"percent","chart_type":"line","line_width":1,"point_size":1,"fill":0.5,"stacked":"none","label":"","terms_field":"proxy.name.keyword","terms_include":"","terms_size":"100","terms_order_by":"_key"}],"time_field":"@timestamp","index_pattern":"new-briapi-ext-prod*","interval":"30m","axis_position":"left","axis_formatter":"number","axis_scale":"normal","show_legend":1,"show_grid":1,"tooltip_mode":"show_all","default_index_pattern":"new-briapi-ext-prod-v2-2021-*","default_timefield":"@timestamp","isModelInvalid":false,"background_color_rules":[{"id":"a4434dd0-ce4d-11eb-b992-8fbdc88bf5c8"}],"gauge_color_rules":[{"value":0.9,"id":"a4958c80-ce4d-11eb-b992-8fbdc88bf5c8","operator":"lt","text":"rgba(227,0,0,1)","gauge":"rgba(227,0,0,1)"},{"value":0.99,"id":"611a3310-ce4e-11eb-b992-8fbdc88bf5c8","operator":"gte","text":"rgba(0,255,55,1)","gauge":"rgba(0,255,55,1)"},{"value":0.99,"id":"c11e3a30-d98a-11eb-b995-55a648def6ee","operator":"lt","gauge":"rgba(222,251,3,1)"}],"gauge_width":10,"gauge_inner_width":10,"gauge_style":"half","filter":{"query":"proxy.name.keyword : *ceria*","language":"kuery"},"gauge_max":"","bar_color_rules":[{"id":"eef7cbc0-ce4e-11eb-9975-612f9e282e60"}]}],"state":{},"savedObjectId":"unsaved"}'
    data = data.replace("$start", start)
    data = data.replace("$end", end)
    resp = requests.post(url, headers=headers, data=data, auth=HTTPBasicAuth('monitoring_team','Monitoring123'))
    data2 = resp.content
    data3 = json.loads(data2.decode('utf-8'))
    msg = ''
    for bucket in data3['61ca57f0-469d-11e7-af02-69e470af7417']['series']:
        label= bucket['label']
        if (label=='ceria-briapi-prod-v1_0'):
            label=''
        else:
            count= (bucket['data'][1][1])
            a= (bucket['data'][1][1])
            if (type(a)== int):
                count= a
                persen = count*100
                p=str(persen).replace('.',',')
            elif(type(a)== float):
                persen = a*100
                p=str((format(persen, ".3f"))).replace('.',',')
            else:
                count= 0
                persen = count*0
                p=str((format(persen))).replace('.',',')
            if (persen>90):
                status='\U0001F7E2'
            elif(label =='ceria-changepin' and persen==0):
                status='\U0001F7E2'                
            else:
                status='\U0001F7E1'
            sr = status + ' '+label + ' : ' + p + '%'
            #print(label + ' : ' + p + '%' + ' (' + status + ") ")
            #print(sr)
            msg = msg + sr + '\n'
    return msg
            #return msg
            
 
@app.route('/successrate')
def succes_rate():
    time= datetime.now()
    waktu = time.strftime("%H:%M")
    time2 = time + timedelta(hours=-1)
    waktu2 = time2.strftime("%H:%M")
    msg = "*Berikut Terlampir Data Success Rate Ceria pada jam " + waktu2 + "-" + waktu + "*" + "\n"
    msg = msg + '\n' 
    msg = msg + get_pengajuan()
    msg = msg + get_merchant()
    msg = msg + get_suffix_succes_rate()
    msg = msg + '\n'
    return msg 
    
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)