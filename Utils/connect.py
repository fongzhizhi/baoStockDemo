"""
连接到 baostock 系统，并自动退出登录
"""
import functools
import baostock as bs

def login(call):
    """
    登录系统，执行回调
    """
    @functools.wraps(call)
    def wrapped_view(**kwargs):
        # 登录系统
        bs.login()
        res = call(**kwargs)
        # 退出系统
        bs.logout()
        return res

    return wrapped_view