import json
import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from art.models import Art
from helper import rank, rd
from helper.tasks import buy



@cache_page(10)
def show(request, artId):
    time.sleep(3)
    art = Art.objects.get(pk=artId)

    rank.add_rank_week(artId)

    # 查询周阅读排行的文章(小说)
    rankArts = [Art.objects.get(pk=id) for id in rank.get_rank_week(6)]

    return render(request,
                  'art/show.html',
                  locals())


def qbuy(request, id):
    msg = None
    if 'login_user' not in request.session:
        msg = {'code': 101, 'msg': '请先登录'}
    else:
        login_user = json.loads(request.session.get('login_user'))

        # ? 解决同一账号登录，只限一个用户参与抢购
        buy.delay(login_user.get('id'), id)  # 异步执行

        msg = {'code':201, 'msg': '抢购中'}

    return JsonResponse(msg)


def buystate(request, id):  # 查询抢购的状态
    msg = None
    if 'login_user' not in request.session:
        msg = {'code': 101, 'msg': '请先登录'}
    else:
        # 获取登录的用户id
        uid = json.loads(request.session.get('login_user')).get('id')

        # 判断用户是否抢到
        if rd.hexists('qbuy', uid):
            gid = rd.hget('qbuy', uid).decode()
            msg = (
                {'code': 200, 'msg': '成功', 'gid': gid}
                if int(id) == int(gid)
                else {'code': 301, 'msg': '失败', 'content': '同一用户只能抢一部小说'}
            )

        elif rd.hlen('qbuy') < 5:
            # 没有达到限量
            msg = {'code': 201, 'msg': '抢购中'}
        else:
            msg = {'code': 300, 'msg': '抢购失败'}

    return JsonResponse(msg)