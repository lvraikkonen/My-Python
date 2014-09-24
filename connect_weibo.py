from weibo import APIClient

APP_KEY = '3154041990' # app key
APP_SECRET = 'b817f3a4f74f51af23b26d7582dffd68' # app secret
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' # callback urlAPP_

client = APIClient(app_key=APP_KEY,
                   app_secret=APP_SECRET,
                   redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

## redirect to auth url
code = '43e4f01979c0a060e1333f5bba58a456'

## get url code
r = client.request_access_token(code)
access_token = r.access_token # token
expires_in = r.expires_in # token expire UNIX time：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
# TODO: save access token
client.set_access_token(access_token, expires_in)

## call API
print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u'测试OAuth 2.0发微博')
