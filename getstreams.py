# coding:utf-8
import requests

#获取token，输入用户名密码
def login(username,password):
    url='http://api.eadiannet.com/OpenAPI/v1/user/loginphone?username={0}&password={1}&device=R6007'.format(username,password)
    log=requests.get(url).json()
    return log['data']['token']
#获取房间列表，类型为list
def getlist():
    url='http://api.eadiannet.com/OpenAPI/v1/Anchor/getAnchorListTest?token={0}&province=%E7%83%AD%E9%97%A8&device=R6007&token={1}'.format(token,token)
    res=requests.get(url).json()
    data=res['data']['list']
    return data
#获取直播流地址，需要房间号和token
def getrtmp(roomid,token):
    fullurl='http://api.eadiannet.com/OpenAPI/v1/qiniu/getPullAddress?roomID={0}&device=R6007&{1}'.format(roomid,token)
    rtmp=requests.get(fullurl).json()
    return rtmp['data']


if __name__=='__main__':
    #登录
    username=input('请输入用户名：')
    password=input('请输入密码：')
    #获取token
    token=login(username,password)
    #获取房间信息
    roomlist=getlist()
    #打印地址
    for item in roomlist:
        print(getrtmp(item['curroomnum'],token))
