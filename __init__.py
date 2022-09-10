#!/usr/bin/env python3
# coding=utf-8

import os
import random
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, GROUP, Message
from nonebot.plugin import on_command

__zx_plugin_name__ = "孙哥语音包"
__plugin_usage__ = """
usage：
    跟尸体对话吧！
        指令：
            [来点孙笑川]
""".strip()
__plugin_des__ = "尸体在说话"
__plugin_cmd__ = ["来点孙笑川"]
__plugin_type__ = ("一些工具",)
__plugin_version__ = 1.0
__plugin_author__ = "U2yyy"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["来点孙笑川"],
}

sun = on_command("来点孙笑川", aliases = {"孙哥","孙笑川","sun"}, permission=GROUP, priority=50)


@sun.handle()
async def _h(bot: Bot, event: GroupMessageEvent):

    num = random.randint(0,1313)
    sun_path = "/home/zhenxun_bot/plugins/sun/resources/voice/"
    filelist = os.listdir(sun_path)
    sun_mp3 = filelist[num]
    await sun.send(Message('[CQ:record,file=file:////home/zhenxun_bot/plugins/sun/resources/voice/'+sun_mp3+']'))
    await sun.finish()