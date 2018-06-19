import json
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
REGISTRY = {}


class MainHandler(RequestHandler):
    def post(self):
        body = self.get_argument("msg")
        uid = self.get_argument("uid")
        for _ in REGISTRY.get(uid, []):
            if _:
                _.write_message(json.dumps({"msg": body}))
                self.write("OK")
            else:
                self.write("NO")


class WSHandler(WebSocketHandler):
    def open(self, channel):
        print("WebSocket opened")
        self.uid = channel
        if REGISTRY.get(self.uid):
            REGISTRY[self.uid].append(self)
        else:
            REGISTRY[self.uid] = [self]

    def on_message(self, message):
        self.write_message(json.dumps({"msg": "hi, dog"}))

    def check_origin(self, origin):
        return True

    def on_close(self):
        print("WebSocket closed")
        del REGISTRY[self.uid]
