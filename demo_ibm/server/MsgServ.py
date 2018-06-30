from sqlalchemy import desc

from config import client
from core.msg import Msg
from server.BaseServ import BaseServer


class MsgServer(BaseServer):
    def set_msg(self, id, msg):
        self.session.add(Msg(user_id=id, message=msg))

    def get_msg(self):
        return self.session.query(Msg).filter(Msg.flag).order_by(desc(Msg.id)).all()

    def get_my_msg(self, user_id):
        return self.session.query(Msg).filter(Msg.user_id == user_id).order_by(desc(Msg.id)).all()

    def call_msg(self, id, call):
        self.session.query(Msg).filter(Msg.id == id).update({Msg.call: call, Msg.flag: False})

    @staticmethod
    def baidu_pic(pic):
        image = pic.read()
        """ 调用车牌识别 """
        client.licensePlate(image)
        """ 如果有可选参数 """
        options = {}
        options["multi_detect"] = "true"
        """ 带参数调用车牌识别 """
        license = client.licensePlate(image, options)
        if license:
            return license.get('words_result')[0].get('number')
        return
