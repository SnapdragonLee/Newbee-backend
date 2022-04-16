import hashlib
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
import json
import requests
from .models import WXUser
from utils.response import drf_response


# Create your views here.

@api_view(['POST'])
def user_login(request):
    appid = 'wx88389d0a4b41284e'
    secret = '9d6c00e3835e1af3dae970780f5429fd'
    code = request.data['code']
    url = 'https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid \
          + '&secret=' + secret + '&js_code=' + code + '&grant_type=authorization_code'
    response = json.loads(requests.get(url).content)
    if 'errcode' in response:
        return drf_response(3, "获取openid失败")

    openid = response['openid']
    session_key = response['session_key']

    user = WXUser.objects.filter(id=openid)
    if not user:
        new_user = WXUser(id=openid, user_name='默认用户名')
        new_user.save()

    request.session['openid'] = openid
    return drf_response(0)
    # sha = hashlib.sha256()
    # sha.update(openid.encode())
    # sha.update(session_key.encode())
    # key = sha.hexdigest()
    #
    # return Response(data={'ret': 0, 'key': key})
    pass
