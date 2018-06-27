from core.msg import Msg
from server.BaseServ import BaseServer
import random


class MsgServer(BaseServer):
    def set_msg(self, id, msg):
        self.session.add(Msg(user_id=id, message=msg))

    def get_msg(self):
        return self.session.query(Msg).filter(Msg.flag).all()

    def call_msg(self, id, call):
        self.session.query(Msg).filter(Msg.id == id).update({Msg.call: call, Msg.flag: False})
