from core.resident import Resident
from core.robot import Robot, RobotMsg
from core.role import Role
from core.user import User
from server.BaseServ import BaseServer
import random
from config import client


class UserServer(BaseServer):
    def create_user(self, name, password, phone, role='USER'):
        print(role)
        self.session.add(
            User(user_name=name, true_name=name,
                 telephone=phone, password_md=password,
                 role=role)
        )

    def login(self, name, password):
        u = self.session.query(User).filter(User.user_name == name).first()
        print(u.password_md)
        print(password)
        if u and u.password_md == password:
            return u
        else:
            return None

    def create_robot(self):
        robot = Robot(model='joker', place=random.choice('ABCDEFG'))
        self.session.add(robot)
        self.session.flush()
        return robot.id

    def kill_robot(self):
        r = self.session.query(Robot).filter(Robot.status == 0).first()
        self.session.delete(r)

    def all_robot(self):
        return self.session.query(Robot).all()

    def create_robot_msg(self, uid):
        r = self.session.query(Robot).filter(Robot.status == 0).first()
        if r:
            r.status = 1
            m = RobotMsg(robot_id=r.id, user_id=uid)
            self.session.add(m)
            self.session.flush()
            return m.robot_id
        return r

    def get_robot_msg(self, uid):
        r = self.session.query(RobotMsg)\
            .filter(RobotMsg.user_id == uid, RobotMsg.status == 1)\
            .first()
        return r

    def done_robot_msg(self, uid):
        r = self.get_robot_msg(uid)
        r.status = 0
        self.session.query(Robot)\
            .filter(Robot.id == r.robot_id)\
            .update({Robot.status: 0})
        # return rid

    def get_resident(self, building=''):
        return self.session.query(Resident).filter(Resident.building.like(f'%{building}%')).all()

    def get_name(self, uid):
        return self.session.query(User).get(uid).user_name

    def bind_user(self, id, uid):
        r = self.session.query(Resident).get(id)
        r.user_id = uid

    def find_name(self, name):
        kk = self.session.query(User).filter(User.user_name.like(f'%{name}%')).all()
        d = []
        if kk:
            for index, k in enumerate(kk):
                d.append(dict(id=k.id, user_name=k.user_name))
        return d

    def get_role(self):
        return self.session.query(Role).all()

    def del_role(self, day, id):
        d = self.session.query(Role).get(day)
        l = d.role.split(';')
        l.remove(id)
        d.role = ';'.join(l)

    def add_role(self, day, id):
        d = self.session.query(Role).get(day)
        l = d.role and d.role.split(';') or []
        if id in l:
            return
        if d.role:
            d.role = (d.role + ';' + str(id)).strip(';')
        else:
            d.role = str(id)

    def get_text_user(self, text):
        return self.session.query(User).filter(User.role == 'ROLE', User.user_name.like(f'%{text}%')).all()


