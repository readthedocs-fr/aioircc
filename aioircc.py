"""
Legende :
<entry>
[button]
'text'

|---------------|
| host: <...>   |
| port: <...>   |
| nick: <...>   |
|               |
| [connect]     |
|---------------|

=>

|--------------------------------|
|[server] [#home] [#python]      |
|--------------------------------|
| 'Chat content'      | 'User'   |
| 'Chat content'      | 'User'   |
| Message : <...>     |          |
|--------------------------""
 s
"""

# ===========

class NetClient:
    def __init__(self):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

    async def connect():
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)

    async def diconnect():
        if not self.is_connected:
            return

        self.writer.write_eof()
        await self.writer.drain()
        while not self.reader.at_eof():
            await self.read()

        self.writer.close()
        await self.writer.wait_closed()

        self.reader = self.writer = None

    async def send(msg):
        self.writer.send(f'{msg}\r\n'.encode())
        return self.writer.drain()

    async def read_lines():
        while self.is_connected:
            yield await self.reader.readuntil(b'\r\n').decode().strip()

    @property
    def is_connected(self):
        return self.reader and not self.reader.at_eof


@dataclass
class Message:
    author: str
    text: str
    datetime: datetime = field(default_factory=datetime.now)


@dataclass
class Channel:
    name: str
    topic: str = ""
    users: set = field(default_factory=set)
    messages: list = field(default_factory=list)

# ==========

class Contoller:
    def __init__(self, netclient):
        self.netclient = netclient
        self.nick = None
        self.channels = []


    def onjoin(self, user, channel):
        if user == self.nick:
            pass
        else:
            pass


    def onnick(self, user, nick):
        pass


    def onquit(self, user):
        if user == self.nick:
            pass
        else:
            pass


    def onprivmsg(self, user):
        pass




def main():
    gui = Bidule(options.host, options.port)
    net_client = NetClient()


    loop = asyncio.new_event_loop()
    loop.create_task(gui.mainloop())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Press ctrl-c again to force exit.")
        loop.run_until_complete(net_client.disconnect())
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
    except Exception:
        raise SystemExit(1)
