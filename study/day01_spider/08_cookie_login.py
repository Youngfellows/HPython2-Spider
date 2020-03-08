# coding=utf-8
import urllib2
import urllib

url = "https://ckpass.baidu.com/api/sync?bdu=WXpmbWM1ZGsxVGVUSkRWRkZQYVVFNFdtZG5jblJZYlVGNlRTMVlPV0pKWTJoTmRXaFlSRzVuZEg1eFdYaGxTVkZCUVVGQkpDUUFBQUFBQUFBQUFBRUFBQUNPU29zbnM4SzkzREl3TVRBd0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFIOGNaVjV%2BSEdWZU9Y&t=1583684738863"

headers = {
    "Host": "ckpass.baidu.com",
    "Connection": "keep-alive",
    # "Upgrade-Insecure-Requests" : "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "http://www.renren.com/SysHome.do",
    # "Accept-Encoding" : "gzip, deflate, sdch",
    "Cookie": "BAIDUID=29919210EDBD3418D167A8D07C6B1AB2:FG=1; BIDUPSID=29919210EDBD3418D167A8D07C6B1AB2; PSTM=1583071626; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; yjs_js_security_passport=d362e32c5675ad83146aca6d21f2f04a51fd8429_1583677269_js; H_PS_PSSID=30962_1463_21120_30789_30995_30824_26350_22158; cflag=13%3A3; BDUSS=Yzfmc5dk1TeTJDVFFPaUE4WmdncnRYbUF6TS1YOWJJY2hNdWhYRG5ndH5xWXhlSVFBQUFBJCQAAAAAAAAAAAEAAACOSosns8K93DIwMTAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH8cZV5~HGVeOX",
    "Accept-Language": "zh-CN,zh;q=0.9",
}

# 发送到web服务器的表单数据
formdata = {
    "bdu": "WXpmbWM1ZGsxVGVUSkRWRkZQYVVFNFdtZG5jblJZYlVGNlRTMVlPV0pKWTJoTmRXaFlSRzVuZEg1eFdYaGxTVkZCUVVGQkpDUUFBQUFBQUFBQUFBRUFBQUNPU29zbnM4SzkzREl3TVRBd0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFIOGNaVjV+SEdWZU9Y",
    "t": "1583684738863"
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data=data, headers=headers)

response = urllib2.urlopen(request)

print("code: %s" % response.getcode())
print("html: %s" % response.read())
