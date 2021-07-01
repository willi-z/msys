from .core import *



module = Module(name="Test",
                description="Test Module",
                nodes=[Node("1", "http://127.0.0.1:8000"),
                       Node("2", "http://127.0.0.1:8000"),
                       Node("3", "http://127.0.0.1:8000")])

from .routers.server import ModuleServer

app = ModuleServer(module=module)