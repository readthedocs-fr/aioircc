import tkinter as tk
import asyncio

FPS = 20

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
|--------------------------------|
"""

async def mainloop(root):
    while True:
        root.update()
        await asyncio.sleep(1 / FPS)

class Vue(tk.Frame):

    def __init__(self, master, inputs):
        super().__init__(master)
        self.inputs_function = inputs
        self.widgets = []
        self.load()

    def output(self, kwargs):
        ...

    def load(self):
        ...

class ConnectVue(Vue):

     def load(self):
        self.choose_host = tk.StringVar()

        host_text = tk.Label(self, text="Host :")
        host_text.pack()

        host_entry = tk.Entry(self, textvariable=self.choose_host)
        host_entry.pack()

        self.choose_port = tk.StringVar()

        port_text = tk.Label(self, text="Port :")
        port_text.pack()

        port_entry = tk.Entry(self, textvariable=self.choose_port)
        port_entry.pack()

        self.choose_nick = tk.StringVar()

        nick_text = tk.Label(self, text="Nick :")
        nick_text.pack()

        nick_entry = tk.Entry(self, textvariable=self.choose_nick)
        nick_entry.pack()

        connect_button = tk.Button(self, text="Connect")
        connect_button.pack()

async def switch(app):
    while True:
        await asyncio.sleep(1)
        app.pack_forget()
        await asyncio.sleep(1)
        app.pack()

def main():
    root = tk.Tk()
    app = ConnectVue(root, "")
    app.pack()
    loop = asyncio.new_event_loop()
    loop.create_task(mainloop(root))
    loop.create_task(switch(app))
    loop.run_forever()

if __name__ == "__main__":
    main()
