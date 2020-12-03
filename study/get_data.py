# coding=utf-8
# author yanNa
# Data: 2020/8/20 21:49

from mitmproxy import http
def request(flow):
    request_data = flow.request
    request_url = request_data.url
    request_pr = request_data.query
    request_form = request_data.urlencoded_form
    print('url:============', request_url)
    print('pr:============', request_pr)
    print('form:============', request_form)

def response(flow):
    response_data = flow.response
    response_header = response_data.headers
    content_type = response_header['Content-Type']
    print('content-type===========', content_type)
    if 'image/jpeg' in content_type:
        print('这个返回的是图片')
    elif 'application/json' in content_type:
        status_code = response_data.status_code
        text = response_data.text
        print('code==========', status_code)
        print('text==========', text)
    else:
        print('格式不是我们预期的')

