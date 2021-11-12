import asyncio

from graia.ariadne.adapter import DefaultAdapter
from graia.ariadne.app import Ariadne
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.model import Friend, Group, MiraiSession
from graia.broadcast import Broadcast

loop = asyncio.new_event_loop()

bcc = Broadcast(loop=loop)
app = Ariadne(
    broadcast=bcc,
    adapter=DefaultAdapter(
        bcc,
        MiraiSession(
            host="http://localhost:4201",    #HttpAPI服务的地址
            verify_key="keyofMiraiHttpAPI",  #verifyKey
            account=123456789,              #机器人的QQ号
        ),
    )
)

@bcc.receiver("GroupMessage")
async def groupMessageListener(app: Ariadne, group: Group, message: MessageChain):
    if message.asDisplay() == "123":
        await app.sendMessage(group, MessageChain.create([
            Plain("OK")
        ]))

loop.run_until_complete(app.lifecycle())
