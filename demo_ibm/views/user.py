from flask import Blueprint, jsonify, request

from server.MsgServ import MsgServer
from server.UserServ import UserServer
from views.form.msg_form import CallInForm

bp = Blueprint('user', __name__)


@bp.route('call_in', methods=['POST'])
def call_in():
    form = CallInForm()
    data = form.data_with_csrf()
    with MsgServer() as s:
        s.set_msg(**data)
    return jsonify(code=0)


@bp.route('get_robot_user')
def use_robot():
    uid = request.args['uid']
    with UserServer() as s:
        r = s.get_robot_msg(uid)
    return jsonify(code=0, data=r and r.robot_id)


@bp.route('done_robot')
def done_robot():
    uid = request.args['uid']
    with UserServer() as s:
        rid = s.done_robot_msg(uid)
    return jsonify(code=0)


@bp.route('get_msg')
def get_msg():
    uid = request.args['uid']
    with MsgServer() as s:
        ml = s.get_my_msg(uid)
    return jsonify(code=0, data=ml and [dict(msg=x.message,
                                             time=x.createtime.strftime('%m月%d日'),
                                             call=x.call,
                                             flag=x.flag)
                                        for x in ml] or [])

