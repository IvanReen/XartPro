from helper import rd


def add_rank_week(artId):
    # 判断周排行"WeekRank" 是否存在
    flag = rd.exists('WeekRank')
    rd.zincrby('WeekRank', artId)
    if not flag:  # 如果之前的WeekRank不存在
        rd.expire('WeekRank', 604800)   # 一周的有效时间


def get_rank_week(top):
    '''
    获取周的阅读排行
    :param top: top n
    :return: ['1', '2', '3'] 按降序排列出art的id
    '''
    return [id.decode() for id in rd.zrevrange('WeekRank', 0, top-1)]