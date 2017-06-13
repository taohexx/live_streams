# coding:utf-8
import requests
def getlist():
    url='http://www.xvsite.com/api/public/?service=Home.getHot'
    res=requests.get(url).json()
    data=res['data']['info'][0]['list']
    for info in data:
        print(info['pull'])

if __name__=="__main__":
    getlist()
