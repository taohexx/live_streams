# coding:utf-8
import requests
def postdata():
    url='http://www.wipo360.com/Api/SiSi/getLive'
    data={'timestamp':'1493473697','limit_begin':0,'version_num':'2.0.0','limit_num':20,'os':'android','sign':'fd9ad9163eb1bac3bdd84c7b416ffbe6','soft_ver':'4.2.2','type':2}
    res=requests.post(url,data=data).json()
    #print(res['info'])
    for item in res['info']:
        print(item['channel_source'])
if __name__=="__main__":
    postdata()
