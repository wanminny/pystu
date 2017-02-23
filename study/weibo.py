import requests
url_get_token = "https://api.weibo.com/oauth2/access_token"
#构建POST参数
playload = {
"client_id":"1720692856",
"client_secret":"46c5e57722a8cc285ee431cb71fb385e",
"grant_type":"code",
# "code":"上面获得的CODE",
"redirect_uri":"http://www.tuangoujf.com"
}
#POST请求
r = requests.post(url_get_token,data=playload)
#输出响应信息
print(r.text)

