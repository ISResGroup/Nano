from graia.broadcast import Broadcast
from graia.application.entry import GraiaMiraiApplication, Session, MessageChain, Group, Plain
import asyncio

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:4201",   #HttpAPI服务的地址
        authKey="keyofMiraiHttpAPI",    #authKey
        account=1234567890,             #机器人的QCIC账号
        websocket=True
    )
)

@bcc.receiver("GroupMessage")
async def groupMessageListener(app: GraiaMiraiApplication, group: Group, mess: MessageChain):
    if mess.asDisplay() == "123":
        await app.sendGroupMessage(group, MessageChain.create([
            Plain("OK")
        ]))

app.launch_blocking()