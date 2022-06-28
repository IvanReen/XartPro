from XartPro.celery import app

import time


from helper import rd


@app.task
def buy(uid, gid):
    print('--正在抢购--')
    msg = ''
    time.sleep(0.1)

    # 判断是否抢完（Redis-Hash:  qbuy）- 限量5部小说
    if rd.hlen('qbuy') < 5:
        # 下单(向订单表中增加成功购买的记录)
        # 向Redis-Hash的qbuy中存放抢购的商品信息（小说）
        # 判断用户是否已抢到
        if not rd.hexists('qbuy', uid):
            rd.hset('qbuy', uid, gid)
            msg = f'{uid} 抢购 {gid} 成功'
        else:
            msg = f'{uid} 只能抢购一部商品！'
    else:
        msg = f'{uid} 抢购 {gid} 商品失败!'

    return msg